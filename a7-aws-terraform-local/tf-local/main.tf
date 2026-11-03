terraform {
  required_providers {
    local = {
      source  = "hashicorp/local"
      version = "~> 2.0"
    }
  }
}

provider "local" {}

# Q2: one welcome file. Q3: second file. Q4: values come from variables.
resource "local_file" "welcome" {
  filename = var.file1_name
  content  = var.file1_content
}

resource "local_file" "second" {
  filename = var.file2_name
  content  = var.file2_content
}
