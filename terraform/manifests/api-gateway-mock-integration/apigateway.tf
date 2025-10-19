resource "aws_api_gateway_rest_api" "api_gateway" {
  name        = format("%s-api-gateway", var.prefix)
  description = "My API Gateway"
  endpoint_configuration {
    types = ["REGIONAL"]
  }
  tags = {
    Name = format("%s-api-gateway", var.prefix)
  }
}

resource "aws_api_gateway_resource" "root" {
  rest_api_id = aws_api_gateway_rest_api.api_gateway.id
  parent_id   = aws_api_gateway_rest_api.api_gateway.root_resource_id
  path_part   = "users"
}

resource "aws_api_gateway_method" "proxy" {
  rest_api_id   = aws_api_gateway_rest_api.api_gateway.id
  resource_id   = aws_api_gateway_resource.root.id
  http_method   = "GET"
  authorization = "NONE"
  request_models = {
    "application/json" = "Empty"
  }
}

resource "aws_api_gateway_integration" "lambda_integration" {
  rest_api_id             = aws_api_gateway_rest_api.api_gateway.id
  resource_id             = aws_api_gateway_resource.root.id
  http_method             = aws_api_gateway_method.proxy.http_method
  integration_http_method = "GET"
  type                    = "MOCK"
  request_templates = {
    "application/json" = jsonencode({
      statusCode = 200
    })
  }
}

resource "aws_api_gateway_method_response" "proxy" {
  rest_api_id = aws_api_gateway_rest_api.api_gateway.id
  resource_id = aws_api_gateway_resource.root.id
  http_method = aws_api_gateway_method.proxy.http_method
  status_code = 200

  response_models = {
    "application/json" = "Empty"
  }

  response_parameters = {
    "method.response.header.Content-Type" = true
  }
}

resource "aws_api_gateway_integration_response" "proxy" {
  rest_api_id = aws_api_gateway_rest_api.api_gateway.id
  resource_id = aws_api_gateway_resource.root.id
  http_method = aws_api_gateway_method.proxy.http_method
  status_code = aws_api_gateway_method_response.proxy.status_code
  response_templates = {
    "application/json" = jsonencode({

    })
  }
  response_parameters = {
    "method.response.header.Content-Type" = "'application/json'"
  }

  depends_on = [
    aws_api_gateway_method.proxy,
    aws_api_gateway_integration.lambda_integration
  ]
}

resource "aws_api_gateway_deployment" "deployment" {
  rest_api_id = aws_api_gateway_rest_api.api_gateway.id
  triggers = {
    redeploy = sha256(jsonencode({
      gateway_method       = aws_api_gateway_method.proxy.id,
      lambda_integration   = aws_api_gateway_integration.lambda_integration.id,
      method_response      = aws_api_gateway_method_response.proxy.id,
      integration_response = aws_api_gateway_integration_response.proxy.id,
      resource             = aws_api_gateway_resource.root.id,
      rest_api             = aws_api_gateway_rest_api.api_gateway.id
    }))
  }
  depends_on = [
    aws_api_gateway_integration.lambda_integration,
  ]
}

resource "aws_api_gateway_stage" "dev" {
  stage_name    = "dev"
  rest_api_id   = aws_api_gateway_rest_api.api_gateway.id
  deployment_id = aws_api_gateway_deployment.deployment.id
}
