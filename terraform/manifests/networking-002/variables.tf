variable "prefix" {
  type        = string
  description = "A prefix used to name all the resources created by this configuration."
}

variable "region" {
  type        = string
  description = "The AWS region where the infrastructure will be deployed."
}


variable "vpc_cidr" {
  type        = string
  description = "CIDR block for the VPC."
  default     = "10.0.0.0/16"
}

variable "availability_zone_1" {
  type        = string
  description = "The availability zone to use for the subnet."
  default     = "us-east-1a"
}
variable "public_subnet_cidr" {
  type        = string
  description = "CIDR block for the public subnet."
  default     = "10.0.0.0/24"
}
variable "private_subnet_cidr" {
  type        = string
  description = "CIDR block for the private subnet."
  default     = "10.0.1.0/24"
}



variable "ami" {
  description = "AMI ID for the EC2 instance"
  type        = string
  default     = "ami-0f1dcc636b69a6438"
}

variable "instance_type" {
  description = "Instance type for the EC2 instance"
  type        = string
  default     = "t2.micro"
}

variable "ssh_key_name" {
  description = "Name of the SSH key pair to use for the EC2 instance"
  type        = string
}
