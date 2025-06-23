# Your first terraform script

## Installation Guide
For detailed step-by-step instructions and platform-specific installation methods, please visit the official [Terraform Installation Guide](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli).


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

## Quick start tutorial

Now that you've installed Terraform, you can provision an NGINX server in less than a minute using Docker on Mac, Windows, or Linux. You can also follow the rest of this tutorial in your web browser.

Create a directory named `learn-terraform-docker-container`. <br>
This working directory houses the configuration files that you write to describe the infrastructure you want Terraform to create and manage. When you initialize and apply the configuration here, Terraform uses this directory to store required plugins, modules (pre-written configurations), and information about the real infrastructure it created. <br>
In the working directory, create a file called `main.tf` and paste the following Terraform configuration into it.

for MAC and linux
```zsh
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
```zsh
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



## Working with AWS

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

```zsh
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

checks whether your Terraform configuration files are syntactically valid and internally consistent. It does not check with the cloud provider or create any resources. It helps you catch errors or typos in your .tf files before running terraform plan or terraform apply.
```zsh
terraform validate
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

terraform apply --auto-approve -var-file="dev.tfvars"
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




```bash
terraform show

# terraform state show in json format
terraform show -json
```


```zsh
terraform providers

terraform providers mirror <another-directory>
```

```zsh
terraform output

terraform output <variable-name>
```


```zsh
terraform apply --refresh-only
```

Normally, `terraform plan` checks the actual resources in your cloud provider to update its state file before showing what changes it will make. With `--refresh=false`, it skips this check and uses only the existing state file, which can make the plan faster but may not reflect the current real-world infrastructure. This is useful if you want to avoid unnecessary API calls or if you know the state hasn't changed outside of Terraform.
```zsh
terraform plan --refresh=false
```


```zsh
# show in .svg format
terraform graph

terraform graph | dot -Tsvg > graph.svg
```


## Lifecycle rules

create_before_destroy


prevent_destroy


ignore_changes


