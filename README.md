# devi-revolutti

This project aims to create a local development environment using the kind Kubernetes cluster.
It also includes setup instructions for Terraform and GKE (Google Kubernetes Engine) configuration.

## Create a Local Environment using `kind` for kubernetes cluster

To create the local environment, follow these steps:

```bash
# Create the kind cluster
kind create cluster --name $NAME

# Load the Docker image
kind load docker-image $NAME:0.1.0
```

## Create a GKE environment using kind Kubernetes Cluster

To set up the Terraform code and configure GCP (Google Cloud Platform), follow these steps:

```bash
# # Configure Google Cloud CLI
gcloud auth login
gcloud auth application-default login
gcloud config set project $GKE_PROJECT_ID
gcloud config set region $GKE_REGION
```

**Note**: Before proceeding further, ensure that you have enabled the Kubernetes API by visiting the following link in
your
browser: [Enable Kubernetes API](https://console.cloud.google.com/flows/enableapi?apiid=container.googleapis.com&_ga=2.267233742.1106497351.1685574149-189793240.1640013890)

### Configure and apply the terraform code

Terraform will create a simple GKE Cluster and service account used later for GitHub Actions workflows.

```bash
cd terraform

make init

cat >defaults.auto.tfvars <<EOF
project_id = "$GKE_PROJECT_ID"
region = "$GKE_REGION"
cluster_name = "$CLUSTER_NAME"
EOF

make apply
```

Generate `kubeconfig` basing on GKE

```bash
gcloud container clusters get-credentials $CLUSTER_NAME
```

## Deploy Helm charts

Check your default `values.yaml` files inside `helm/` directory and then apply those charts to your kube contex.

```bash
(cd helm/mysql && make init && make apply)
(cd helm/app && make apply && make test)
```

**Note:** you can print manifests before apply using this make target:

```bash
make validate
```

### Test your application

Make a simple request using a `curl` command to PUT your data into the database.

```
❯ curl 35.241.153.211/hello/s3lcsum -X PUT -H 'Content-Type: application/json' -d '{"dateOfBirth":"1999-01-01"}' -v
*   Trying 35.241.153.211:80...
* Connected to 35.241.153.211 (35.241.153.211) port 80 (#0)
> PUT /hello/s3lcsum HTTP/1.1
> Host: 35.241.153.211
> User-Agent: curl/7.88.1
> Accept: */*
> Content-Type: application/json
> Content-Length: 28
>
< HTTP/1.1 204 No Content
< date: Wed, 31 May 2023 23:55:00 GMT
< server: uvicorn
< content-type: application/json
<
* Connection #0 to host 35.241.153.211 left intact
```

More examples of API requests you can find in this [file](app/README.md)

## GitHub Actions

To authorize your workflows to deploy new charts into GKE you can follow these steps:

### Generate Key for service account generated via terraform code

```bash
gcloud iam service-accounts keys create credentials.json --iam-account=github-actions@${PROJECT_ID}.iam.gserviceaccount.com
```

### Put secrets and GKE configuration into your repository

```bash
gh secret set GKE_CREDENTIALS_JSON < credentials.json
gh variable set GKE_CLUSTER_NAME --body $CLUSTER_NAME
gh variable set GKE_REGION --body $GKE_REGION
```

### Push new `imagePullSecret` into your kubernetes

```bash
export GH_TOKEN=$(gh auth token)

kubectl create secret docker-registry github-registry \
  --docker-server=ghcr.io \
  --docker-username=$GH_USER \
  --docker-password=$GH_TOKEN \
  --docker-email=$GH_EMAIL

```

### Diagram of example GKE deployment

![architecture.png](docs%2Farchitecture.png)


