region = "us-east-1"
prefix = "abhishek-practice"

vpc_cidr = "10.0.0.0/16"

availability_zone_1  = "us-east-1a"
public_subnet1_cidr  = "10.0.0.0/24"
private_subnet1_cidr = "10.0.1.0/24"
secure_subnet1_cidr  = "10.0.2.0/24"


availability_zone_2  = "us-east-1b"
public_subnet2_cidr  = "10.0.3.0/24"
private_subnet2_cidr = "10.0.4.0/24"
secure_subnet2_cidr  = "10.0.5.0/24"




ami           = "ami-0f88e80871fd81e91"
instance_type = "t2.micro"
ssh_key_name  = "abhishek-dev-us-east"
