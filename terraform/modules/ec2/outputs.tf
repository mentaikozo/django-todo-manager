output "instance_ip" {
  value = {
    for instance in aws_instance.django-server[*] :
    instance.tags.Name => instance.public_ip
  }
}
output "instance_id" {
  value = aws_instance.django-server[*].id
}
