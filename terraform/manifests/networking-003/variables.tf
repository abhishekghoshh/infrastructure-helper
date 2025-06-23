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
  description = "The CIDR block for the VPC."
}



variable "availability_zone_1" {
  type        = string
  description = "The availability zone 1"
}

variable "public_subnet1_cidr" {
  type        = string
  description = "The CIDR block for subnet 1, typically used in availability zone 1."
}

variable "private_subnet1_cidr" {
  type        = string
  description = "The CIDR block for subnet 2, typically used in availability zone 2."
}

variable "secure_subnet1_cidr" {
  type        = string
  description = "The CIDR block for subnet 3, typically used in availability zone 3."
}


variable "availability_zone_2" {
  type        = string
  description = "The availability zone 1"
}

variable "public_subnet2_cidr" {
  type        = string
  description = "The CIDR block for subnet 1, typically used in availability zone 1."
}

variable "private_subnet2_cidr" {
  type        = string
  description = "The CIDR block for subnet 2, typically used in availability zone 2."
}

variable "secure_subnet2_cidr" {
  type        = string
  description = "The CIDR block for subnet 3, typically used in availability zone 3."
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
