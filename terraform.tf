provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "practice_instance" {
  ami           = "ami-0c02fb55956c7d316" # Amazon Linux 2 AMI (us-east-1)
  instance_type = "t2.micro"

  tags = {
    Environment = "PracticeJMarin"
  }
}

output "instance_public_ip" {
  description = "Public IP address of the EC2 instance"
  value       = aws_instance.practice_instance.public_ip
}