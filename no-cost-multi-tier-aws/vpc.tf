resource "aws_vpc" "no-cost-main" {
  cidr_block           = var.vpc_cidr
  enable_dns_support   = true
  enable_dns_hostnames = true

  tags = var.common_tags

}

resource "aws_internet_gateway" "no-cost-igw" {
  vpc_id = aws_vpc.no-cost-main.id

  tags = var.common_tags
}

