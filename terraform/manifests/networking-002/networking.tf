resource "aws_vpc" "vpc_main" {
  cidr_block           = var.vpc_cidr
  enable_dns_hostnames = true
  tags = {
    Name = "${var.prefix}-vpc"
  }
}

resource "aws_internet_gateway" "internet_gateway_main" {
  vpc_id = aws_vpc.vpc_main.id
  tags = {
    Name = "${var.prefix}-internet-gateway"
  }
}


resource "aws_eip" "eip_main" {
  tags = {
    Name = "${var.prefix}-eip"
  }
}

resource "aws_nat_gateway" "nat_gateway_main" {
  allocation_id = aws_eip.eip_main.id
  subnet_id     = aws_subnet.subnet_public.id

  tags = {
    Name = "${var.prefix}-nat-gateway"
  }

  depends_on = [aws_internet_gateway.internet_gateway_main]
}