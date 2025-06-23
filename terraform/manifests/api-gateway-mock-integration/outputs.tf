output "region" {
  value       = var.region
  description = "value of the region variable"
}
output "api_gateway_id" {
  value = aws_api_gateway_rest_api.api_gateway.id
}