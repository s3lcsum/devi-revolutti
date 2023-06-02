# REST API

This is a simple Python application to return of days until your user's birthdays.

## Configuration

Makefile will read values from file `.env` or you can pass them as environment values.

```dotenv
# Generic configuration
APP_HOST=0.0.0.0
APP_PORT=8000

# MySQL configuration
DATABASE_USER=
DATABASE_PASS=
DATABASE_HOST=
DATABASE_PORT=
```

## Install

    make install

Creates a virtual environment and installs dependencies

## Run the app

    make run

## Run the tests

    make tests

## Delete temporary files

    make clean

## Build image

    make build TAG=

Build a docker image with passed TAG

# REST API

The REST API to the example app is described below.

## Get your user's birthday

### Request

`GET /hello/{username}`

    curl -i -H 'Content-Type: application/json' http://localhost:8000/hello/test_user

### Response

    HTTP/1.1 200 OK
    Date: Thu, 01 Jan 1999 12:36:30 GMT
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Content-Length: 60

    {"message":"Hello, test_user! Your birthday is in 1 day(s)"}

## Create a user

### Request

`PUT /hello/{username}`

    curl -i -H 'Content-Type: application/json' -d '{"dateOfBirth":"02-01-1997"}' http://localhost:8000/hello/test_user

### Response

    HTTP/1.1 204 No Content
    Date: Thu, 01 Jan 1999 12:36:30 GMT
    Status: 204 No Content
    Connection: close

## Healthcheck

### Request

`GET /_healthz`

    curl -i -H  http://localhost:8000/_healthz

### Response

    HTTP/1.1 200 OK
    Date: Thu, 01 Jan 1999 12:36:30 GMT
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Content-Length: 16

    {"message":"ok"}
