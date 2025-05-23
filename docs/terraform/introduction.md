# Infrastructure as Code (IaC) with Terraform

Simple crash course to start and EC2 instance, update it and then destroy it

## Introduction

- **Infrastructure as Code (IaC)** tools manage infrastructure using configuration files instead of GUIs.
- Allows for building, changing, and managing infrastructure in a safe, consistent, and repeatable manner.
- Enables defining resource configurations that can be versioned, reused, and shared.

## Why Terraform?

- **Multi-Platform Management:** Manages infrastructure across multiple cloud platforms.
- **Human-Readable Configuration Language:** Facilitates quick writing of infrastructure code.
- **State Management:** Tracks resource changes throughout deployments.
- **Version Control Integration:** Safe collaboration on infrastructure through version control systems.

## Terraform Providers

- **Providers:** Plugins that interact with cloud platforms and services via APIs.
- Over **1,000 providers** available for AWS, Azure, GCP, Kubernetes, GitHub, Splunk, DataDog, and more.
- Providers can be found in the [Terraform Registry](https://registry.terraform.io/).
- If a specific provider is not available, custom providers can be created.

## Key Concepts

- **Resources:** Individual units of infrastructure, like compute instances or networks.
- **Modules:** Reusable Terraform configurations composed of resources from different providers.
- **Declarative Configuration Language:** Describes the desired end-state of infrastructure.
- **Automatic Dependency Management:** Calculates dependencies to create/destroy resources in the correct order.

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

# Installation guide

### Upgrade Terraform (Homebrew)
```bash
brew upgrade hashicorp/tap/terraform
```

### Install Terraform (Chocolatey)
```powershell
choco install terraform
```

## For Full Installation Guide
For detailed step-by-step instructions and platform-specific installation methods, please visit the official [Terraform Installation Guide](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli).

# Terraform CLI Installation - Quick Reference

## Important Commands

### Verify Installation
```bash
terraform -v

terraform -help

terraform -help plan
```

### Enable tab completion

If you use either Bash or Zsh, you can enable tab completion for Terraform commands. To enable autocomplete, first ensure that a config file exists for your chosen shell.
```sh
touch ~/.bashrc
touch ~/.zshrc
```

Then install the autocomplete package.
```sh
terraform -install-autocomplete
```

### Quick start tutorial

Now that you've installed Terraform, you can provision an NGINX server in less than a minute using Docker on Mac, Windows, or Linux. You can also follow the rest of this tutorial in your web browser.

Create a directory named `learn-terraform-docker-container`. <br>
This working directory houses the configuration files that you write to describe the infrastructure you want Terraform to create and manage. When you initialize and apply the configuration here, Terraform uses this directory to store required plugins, modules (pre-written configurations), and information about the real infrastructure it created. <br>
In the working directory, create a file called `main.tf` and paste the following Terraform configuration into it.

for MAC and linux
```hcl
terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
  }
}

provider "docker" {}

resource "docker_image" "nginx" {
  name         = "nginx"
  keep_locally = false
}

resource "docker_container" "nginx" {
  image = docker_image.nginx.image_id
  name  = "tutorial"

  ports {
    internal = 80
    external = 8000
  }
}
```

for Windows
```hcl
terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
  }
}

provider "docker" {
  host    = "npipe:////.//pipe//docker_engine"
}

resource "docker_image" "nginx" {
  name         = "nginx"
  keep_locally = false
}

resource "docker_container" "nginx" {
  image = docker_image.nginx.image_id
  name  = "tutorial"

  ports {
    internal = 80
    external = 8000
  }
}
```

Initialize the project, which downloads a plugin called a provider that lets Terraform interact with Docker.
```bash
terraform init
```

Provision the `NGINX` server container with `apply`. When Terraform asks you to confirm type yes and press ENTER.
```bash
terraform apply
```

Verify the existence of the NGINX container by visiting `localhost:8000` in your web browser or running `docker ps` to see the container.

To stop the container, run `terraform destroy`.

# Working with AWS

We will provision an `EC2` instance on `Amazon Web Services (AWS)`. `EC2` instances are virtual machines running on `AWS`, and a common component of many infrastructure projects.

### Prerequisites

**To follow this tutorial you will need**

- The Terraform CLI (1.2.0+) installed.
- The AWS CLI installed.
- AWS account and associated credentials that allow you to create resources.

To use your IAM credentials to authenticate the Terraform AWS provider, set the `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` environment variable.
```sh
export AWS_ACCESS_KEY_ID=
export AWS_SECRET_ACCESS_KEY=
```

> Tip : If you don't have access to IAM user credentials, use another authentication method described in the [AWS provider documentation](https://registry.terraform.io/providers/hashicorp/aws/latest/docs?product_intent=terraform#environment-variables).

## Build Infrastructure

### Write configuration

Create a directory for your configuration. Configuration files must be in this directory for Terraform to run them.

```sh
mkdir learn-terraform-aws-instance
cd learn-terraform-aws-instance
```

Create a file named `main.tf` and paste the following configuration into it.

```hcl
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"
    }
  }

  required_version = ">= 1.2.0"
}

provider "aws" {
  region  = "ap-south-1"
}

resource "aws_instance" "app_server" {
  ami           = "ami-830c94e3"
  instance_type = "t2.micro"

  tags = {
    Name = "ExampleAppServerInstance"
  }
}
```

### Terraform Block
The `terraform {}` block contains Terraform settings, including the required providers Terraform will use to provision your infrastructure. For each provider, the source attribute defines an optional hostname, a namespace, and the provider type. Terraform installs providers from the [Terraform Registry](https://registry.terraform.io/?product_intent=terraform) by default. In this example configuration, the aws provider's source is defined as `hashicorp/aws`, which is shorthand for `registry.terraform.io/hashicorp/aws`.

You can also set a version constraint for each provider defined in the required_providers block. The version attribute is optional, but we recommend using it to constrain the provider version so that Terraform does not install a version of the provider that does not work with your configuration. If you do not specify a provider version, Terraform will automatically download the most recent version during initialization.

To learn more, reference the provider source documentation.

### Initialize the directory

Initialize the configuration directory. This step downloads the necessary provider plugins for the configuration.

```sh
terraform init
```


```sh
terraform fmt
```

```sh
terraform plan

## We can additionally give variable value
terraform plan -var-file="dev.tfvars"
```

### Apply configuration

Apply the configuration to create your instance.

```sh
terraform apply

## We can additionally give variable value
terraform apply -var-file="dev.tfvars"
```


```bash
terraform show
```

When prompted to confirm, type `yes` and press ENTER.

### Verify the instance

Verify that your instance is running.

```sh
aws ec2 describe-instances --filters "Name=instance-state-name,Values=running"
```

### Clean up your infrastructure

Destroy the instance to avoid ongoing charges.

```sh
terraform destroy

## We can additionally give variable value
terraform destroy -var-file="dev.tfvars"

## 
terraform destroy --auto-approve -var-file="dev.tfvars"
```

When prompted to confirm, type `yes` and press ENTER.






## Content

- [ec2](./manifests/ec2/)
- [variables](./manifests/variables/)
- [networking 001](./manifests/networking-001/)
- [networking 002](./manifests/networking-002/)
- [networking 003](./manifests/networking-003/)