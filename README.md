# devi-revolutti

## Create local environment using `kind` k8s-cluster

```bash
export NAME=devi-revolutti

kind create cluster --name $NAME
kind load docker-image $NAME:0.1.0
```

## Setup terraform code

```bash
gcloud auth login
gcloud auth application-default login
gcloud config set project devi-revolutti
```

Enable Kubernets API form the browser
https://console.cloud.google.com/flows/enableapi?apiid=container.googleapis.com&_ga=2.267233742.1106497351.1685574149-189793240.1640013890

### Download GKE config

```
gcloud container clusters get-credentials devi-revolutti --region europe-west1 
```

### Auth GKE to use private GHCR

```bash
kubectl create secret docker-registry github-registry \
  --docker-server=ghcr.io \
  --docker-username= \
  --docker-password= \
  --docker-email=
```

```
(GHA takes care of building new image every commit, but only with tag :latest)

cd terraform && make init && make apply | yes

cd helm/mysql && make init && make apply
cd helm/app && make apply && make test
```

Output

```
❯ curl 35.241.153.211/hello/s3lcsum -X PUT -H 'Content-Type: application/json' -d '{"dateOfBirth":"2020-02-02"}' -v
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

```
❯ curl 35.241.153.211/hello/s3lcsum -H 'Content-Type: application/json'
{"message":"Hello, s3lcsum! Your birthday is in 247 day(s)"}
```

# TODO: GHA auto runs make apply on chart to deploy it to GKE

# TODO: Diagram

# TODO: Clean the code