output "vpc_id" {
  description = "VPC ID"
  value       = aws_vpc.vpc_main.id
}