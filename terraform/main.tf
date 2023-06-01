resource "google_container_cluster" "cluster" {
  name               = var.cluster_name
  location           = var.region
  initial_node_count = 1

  node_config {
    machine_type = "n1-standard-1"
  }
}


resource "google_service_account" "github-actions" {
  account_id   = "github-actions"
  display_name = "Service Account for GitHub Actions"
}

resource "google_project_iam_member" "github-actions" {
  project = var.project_id

  role   = "roles/container.developer"
  member = "serviceAccount:${google_service_account.github-actions.email}"
}