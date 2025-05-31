
resource "aws_instance" "public_app_server" {
  ami                         = var.ami
  instance_type               = var.instance_type
  subnet_id                   = aws_subnet.subnet_public.id
  vpc_security_group_ids      = [aws_security_group.security_group_public.id]
  key_name                    = var.ssh_key_name
  associate_public_ip_address = var.associate_public_ip_address

  # we can use remote-exec provisioner to copy the server.py file to the instance
  user_data = <<-EOF
                #!/bin/bash
                sudo yum update -y && sudo yum upgrade -y
                sudo yum install -y python3
                sudo python3 -m ensurepip --default-pip
                sudo pip3 install flask
                sudo pip3 install --upgrade pip
                EOF
  tags = {
    Name = "${var.prefix}-ec2-instance"
  }
}