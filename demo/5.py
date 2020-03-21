def gen_func():
    html=yield 'ggggg'
    print(html)
    yield 2

if __name__=="__main__":
    gen=gen_func()
    url = next(gen)
    print(url)
    gen.send('hhh')

    pass