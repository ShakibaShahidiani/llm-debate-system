output "ec2_public_ip" {
  description = "Public IP of the EC2 instance"
  value       = aws_instance.main.public_ip
}

output "rds_endpoint" {
  description = "RDS PostgreSQL endpoint"
  value       = aws_db_instance.main.endpoint
}

output "ssm_groq_key_path" {
  description = "SSM path for Groq API key"
  value       = aws_ssm_parameter.groq_api_key.name
}

output "ssm_database_url_path" {
  description = "SSM path for database URL"
  value       = aws_ssm_parameter.database_url.name
}

output "github_actions_role_arn" {
  value = aws_iam_role.github_actions_deploy.arn
}
