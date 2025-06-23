
resource "aws_subnet" "subnet_public" {
  vpc_id                  = aws_vpc.vpc_main.id
  cidr_block              = var.public_subnet_cidr
  map_public_ip_on_launch = true
  availability_zone       = var.availability_zone_1

  tags = {
    Name = "${var.prefix}-public-subnet"
  }
}

resource "aws_subnet" "subnet_private" {
  vpc_id                  = aws_vpc.vpc_main.id
  cidr_block              = var.private_subnet_cidr
  availability_zone       = var.availability_zone_1
  map_public_ip_on_launch = false

  tags = {
    Name = "${var.prefix}-private-subnet"
  }
}