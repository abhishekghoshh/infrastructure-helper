## Official documentation

- [Hands-on Tutorials](https://aws.amazon.com/getting-started/hands-on)
- [Welcome to AWS Documentation](https://docs.aws.amazon.com/)



## AWS projects for learning

### Project 1: Deploy a Static Website
- **Description**: Learn how to deploy a static website using Amazon S3 and Amazon CloudFront.
- **Resources**: [AWS S3](https://aws.amazon.com/s3/), [AWS CloudFront](https://aws.amazon.com/cloudfront/), [AWS Certificate Manager](https://aws.amazon.com/certificate-manager/), [AWS WAF](https://aws.amazon.com/waf/), [AWS CloudWatch](https://aws.amazon.com/cloudwatch/)

### Project 2: Silent Scalper
- **Description**: Build a serverless application that monitors stock prices and sends notifications when certain conditions are met.
- **Resources**: [AWS S3](https://aws.amazon.com/s3/), [AWS Lambda](https://aws.amazon.com/lambda/), [DynamoDB](https://aws.amazon.com/dynamodb/), [API Gateway](https://aws.amazon.com/api-gateway/), [SNS](https://aws.amazon.com/sns/), [AWS CloudWatch](https://aws.amazon.com/cloudwatch/)

### Project 3: The Smart Vault
- **Description**: Create a secure storage solution for sensitive data with automated backup and monitoring.
- **Resources**: [EC2](https://aws.amazon.com/ec2/), [EBS](https://aws.amazon.com/ebs/), [EventBridge](https://aws.amazon.com/eventbridge/), [AWS Lambda](https://aws.amazon.com/lambda/), [SNS](https://aws.amazon.com/sns/), [AWS CloudWatch](https://aws.amazon.com/cloudwatch/)

### Project 4: AI Customer Service Bot
- **Description**: Develop an AI-powered chatbot for customer service that can handle common queries and escalate complex issues.
- **Resources**: [AWS S3](https://aws.amazon.com/s3/), [AWS Lambda](https://aws.amazon.com/lambda/), [SNS](https://aws.amazon.com/sns/), [Amazon Lex](https://aws.amazon.com/lex/), [Amazon Polly](https://aws.amazon.com/polly/)

### Project 5: Intelligent Document Engine
- **Description**: Build a document processing system that extracts information from documents and stores it in a searchable database.
- **Resources**: [AWS S3](https://aws.amazon.com/s3/), [Textract](https://aws.amazon.com/textract/), [SageMaker](https://aws.amazon.com/sagemaker/), [OpenSearch](https://aws.amazon.com/opensearch-service/), [DynamoDB](https://aws.amazon.com/dynamodb/), [MLOps](https://aws.amazon.com/mlops/)



## Aws core services

### Compute Services
These services provide the necessary resources for running applications and workloads in the cloud.

   - **AWS IAM**: Identity and Access Management service that allows you to manage user access and permissions securely.
   - **EC2 (Elastic Compute Cloud)**: Provides resizable compute capacity in the cloud, allowing users to run virtual servers.
   - **Elastic Kubernetes Service (EKS)**: Managed service for running Kubernetes on AWS without needing to install and operate your own Kubernetes control plane.
   - **Elastic Container Service (ECS)**: A highly scalable container orchestration service that supports Docker containers.
   - **AWS Fargate**: Serverless compute engine for containers, allowing users to run containers without managing servers.
   - **AWS Lambda**: Serverless computing service that runs code in response to events, automatically managing the compute resources.
   - **Lightsail**: Easiest way to get started with AWS for small-scale applications, offering virtual servers, storage, and networking.
   - **Batch**: Fully managed service for running batch computing workloads of any scale.

### Storage Services
These services are designed for storing data in various formats.

   - **S3 (Simple Storage Service)**: Object storage service that offers scalability, data availability, security, and performance.
   - **RDS (Relational Database Service)**: Managed relational database service supporting various database engines like MySQL, PostgreSQL, and Oracle.
   - **DynamoDB**: Fully managed NoSQL database service that provides fast and predictable performance with seamless scalability.
   - **EBS (Elastic Block Store)**: Provides persistent block storage volumes for use with Amazon EC2 instances.
   - **EFS (Elastic File System)**: Provides scalable file storage for use with Amazon EC2.
   - **Glacier**: Secure, durable, and extremely low-cost cloud storage service for data archiving and long-term backup.

### Networking Services
Networking services facilitate communication between resources and manage traffic.

   - **VPC**: A VPC is a virtual private cloud that isolates your resources from other resources in the AWS cloud.
   - **Subnets**: A subnet is a range of IP addresses within a VPC. You can create public and private subnets. Public subnets have access to the internet, while private subnets do not.
   - **Security group**: A security group is a virtual firewall that controls traffic to and from your EC2 instances.
   - **Internet Gateway**: A gateway connects your VPC to other networks. There are different types of gateways, such as internet gateways and NAT gateways.
   - **Route Table**: A route table determines how traffic flows within a VPC. You can create custom route tables for your subnets.
   - **NAT Gateway**: A NAT Gateway in AWS is a managed Network Address Translation service that allows instances in private subnets to access the internet while preventing external services from initiating connections to those instances.
   - **NACL**: An NACL is a virtual firewall that controls traffic to and from your subnets.
   - **Load Balancer**: Distributes incoming application traffic across multiple targets, such as EC2 instances.
   - **Route 53**: Scalable Domain Name System (DNS) web service designed to route end users to Internet applications.
   - **Amazon CloudFront**: Content Delivery Network (CDN) that securely delivers data, videos, applications, and APIs with low latency.
   - **API Gateway**: Managed service for creating, publishing, maintaining, monitoring, and securing APIs at any scale.
   - **Direct Connect**: Provides a dedicated network connection from your premises to AWS.
   - **Transit Gateway**: Enables customers to connect their VPCs and their on-premises networks to a single gateway.

### Messaging Services
These services enable communication between distributed systems or components.

   - **SQS (Simple Queue Service)**: Fully managed message queuing service that enables decoupling of microservices, distributed systems, and serverless applications.
   - **SNS (Simple Notification Service)**: Managed messaging service for sending notifications from the cloud to subscribers or other applications.
   - **MQ**: Managed message broker service for Apache ActiveMQ and RabbitMQ that makes it easy to set up and operate message brokers in the cloud.

### Security & Management Services
Services focused on governance, security, and resource management.

   - **Secrets Manager**: Protects access to applications, services, and IT resources without the upfront investment and on-going maintenance costs of operating your own infrastructure.
   - **AWS CDK (Cloud Development Kit)**: Open-source software development framework to define your cloud application resources using familiar programming languages.
   - **CloudTrail**: Enables governance, compliance, and operational and risk auditing of your AWS account.
   - **Config**: Provides AWS resource inventory, configuration history, and configuration change notifications to enable security and governance.

### Monitoring & Observability Services
These services provide insights into application performance and resource utilization.

   - **CloudWatch**: Monitoring service for AWS cloud resources and applications that provides data and actionable insights to monitor applications.
   - **X-Ray**: Helps developers analyze and debug production, distributed applications, such as those built using a microservices architecture.
   - **CloudTrail**: Enables governance, compliance, and operational and risk auditing of your AWS account.



## Watch this videos
- [The only Cloud services you actually need to know](https://www.youtube.com/watch?v=gcfB8iIPtbY)
- [AWS Networking Basics For Programmers | Hands On](https://www.youtube.com/watch?v=2doSoMN2xvI)
- [AWS Cloud Computing Course](https://www.youtube.com/playlist?list=PL0X6fGhFFNTcU-_MCPe9dkH6sqmgfhy_M)


## Udemy
- [Ultimate AWS Certified Cloud Practitioner CLF-C02](https://www.udemy.com/course/aws-certified-cloud-practitioner-new)
    - [6 Practice Exams | AWS Certified Cloud Practitioner CLF-C02](https://www.udemy.com/course/practice-exams-aws-certified-cloud-practitioner/?_gl=1*1asmfb2*_ga*MTYyODg0OTc2Ni4xNzM5NTU1MzE1*_ga_6GZZTGGX7H*MTczOTU1NTMxNC4xLjEuMTczOTU1NTQ3NC4zNi4wLjA.&couponCode=FEB_25_GET_STARTED)
- [Ultimate AWS Certified Developer Associate 2025 DVA-C02](https://udemy.com/course/aws-certified-developer-associate-dva-c01)
    - [Practice Exams | AWS Certified Developer Associate 2024](https://www.udemy.com/course/aws-certified-developer-associate-practice-tests-dva-c01/?_gl=1*1mu0o3w*_ga*MTYyODg0OTc2Ni4xNzM5NTU1MzE1*_ga_6GZZTGGX7H*MTczOTU1NTMxNC4xLjEuMTczOTU1NTgwOS42MC4wLjA.&couponCode=FEB_25_GET_STARTED)
- [AWS Certified Cloud Practitioner CLF-C02](https://www.udemy.com/course/practice-exams-aws-certified-cloud-practitioner)
    - [Practice Exams | AWS Certified Solutions Architect Associate](https://www.udemy.com/course/practice-exams-aws-certified-solutions-architect-associate/?_gl=1*1rnmkl5*_ga*MTYyODg0OTc2Ni4xNzM5NTU1MzE1*_ga_6GZZTGGX7H*MTczOTU1NTMxNC4xLjAuMTczOTU1NTMxNC42MC4wLjA.&couponCode=FEB_25_GET_STARTED)
