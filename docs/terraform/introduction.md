# Infrastructure as Code (IaC) with Terraform

A simple crash course to start an EC2 instance, update it, and then destroy it.

## Introduction

- **Infrastructure as Code (IaC)** tools manage infrastructure using configuration files instead of GUIs.
- Enable building, changing, and managing infrastructure in a safe, consistent, and repeatable manner.
- Allow defining resource configurations that can be versioned, reused, and shared.

## Why Terraform?

- **Multi-Platform Management:** Manage infrastructure across multiple cloud platforms.
- **Human-Readable Configuration Language:** Quickly write infrastructure code.
- **State Management:** Track resource changes throughout deployments.
- **Version Control Integration:** Collaborate safely on infrastructure through version control systems.

## Terraform Providers

- **Providers:** Plugins that interact with cloud platforms and services via APIs.
- Over **1,000 providers** are available for AWS, Azure, GCP, Kubernetes, GitHub, Splunk, DataDog, and more.
- Providers can be found in the [Terraform Registry](https://registry.terraform.io/).
- If a specific provider is not available, custom providers can be created.

## Key Concepts

- **Resources:** Individual units of infrastructure, like compute instances or networks.
- **Modules:** Reusable Terraform configurations composed of resources from different providers.
- **Declarative Configuration Language:** Describe the desired end-state of infrastructure.
- **Automatic Dependency Management:** Calculate dependencies to create/destroy resources in the correct order.

## Terraform Workflow

1. **Scope:** Identify the required infrastructure for your project.
2. **Author:** Write the configuration for your infrastructure.
3. **Initialize:** Install necessary plugins for infrastructure management.
4. **Plan:** Preview changes Terraform will make.
5. **Apply:** Execute changes to match the desired infrastructure state.

## Tracking Your Infrastructure

- **State File:** Acts as the source of truth for your environment.
- Terraform uses the state file to determine changes needed to match your configuration.

## Collaboration with Terraform

- **Remote State Backends:** Securely share your state with teammates.
- Prevent race conditions when multiple people make changes simultaneously.
- Connect HCP Terraform to version control systems (VCSs) like GitHub, GitLab, etc.
- Automatically propose infrastructure changes when committing configuration changes to VCS.
- Manage infrastructure changes through version control, similar to application code.

## Example Code

```hcl
# Configure the AWS Provider
provider "aws" {
  region = "us-west-2"
}

# Create an EC2 Instance
resource "aws_instance" "example" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"

  tags = {
    Name = "example-instance"
  }
}
```