


Status: accepted
Date: 2023-07-01
deciders: [Alice, Bob]
consulted: [Chris, Dana]
informed: [Entire Dev Team]

---
# Database Selection - Project - eCommerce Example

## Context and Problem Statement

We are starting development on Project X and need to select an appropriate database. Should we go for a relational or NoSQL database?

## Decision Drivers

* Scalability
* Data integrity
* Query complexity
* Budget

## Considered Options

* MySQL
* MongoDB
* PostgreSQL

## Decision Outcome

Chosen option: "PostgreSQL", because it provides scalability, ensures data integrity, and supports complex queries.

### Consequences

* Good, because we have in-house expertise.
* Good, because PostgreSQL has a strong community and lots of support.
* Bad, because initial setup might be slightly more complex than MongoDB.

## Validation

To be validated by reviewing the initial setup and first two sprints' database-related tasks.

## Pros and Cons of the Options

### PostgreSQL

* Good, because of its ACID compliance.
* Good, because of its support for JSONB.
* Neutral, because it is relational, and we might need to adjust some schemas.
* Bad, because setup is a bit more involved than MongoDB.

### MongoDB

* Good, because of its scalability.
* Good, because of its schema-less nature.
* Neutral, because we would need to handle transactions carefully.
* Bad, because it's not ACID compliant out of the box.

