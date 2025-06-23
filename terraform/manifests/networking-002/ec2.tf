
resource "aws_instance" "public_app_server" {
  ami                         = var.ami
  instance_type               = var.instance_type
  subnet_id                   = aws_subnet.subnet_public.id
  vpc_security_group_ids      = [aws_security_group.security_group_public.id]
  key_name                    = var.ssh_key_name
  associate_public_ip_address = true

  tags = {
    Name = "${var.prefix}-public-ec2-instance"
  }
}

resource "aws_instance" "abhishek_private_ec2" {
  ami                         = var.ami
  instance_type               = var.instance_type
  subnet_id                   = aws_subnet.subnet_private.id
  vpc_security_group_ids      = [aws_security_group.security_group_private.id] # Reuse the existing SG
  key_name                    = var.ssh_key_name
  associate_public_ip_address = false

  tags = {
    Name = "${var.prefix}-private-ec2-instance"
  }
}