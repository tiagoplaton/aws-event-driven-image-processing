# AWS Event-Driven Image Processing Architecture

## Project Overview

This project demonstrates a serverless event-driven architecture on AWS designed to process image uploads in a scalable and resilient way.

Instead of processing images synchronously inside an application server, this solution introduces a decoupled architecture using managed AWS services.

---

## Architecture Components

- Amazon S3 – Object storage for uploaded images
- Amazon SQS – Message queue for decoupling and buffering
- AWS Lambda – Serverless compute for asynchronous processing
- Amazon CloudWatch – Monitoring and logging

---

## Architecture Flow

1. A user uploads an image to Amazon S3.
2. S3 generates an event notification.
3. The event is sent to Amazon SQS.
4. AWS Lambda consumes messages from SQS.
5. The image processing logic runs asynchronously.

---

## Design Goals

- Improve scalability during traffic spikes
- Prevent application overload
- Ensure message durability
- Reduce operational overhead
- Enable fault tolerance with retry mechanisms

---

## Why Use SQS Between S3 and Lambda?

Instead of triggering Lambda directly from S3, SQS provides:

- Buffering during high traffic
- Retry control
- Dead-letter queue support
- Better fault isolation
- Improved reliability

This follows event-driven architectural best practices.

---

## Reliability Features

- Asynchronous processing
- Automatic retries
- Decoupled services
- Designed for DLQ integration

---

## Cost Efficiency

This architecture is cost-effective because:

- Lambda follows a pay-per-execution model
- SQS charges per request
- S3 scales automatically based on usage

---

## Future Improvements

- Implement image resizing logic
- Add Dead Letter Queue configuration
- Introduce Infrastructure as Code (Terraform)
- Add monitoring alarms
