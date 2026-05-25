# GitHub Actions OIDC provider
# Lets AWS verify tokens issued by GitHub Actions
resource "aws_iam_openid_connect_provider" "github_actions" {
  url = "https://token.actions.githubusercontent.com"
  client_id_list = ["sts.amazonaws.com"]
  # GitHub's OIDC thumbprint — AWS uses this to verify the TLS connection
  thumbprint_list = ["9514f4ed3c841c96c43def0f0acbf177405ded12"]
}

# IAM role that GitHub Actions assumes via OIDC
resource "aws_iam_role" "github_actions_deploy" {
  name = "llm-debate-github-actions-deploy"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect    = "Allow"
        Principal = {
          Federated = aws_iam_openid_connect_provider.github_actions.arn
        }
        Action = "sts:AssumeRoleWithWebIdentity"
        Condition = {
          StringEquals = {
            "token.actions.githubusercontent.com:aud" = "sts.amazonaws.com"
            "token.actions.githubusercontent.com:sub" = "repo:ShakibaShahidiani/llm-debate-system:ref:refs/heads/main"
          }
        }
      }
    ]
  })
}

# Permissions for the GitHub Actions deploy role
resource "aws_iam_role_policy" "github_actions_deploy_policy" {
  name = "llm-debate-deploy-policy"
  role = aws_iam_role.github_actions_deploy.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect   = "Allow"
        Action   = ["ec2:DescribeInstances"]
        Resource = "*"
      },
      {
        Effect = "Allow"
        Action = ["ssm:SendCommand"]
        Resource = [
          "arn:aws:ssm:eu-central-1::document/AWS-RunShellScript",
          aws_instance.main.arn
        ]
      },
      {
        Effect   = "Allow"
        Action   = ["ssm:GetCommandInvocation"]
        Resource = "*"
      }
    ]
  })
}
