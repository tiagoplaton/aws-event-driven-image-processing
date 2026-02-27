# Architecture Diagram

## Logical Flow

User → Amazon S3 → Amazon SQS → AWS Lambda → CloudWatch
                                      ↓
                                   Dead Letter Queue

This project follows an event-driven pattern with decoupled services.

The introduction of Amazon SQS improves reliability, buffering and failure isolation.
---

## Architectural Trade-offs

While this architecture improves scalability and fault tolerance, it introduces:

- Additional service configuration
- Slight increase in latency due to asynchronous processing
- Higher architectural complexity compared to synchronous processing

However, the benefits in resilience and scalability outweigh these trade-offs.
