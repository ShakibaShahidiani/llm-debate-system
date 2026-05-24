resource "aws_ssm_parameter" "groq_api_key" {
  name        = "/${var.project_name}/groq-api-key"
  description = "Groq API key"
  type        = "SecureString"
  value       = "placeholder"

  tags = {
    Name = "${var.project_name}-groq-api-key"
  }
  
  lifecycle {
    ignore_changes = [value]
  }
}

resource "aws_ssm_parameter" "database_url" {
  name        = "/${var.project_name}/database-url"
  description = "PostgreSQL connection string"
  type        = "SecureString"
  value       = "placeholder"

  tags = {
    Name = "${var.project_name}-database-url"
  }
  lifecycle {
    ignore_changes = [value]
  }

}

