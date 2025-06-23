terraform {
  backend "s3" {
    bucket       = "abhishek-iac-lab-tfstate"
    key          = "terraform/state/terraform.tfstate"
    region       = "ap-south-1"
    encrypt      = true // Recommended for sensitive state data
    use_lockfile = true // Enables S3-native state locking
  }
}

provider "aws" {
  region = var.region
}