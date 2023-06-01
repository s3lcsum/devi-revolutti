terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 4.67"
    }
  }
}

provider "google" {
  project = var.project_id
  region  = var.region
}