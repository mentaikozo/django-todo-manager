resource "aws_security_group" "test" {
  name   = var.sg_config.name
  vpc_id = var.sg_config.vpc_id

  dynamic "ingress" {
    for_each = var.sg_config.port

    content {
      from_port   = ingress.value
      to_port     = ingress.value
      protocol    = var.sg_config.protocol
      cidr_blocks = var.sg_config.cidr_blocks
    }
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
