# HCL - Hashicorp Configuration Language
# Linguagem declarativa

resource "aws_s3_bucket" "mybucket" {
  bucket = "${var.base_bucket_name}-${var.ambiente}-${var.numero_conta}"
  tags = {
    XP     = "IGTI",
    COURSE = "EDC"
  }
}

resource "aws_s3_bucket_server_side_encryption_configuration" "datalake" {
  # Parâmetros de configuração do recurso escolhido
  # Buscar no google: terraform aws s3
  # https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/s3_bucket
  #bucket = "$(var.base_bucket_name)-$(var.ambiente)-$(var.numero_conta)"
  bucket = aws_s3_bucket.mybucket.id
  #server_side_encryption_configuration {
  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
  #}
}

resource "aws_s3_bucket_acl" "datalake_acl" {
  bucket = aws_s3_bucket.mybucket.id
  acl    = "private"
}

#Inserindo arquivo no Bucket
resource "aws_s3_bucket_object" "codigo_spark" {
  bucket = aws_s3_bucket_server_side_encryption_configuration.datalake.id
  key    = "emr-code/pyspark/job_emr_spark.py"
  acl    = "private"
  source = "../job_emr_spark.py"
  etag   = filemd5("../job_emr_spark.py")
  # etag controla se o arquivo foi mudado e precisa ser enviado novamente quando for rodar este script
}

provider "aws" {
  region  = var.regiao

}

# Centralizar o arquivo de controle de estado do terraform
terraform {
  backend s3 {
    bucket = "terraform-state-igti-ricardonn"
    key = "state/igti/edc/mod1/terraform.tfstate"
    region = "us-east-1"
  }
}