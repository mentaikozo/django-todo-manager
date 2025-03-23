data aws_ssm_parameter amzn2_ami {
  name = "/aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2"
}

resource "aws_instance" "django-server" {
  count         = var.ec2_config.instance_count
  ami           = data.aws_ssm_parameter.amzn2_ami.value
  instance_type = var.ec2_config.instance_type
  key_name      = var.ec2_config.key_name
  vpc_security_group_ids = [
    var.ec2_config.sg_id
  ]
  subnet_id = element(var.ec2_config.public_subnet_id, count.index % length(var.ec2_config.public_subnet_id))
  root_block_device {
    volume_type           = var.storage_config.volume_type
    volume_size           = var.storage_config.volume_size
    delete_on_termination = var.storage_config.delete_on_termination
  }
  tags = {
    Name = "${var.ec2_config.NameTag}-instance${count.index}"
  }
}
