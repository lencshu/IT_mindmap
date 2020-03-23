import asyncio
import aiohttp
import aiomysql
import re
from pyquery import PyQuery

start_url = "http://www.jobbole.com/"
waiting_urls = []
seen_urls = set()
stopping = False

# 限制并发数量
sem = asyncio.Semaphore(3)


async def fetch(url, session):
    async with sem:
        try:
            async with session.get(url) as response:
                if response.status in [200, 201]:
                    return await response.text()
        except Exception as e:
            print(e)


def extract_urls(html):
    urls = []
    pq = PyQuery(html)
    for link in pq.items("a"):
        url = link.attr("href")
        if url and url.startswith("http") and url not in seen_urls:
            urls.append(url)
            waiting_urls.append(url)
    return urls


async def init_urls(url, session):
    html = await fetch(url, session)
    seen_urls.add(url)
    urls = await extract_urls(html)


async def article_handle(url, session, pool):
    """ 获取文章详情并解析入库 """
    html = await fetch(url, session)
    seen_urls.add(url)
    await extract_urls(html)
    pq = PyQuery(html)
    title = pq("title").text()
    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            insert_sql = f"insert into article_test(title) value ('{title}')"
            await cur.execute(insert_sql)
    pool.close()
    await pool.wait_closed()


async def consumer(pool):
    # session 复用
    async with aiohttp.ClientSession() as session:
        while not stopping:
            # 全局列表必须处理是否为空
            if not len(waiting_urls):
                await asyncio.sleep(0.5)
                continue
            url = waiting_urls.pop()
            print(f"start get url: {url}")
            if re.match("http://.*?jobbole.com/\d+/", url):
                if url not in seen_urls:
                    asyncio.ensure_future(article_handle(url, session, pool))
                    await asyncio.sleep(0.5)
            else:
                if url not in seen_urls:
                    asyncio.ensure_future(init_urls(url, session))

async def main(loop):
    pool = await aiomysql.create_pool(host="127.0.0.1", port=3307, user="root", password="usbw", db="mysql", loop=loop, charset="utf8", autocommit=True)
    async with aiohttp.ClientSession() as session:
        html = await fetch(start_url, session)
        seen_urls.add(start_url)
        extract_urls(html)
    asyncio.ensure_future(consumer(pool))


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    asyncio.ensure_future(main(loop))
    loop.run_forever()
