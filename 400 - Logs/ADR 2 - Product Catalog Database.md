Tags: #Example #Log/ADR 



### Status: Accepted

### Context:

We need to decide on the database technology for the Product Catalog component. We have several options to consider, including using a SQL database or a NoSQL database. We need to consider factors such as data complexity, scalability, performance, and ease of development.

### Decision:

We have decided to use a SQL database for the Product Catalog component. Specifically, we will use MySQL, which offers a mature and robust relational database system that can handle complex data structures and high volumes of data. MySQL also offers high performance and scalability, making it suitable for our needs.

### Consequences:

By using a SQL database for the Product Catalog component, we will need to invest in designing and maintaining a schema for the database. However, this will provide us with a reliable and scalable database system that can handle the needs of the ecommerce website.