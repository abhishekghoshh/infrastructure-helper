variable "instance_name" {
  description = "Value of the Name tag for the EC2 instance"
  type        = string
  default     = "ExampleAppServerInstance"
}

variable "ami" {
  description = "AMI ID for the EC2 instance"
  type        = string
  default     = "ami-0f88e80871fd81e91"
}

variable "instance_type" {
  description = "Instance type for the EC2 instance"
  type        = string
  default     = "t2.micro"
}


variable "prefix" {
  type        = string
  description = "A prefix used to name all the resources created by this configuration."
}

variable "region" {
  type        = string
  description = "The AWS region where the infrastructure will be deployed."
}