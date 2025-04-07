
## Fundamentals of AWS Cloud Computing

This video explains the basics of AWS cloud computing and how different AWS services are used together to build real-world applications. The video is divided into 6 key parts:

### 1. Static Content Hosting & Delivery

*   **S3 (Simple Storage Service):**
    *   S3 is the storage location for all website files, including images, HTML, JavaScript, and CSS.
    *   It is highly reliable and can handle files of any size.
    *   S3 organizes files into buckets, which act as root folders for websites.
*   **CloudFront:**
    *   CloudFront is AWS's Content Delivery Network (CDN).
    *   It copies website files to data centers globally (Edge locations) for fast user access, regardless of location.
    *   CloudFront enhances security with features like signed URLs and cookies for content access control.
    *   It integrates with AWS WAF (Web Application Firewall) to protect websites from cyber attacks.
*   **Route 53:**
    *   Route 53 is AWS's DNS service.
    *   It translates website domain names into IP addresses.
    *   It directs users to the nearest or fastest server location.
    *   It can split traffic for testing new website versions.

### 2. Backend Services / Compute Layer

*   **Serverless with API Gateway & Lambda:**
    *   API Gateway receives requests and routes them to appropriate Lambda functions.
    *   Lambda functions execute code in response to triggers.
    *   Lambda is serverless, meaning AWS manages the underlying servers.
    *   Serverless is ideal for unpredictable workloads and specific tasks.
    *   It scales automatically and charges only for compute time used.
*   **EC2 (Elastic Cloud Compute):**
    *   EC2 provides virtual servers in AWS data centers.
    *   It offers complete control over the server environment, including OS, software, and security.
    *   EC2 is scalable, allowing users to adjust server capacity as needed.
    *   It suits applications needing specific configurations or legacy software.
*   **Containers with ECS (Elastic Container Service):**
    *   ECS manages containers, which package applications and their dependencies.
    *   Containers ensure consistent performance across different environments.
    *   ECS is ideal for microservices architectures.
    *   It allows independent scaling and updates of application components.
    *   It balances serverless and EC2, offering more control than Lambda but less management than EC2.
*   **Elastic Kubernetes Service (EKS):**
    *   Managed service for running Kubernetes on AWS without needing to install and operate your own Kubernetes control plane.
*   **AWS Fargate:**
    *   Serverless compute engine for containers, allowing users to run containers without managing servers.
*   **Lightsail:**
    *   Easiest way to get started with AWS for small-scale applications, offering virtual servers, storage, and networking.
*   **Batch:**
    *   Fully managed service for running batch computing workloads of any scale.

### 3. Data Storage & Management

*   **S3 (Object Storage):**
    *   S3 is object storage, suitable for files like images, videos, and documents.
    *   Files are stored as complete objects and accessed via URLs.
    *   It is best for infrequently modified, complete files.
*   **RDS (Relational Database Service):**
    *   RDS is for traditional SQL databases.
    *   It automatically manages tasks like backups, security, and scaling.
    *   It is suitable for structured data with clear relationships.
    *   Example: e-commerce applications managing orders, customers, and products.
*   **DynamoDB (NoSQL Database):**
    *   DynamoDB is a NoSQL database designed for speed and scalability.
    *   It handles large data volumes with millisecond responses.
    *   It is flexible and best for data that doesn't fit into tables or needs fast access.
    *   Example: tracking delivery driver locations.
*   **EBS (Elastic Block Store):**
    *   Provides persistent block storage volumes for use with Amazon EC2 instances.
*   **EFS (Elastic File System):**
    *   Provides scalable file storage for use with Amazon EC2.
*   **Glacier:**
    *   Secure, durable, and extremely low-cost cloud storage service for data archiving and long-term backup.

### 4. AI and Machine Learning

*   **Amazon Bedrock:**
    *   Bedrock offers pre-built AI models.
    *   It allows easy integration of advanced AI capabilities without building models from scratch.
    *   Useful for quickly adding chatbots or other AI features.
    *   Offers customization and security.
*   **Amazon SageMaker:**
    *   SageMaker is a comprehensive platform for building, training, and deploying custom machine learning models.
    *   It is ideal for complex tasks like predicting user behavior or fraud detection.
    *   Offers full control over AI development.

### 5. Security

*   **VPC (Virtual Private Cloud):**
    *   VPC is a private network within AWS.
    *   It allows control over network configurations, subnets, and internet access.
    *   It uses public subnets for internet-facing resources.
    *   It uses private subnets for internal resources.
    *   NAT Gateways provide secure internet access from private subnets.
*   **IAM (Identity and Access Management):**
    *   IAM controls access to AWS resources.
    *   It ensures users and services have only necessary permissions.
    *   It enables granular permission settings for services like Lambda and EC2.
    *   Crucial for securing AI and machine learning workloads.
*   **Security Tools:**
    *   AWS provides additional security services.
    *   GuardDuty for threat detection.
    *   KMS for encryption key management.
    *   AWS Shield and WAF for cyber attack protection.
*   **Secrets Manager:**
    *   Protects access to applications, services, and IT resources without the upfront investment and on-going maintenance costs of operating your own infrastructure.
*   **AWS CDK (Cloud Development Kit):**
    *   Open-source software development framework to define your cloud application resources using familiar programming languages.
*   **Config:**
    *   Provides AWS resource inventory, configuration history, and configuration change notifications to enable security and governance.

### 6. Monitoring and Auditing

*   **CloudWatch:**
    *   CloudWatch monitors AWS services and applications.
    *   It collects performance metrics, logs, and events.
    *   It provides dashboards and alerts for real-time insights into application performance.
    *   It can automate responses to issues.
*   **CloudTrail:**
    *   CloudTrail records API calls within the AWS account.
    *   It logs all changes made to the AWS environment.
    *   Essential for auditing and security.
    *   Tracks who made changes, when, and what was changed.
    *   Especially important in AI and machine learning for tracking model performance and access.
*   **X-Ray:**
    *   Helps developers analyze and debug production, distributed applications, such as those built using a microservices architecture.

### Networking Services

Networking services facilitate communication between resources and manage traffic.

*   **VPC (Virtual Private Cloud):**
    *   A VPC is a virtual private cloud that isolates your resources from other resources in the AWS cloud. It allows you to launch AWS resources into a virtual network that you've defined.
*   **Subnets:**
    *   A subnet is a range of IP addresses within a VPC. You can create public and private subnets. Public subnets have access to the internet, while private subnets do not.
*   **Security Group:**
    *   A security group acts as a virtual firewall that controls the traffic to and from your EC2 instances. You can specify rules to allow or deny traffic based on IP addresses, protocols, and ports.
*   **Internet Gateway:**
    *   An internet gateway connects your VPC to the internet. It allows communication between instances in your VPC and the internet.
*   **Route Table:**
    *   A route table determines how traffic flows within a VPC. You can create custom route tables for your subnets to control the routing of traffic.
*   **NAT Gateway:**
    *   A NAT Gateway in AWS is a managed Network Address Translation service that allows instances in private subnets to access the internet while preventing external services from initiating connections to those instances.
*   **NACL (Network ACL):**
    *   A Network ACL is a virtual firewall that controls traffic to and from your subnets. It provides an additional layer of security at the subnet level.
*   **Load Balancer:**
    *   A load balancer distributes incoming application traffic across multiple targets, such as EC2 instances, to ensure high availability and reliability.
*   **Direct Connect:**
    *   Direct Connect provides a dedicated network connection from your premises to AWS. It allows you to establish a private connection between AWS and your data center, office, or colocation environment.
*   **Transit Gateway:**
    *   Transit Gateway enables customers to connect their VPCs and their on-premises networks to a single gateway. It simplifies network architecture and reduces the complexity of managing multiple connections.

### Messaging Services

These services enable communication between distributed systems or components.

*   **SQS (Simple Queue Service):**
    *   SQS is a fully managed message queuing service that enables decoupling of microservices, distributed systems, and serverless applications. It allows you to send, store, and receive messages between software components.
*   **SNS (Simple Notification Service):**
    *   SNS is a managed messaging service for sending notifications from the cloud to subscribers or other applications. It supports multiple messaging protocols, including HTTP/HTTPS, email, SMS, and AWS Lambda.
*   **MQ:**
    *   MQ is a managed message broker service for Apache ActiveMQ and RabbitMQ that makes it easy to set up and operate message brokers in the cloud. It enables communication between distributed applications and microservices.

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


