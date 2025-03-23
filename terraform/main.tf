terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 4.67"
    }
  }

  required_version = ">= 1.2.0"
}

provider "aws" {
  region = "ap-northeast-1"
}

module vpc {
  source = "./modules/vpc"

  vpc_config = {
    NameTag              = "Terraform"
    cidr_block           = "10.0.0.0/16"
    enable_dns_support   = true
    enable_dns_hostnames = true
    subnet_count         = 2
  }
}

module ec2-sg {
  source = "./modules/sg"

  sg_config = {
    name        = "ec2-sg"
    vpc_id      = module.vpc.vpc_id
    protocol    = "tcp"
    port        = [80]
    cidr_blocks = ["0.0.0.0/0"]
  }
}

module ec2 {
  source = "./modules/ec2"

  ec2_config = {
    vpc_id           = module.vpc.vpc_id
    public_subnet_id = module.vpc.public_subnet_id
    sg_id            = module.ec2-sg.sg_id
    NameTag          = "django-server"
    instance_type    = "t2.micro"
    instance_count   = 1
    key_name         = "test-key"
  }
  storage_config = {
    volume_type           = "gp2"
    volume_size           = 8
    delete_on_termination = true
  }
}
