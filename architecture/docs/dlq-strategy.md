# Dead Letter Queue (DLQ) Strategy

A Dead Letter Queue (DLQ) is used to capture messages that fail processing after multiple retry attempts.

## Why DLQ Matters

- Prevents message loss
- Avoids infinite retry loops
- Improves observability
- Enables manual or automated reprocessing

## Implementation Plan

1. Configure SQS Redrive Policy
2. Set maxReceiveCount (e.g., 3 attempts)
3. Redirect failed messages to DLQ
4. Monitor DLQ metrics via CloudWatch

This enhances reliability and aligns with distributed system best practices.
