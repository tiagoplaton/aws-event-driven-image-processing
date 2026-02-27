# Design Decisions

## Why Event-Driven Architecture?

Event-driven architectures improve scalability and decouple services, allowing each component to scale independently.

## Why Use Amazon SQS?

Using SQS between S3 and Lambda provides:

- Message durability
- Traffic spike buffering
- Retry control
- Dead-letter queue support

Without SQS, direct S3-to-Lambda integration may increase failure coupling.

## Failure Handling Strategy

If a message fails processing multiple times, it can be redirected to a Dead Letter Queue (DLQ) for further inspection.

This prevents infinite retry loops and improves system observability.

## Trade-offs

- Slightly increased architecture complexity
- Additional service configuration
- Small added latency due to asynchronous flow
