
# first availability zone

resource "aws_subnet" "public_subnet_1" {
  vpc_id            = aws_vpc.vpc_main.id
  cidr_block        = var.public_subnet1_cidr
  availability_zone = var.availability_zone_1

  tags = {
    Name = format("%s-public-subnet-1", var.prefix)
  }
}

resource "aws_subnet" "private_subnet_1" {
  vpc_id            = aws_vpc.vpc_main.id
  cidr_block        = var.private_subnet1_cidr
  availability_zone = var.availability_zone_1

  tags = {
    Name = format("%s-private-subnet-1", var.prefix)
  }
}

resource "aws_subnet" "secure_subnet_1" {
  vpc_id            = aws_vpc.vpc_main.id
  cidr_block        = var.secure_subnet1_cidr
  availability_zone = var.availability_zone_1

  tags = {
    Name = format("%s-secure-subnet-1", var.prefix)
  }
}



# second availability zone


resource "aws_subnet" "public_subnet_2" {
  vpc_id            = aws_vpc.vpc_main.id
  cidr_block        = var.public_subnet2_cidr
  availability_zone = var.availability_zone_2

  tags = {
    Name = format("%s-public-subnet-2", var.prefix)
  }
}

resource "aws_subnet" "private_subnet_2" {
  vpc_id            = aws_vpc.vpc_main.id
  cidr_block        = var.private_subnet2_cidr
  availability_zone = var.availability_zone_2

  tags = {
    Name = format("%s-private-subnet-2", var.prefix)
  }
}


resource "aws_subnet" "secure_subnet_2" {
  vpc_id            = aws_vpc.vpc_main.id
  cidr_block        = var.secure_subnet2_cidr
  availability_zone = var.availability_zone_2

  tags = {
    Name = format("%s-secure-subnet-2", var.prefix)
  }
}
