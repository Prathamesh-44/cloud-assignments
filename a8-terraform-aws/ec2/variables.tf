variable "region" {
  type    = string
  default = "ap-south-1"
}
variable "instance_type" {
  type    = string
  default = "t3.micro"   # Q10: change to t3.small and run terraform apply again
}
