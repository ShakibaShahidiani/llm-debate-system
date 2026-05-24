variable "project_name" {
  description = "Name prefix for all resources"
  type        = string
  default     = "llm-debate"
}

variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "eu-central-1"
}

variable "db_password" {
  description = "PostgreSQL master password"
  type        = string
  sensitive   = true
}
