# Variaveis definidas neste arquivos podem ser usadas em qualquer script terraform, pois todos os scripts são compilados em conjunto


variable "base_bucket_name" {
  default = "datalake-igti-m1-terraform"
}

variable "ambiente" {
  default = "producao"
}

variable "numero_conta" {
  default = "945696890928"
}

variable "regiao" {
  description = "AWS region"
  type        = string
  default     = "us-east-1"

}
