variable "vpc_config" {
  type = object({
    NameTag              = string
    cidr_block           = string
    enable_dns_support   = bool
    enable_dns_hostnames = bool
    subnet_count         = number
  })
}
