.PHONY: help init plan apply destroy

help:
	@echo "Available targets:"
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z0-9_-]+:.*?## / {printf "  %-20s %s\n", $$1, $$2}' $(MAKEFILE_LIST)

init: ## Initialize the Terraform working directory
	terraform init -upgrade

plan: ## Generate an execution plan
	terraform plan

apply: ## Apply the Terraform configuration
	terraform apply

destroy: ## Destroy the infrastructure
	terraform destroy