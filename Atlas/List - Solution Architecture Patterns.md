
# What are Design Patterns?

Design patterns are reusable solutions to commonly occurring problems in software design. They provide generalised templates and best practices for designing parts of a system, facilitating reusable and maintainable code.

As noted by the "Gang of Four" who popularised design patterns:

"Each pattern describes a problem which occurs over and over again in our environment, and then describes the core of the solution to that problem, in such a way that you can use this solution a million times over, without ever doing it the same way twice." [Design Patterns: Elements of Reusable Object-Oriented Software](https://www.amazon.com/Design-Patterns-Elements-Reusable-Object-Oriented/dp/0201633612)

# Best Practices for Using Design Patterns

Here are some best practices when applying design patterns:

- **Identify recurring problems** - Look for general problems that come up again and again in your system and could benefit from a pattern. [Design Patterns](https://sourcemaking.com/design-patterns)
- **Study applicability** - Research the pattern thoroughly to understand its intent, applicability, and implementation. [Refactoring Guru](https://refactoring.guru/design-patterns)
- **Start simple** - Begin by applying simple creational and structural patterns like factory or decorator. [Microsoft Docs on Azure Architecture Patterns](https://docs.microsoft.com/en-us/azure/architecture/patterns/)
- **Combine patterns** - Many patterns are complementary and can be used together. For example, combining strategy, state, and command patterns. [Head First Design Patterns](https://www.amazon.com/Head-First-Design-Patterns-Brain-Friendly/dp/0596007124)
- **Favour composition** - Compose functionality with patterns like decorator and strategy rather than hard-coding behaviour. [Refactoring Guru on Decorator Pattern](https://refactoring.guru/design-patterns/decorator)
- **Program to interfaces** - Use interfaces to provide flexibility when implementing patterns. [Design Patterns: Elements of Reusable Object-Oriented Software](https://www.amazon.com/Design-Patterns-Elements-Reusable-Object-Oriented/dp/0201633612)
- **Keep improving** - Refactor implementations and iterate as you learn more about applying patterns well. [Learning Python Design Patterns](https://www.packtpub.com/product/learning-python-design-patterns-second-edition/9781788993811)

## Architectural Patterns

#pattern/architectural/layered

- [Layered Architecture](https://docs.microsoft.com/en-us/azure/architecture/guide/architecture-styles/layered-architecture) - Microsoft Docs. Describes splitting an app into layers like presentation, business, and data access.

- [N-Tier Architecture style](https://docs.microsoft.com/en-us/azure/architecture/guide/architecture-styles/n-tier) - Microsoft Docs. Expands on layered architecture by physically separating components.

#pattern/architectural/hexagonal 

- [Ports-and-adapters architecture](https://herbertograca.com/2017/09/21/ports-adapters-architecture/) - Herberto Graca. Focuses on decoupling application core from outside concerns.

- [Hexagonal Architecture](https://alistair.cockburn.us/hexagonal-architecture/) - Alistair Cockburn. Original introduction of ports and adapters concept.

#pattern/architectural/microkernel

- [Microkernel Architecture](https://microservices.io/patterns/microkernel.html) - Microservices.io. Core services in a microkernel with other services as plugins. 

- [Microkernel Pattern](https://docs.microsoft.com/en-us/azure/architecture/patterns/microkernel) - Microsoft Docs. Similar to above, promotes extensibility.

## Communication Patterns

#pattern/communication/publisher-subscriber

- [Publisher-Subscriber](https://docs.microsoft.com/en-us/azure/architecture/patterns/publisher-subscriber) - Microsoft Docs. Components publish events that other components can subscribe to.

- [Publish-Subscribe Pattern](https://www.enterpriseintegrationpatterns.com/patterns/messaging/PublishSubscribeChannel.html) - Gregor Hohpe. Explains pub-sub for enterprise integration.

#pattern/communication/request-response

- [Request-Reply Pattern](https://www.enterpriseintegrationpatterns.com/patterns/messaging/RequestReply.html) - Gregor Hohpe. One component requests info and another replies.

- [Request-Response Message Exchange](https://camel.apache.org/manual/latest/request-reply.html) - Apache Camel. Outlines request-response messaging.

## Deployment Patterns 

#pattern/deployment/monolithic

- [Monolithic architecture style](https://docs.microsoft.com/en-us/azure/architecture/guide/architecture-styles/monolithic) - Microsoft Docs. Entire app runs as a single process on one server.

#pattern/deployment/microservices

- [Microservices architecture style](https://docs.microsoft.com/en-us/azure/architecture/guide/architecture-styles/microservices) - Microsoft Docs. App is split into independently deployable services.

- [Microservices](https://martinfowler.com/articles/microservices.html) - Martin Fowler. Seminal article introducing the microservices concept.

#pattern/deployment/serverless

- [Serverless architectures](https://docs.microsoft.com/en-us/azure/architecture/patterns/serverless) - Microsoft Docs. Components are event-driven and resources managed by cloud provider.

- [Serverless Architectures](https://martinfowler.com/articles/serverless.html) - Mike Roberts. Discusses pros/cons and scenarios for serverless.

## Scalability Patterns

#pattern/scalability/horizontal-scaling

- [Horizontal scaling](https://docs.microsoft.com/en-us/azure/architecture/patterns/horizontal-scaling) - Microsoft Docs. Increase capacity by adding instances. 

#pattern/scalability/vertical-scaling

- [Vertical scaling](https://docs.microsoft.com/en-us/azure/architecture/patterns/vertical-scaling) - Microsoft Docs. Increase capacity by adding resources to existing instances.

#pattern/scalability/caching 

- [Cache-aside pattern](https://docs.microsoft.com/en-us/azure/architecture/patterns/cache-aside) - Microsoft Docs. Store frequently accessed data in a cache.

- [Caching](https://docs.microsoft.com/en-us/azure/architecture/best-practices/caching) - Microsoft Docs. Caching overview and best practices.

## Resiliency Patterns  

#pattern/resiliency/circuit-breaker

- [Circuit Breaker pattern](https://docs.microsoft.com/en-us/azure/architecture/patterns/circuit-breaker) - Microsoft Docs. Stops calls to unhealthy components. 

- [Circuit Breaker](https://martinfowler.com/bliki/CircuitBreaker.html) - Martin Fowler. Managing failure scenarios with circuit breakers.

#pattern/resiliency/replication 

- [Replication pattern](https://docs.microsoft.com/en-us/azure/architecture/patterns/replication) - Microsoft Docs. Keep redundant copies of data/components.

- [Database Replication](https://docs.microsoft.com/en-us/sql/relational-databases/replication/sql-server-replication?view=sql-server-ver16) - Microsoft Docs. Replicating SQL Server databases.  

#pattern/resiliency/failover

- [Failover pattern](https://docs.microsoft.com/en-us/azure/architecture/patterns/failover) - Microsoft Docs. Reroute to redundant component if failure occurs.

## Data Patterns

#pattern/data/repository

- [Repository Pattern](https://docs.microsoft.com/en-us/dotnet/architecture/microservices/microservice-ddd-cqrs-patterns/repository-pattern) - Microsoft Docs. Mediates between domain and data mapping.

- [Repository pattern](https://martinfowler.com/eaaCatalog/repository.html) - Martin Fowler. Original repository pattern concept.

#pattern/data/cqrs

- [CQRS pattern](https://docs.microsoft.com/en-us/azure/architecture/patterns/cqrs) - Microsoft Docs. Separate read and write responsibilities. 

- [CQRS](https://martinfowler.com/bliki/CQRS.html) - Martin Fowler. Introducing CQRS pattern.

## Security Patterns

#pattern/security/authentication-authorization

- [Authentication vs authorization](https://docs.microsoft.com/en-us/azure/security/fundamentals/authentication-vs-authorization) - Microsoft Docs. Explains the difference.

#pattern/security/firewall 

- [Firewall pattern](https://docs.microsoft.com/en-us/azure/architecture/patterns/firewall) - Microsoft Docs. Filters incoming/outgoing network traffic.

#pattern/security/proxy

- [Proxy pattern](https://refactoring.guru/design-patterns/proxy) - Refactoring Guru. Intermediary for requests that can add security. 

- [Proxy pattern](https://docs.microsoft.com/en-us/azure/architecture/patterns/proxy) - Microsoft Docs. As above.

## Integration Patterns 

#pattern/integration/adapter

- [Adapter pattern](https://refactoring.guru/design-patterns/adapter) - Refactoring Guru. Converts interface of a class into one clients expect.

- [Adapter pattern](https://docs.microsoft.com/en-us/azure/architecture/patterns/adapter) - Microsoft Docs. As above.

#pattern/integration/facade 

- [Facade pattern](https://refactoring.guru/design-patterns/facade) - Refactoring Guru. Simplified interface to subsystem.

- [Facade pattern](https://docs.microsoft.com/en-us/azure/architecture/patterns/facade) - Microsoft Docs. As above. 

#pattern/integration/bridge

- [Bridge pattern](https://refactoring.guru/design-patterns/bridge) - Refactoring Guru. Decouples abstraction from implementation.

- [Bridge pattern](https://docs.microsoft.com/en-us/azure/architecture/patterns/bridge) - Microsoft Docs. As above.

Let me know if you would like me to modify anything in the combined list.