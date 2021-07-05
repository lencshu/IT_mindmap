1) Why TDD is a good/bad methodology for software development (3 reason)

TDD means that we write and run a set of tests before the code
pros:
1. programming from the point of view of the users instead of coding directly, which can help us find more hidden conditions
2. force us to decouple the software
3. easier to do code refactoring without worrying about getting some fatal errors which are hard to find
cons:
1. It slows down development initially due to spending time writing tests first.
2. The tests may be hard to write if we talk about the quality of the test
3. Test is not the purpose. Sometimes we can be distracted by fancy features in the testing framework

2) 10 best practices that you apply for API Design

1. Provides a good mental model. The api is not only between the client and the server, but should be easy to understand for the different programmers: designer, maintainer and api user. The api should be understandable, debuggable, testable, extensible and maintainable.
2. Make things as simple as possible but not oversimplify. Do not combine models in an unnecessary way.
3. Allows multiple implementations. For the same type of data, we can use different endpoints to access a different service.
4. Solid API documentation
5. Carefully define the "resource" of the API. Resource is an abstraction of the object to deal with. Abstraction is a process of getting rid of details.
6. Choose the right level of abstraction like view level, logical level and physical level.
7. Define the Conceptually meaningful operations on this resource.
8. Compatibility. Apply a deprecation process if a non-compatible change is necessary
9. Be aware of the risks in full replacement. Better use an update mask to specify which member should be updated
10. Don't create your own error codes or error mechanisms. Better use the standard error code.

3) How you deal with API versioning
 

There are 2 main ways to do API versioning that I prefer according to the context:
1. Versioning through URI Path. Simple one, easy to apply a deprecation process when versioning
2. Versioning through custom headers. It doesn’t clutter the URI with versioning information
 

4) When are UML sequence diagrams useful? If you can replace or remove this kind of diagram you will do it? By what ?
When thinking about the design or looking at the collaboration among the objects within a single use case. But UML is just a way of communicating. It is a tool of visual modeling. It is not that important if it is UML or not. DFD(data flow diagrams) or even Visio can do the work. But UML is a good way to express the ideas clearly.