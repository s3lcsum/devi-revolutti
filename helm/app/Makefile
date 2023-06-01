#!/usr/bin/env make -f
.PHONY: help install upgrade uninstall status list lint validate

# Define variables
RELEASE_NAME := app
NAMESPACE := default


help: ## Show this help message
	@echo "Available targets:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}'

apply: ## Install or upgrade the Helm chart
	helm upgrade --install $(RELEASE_NAME) ./ --namespace $(NAMESPACE)

uninstall: ## Uninstall the Helm chart
	helm uninstall $(RELEASE_NAME) --namespace $(NAMESPACE)

validate: ## Validate the Helm chart values
	helm template --values ./values.yaml ./

update: ## Update just a image.tag for deployment
	helm upgrade $(RELEASE_NAME) ./ --reuse-values --set image.tag=$(IMAGE_TAG)
