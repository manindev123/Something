output "cluster_name" {
  value = module.eks.cluster_name
}

output "cluster_region" {
  value = var.aws_region
}

output "vpc_id" {
  value = aws_vpc.main.id
}

output "ecr_url" {
  value = aws_ecr_repository.repo.repository_url
}

output "rds_endpoint" {
  value = aws_db_instance.rds.address
}

output "alb_role_arn" {
  value = aws_iam_role.alb_controller.arn
}

output "db_username_ssm" {
  value = aws_ssm_parameter.db_username.name
}

output "db_password_ssm" {
  value = aws_ssm_parameter.db_password.name
}
