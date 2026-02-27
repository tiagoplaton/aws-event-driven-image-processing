# Architecture Diagram

## Logical Flow

User → Amazon S3 → Amazon SQS → AWS Lambda → CloudWatch
                                      ↓
                                   Dead Letter Queue

This project follows an event-driven pattern with decoupled services.

The introduction of Amazon SQS improves reliability, buffering and failure isolation.
