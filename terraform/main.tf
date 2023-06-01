resource "google_container_cluster" "cluster" {
  name               = var.cluster_name
  location           = var.region
  initial_node_count = 1

  node_config {
    machine_type = "n1-standard-1"
  }
}