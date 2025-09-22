## Mindstix Bootcamp 2025

[![Infrastructure](https://github.com/rhlm-msx/bootcamp/actions/workflows/infra.yaml/badge.svg)](https://github.com/rhlm-msx/bootcamp/actions/workflows/infra.yaml)

- [Explore the App](https://rhlm-msx.github.io/bootcamp/)


## The Architecture

```mermaid

architecture-beta
    group aws(cloud)[AWS]
    service rest(server)[RESTapi] in aws
    service db(database)[Database] in aws
    service s3(disk)[Bucket] in aws
    
    service app(server)[Web App]

    rest:R -- L:db
    rest:B -- L:s3
    app:R -- L:rest

```

### Modules

- Frontend
    - Part of Web App.
- Backend
    - APIs for that modules
- Each module is responsible for initializting its resources and validating them

- The Main Module requires.
    + Database
    + Bucket


> There are two types of modules

```mermaid
flowchart TD

Modules --> Main
Modules --> App

```

> Main: The Webapp, and main routes in backend of restapi.



### Main Module

- Fetch Available Modules.
- Data
    1. Type: MAIN/APP
    2. Icon
    3. Description


### Modules

1. Frontend.
2. Backend (RESTapi).

## The Main Module Implementation

```mermaid

kanban
    database[Database]
        t1[Define Schema]
        t2[Intializting the Data]
        t3[The ORM]

```

## The Main Module Database

- It need to be aware of other modules.
- Information about its own

```mermaid

classDiagram
    class Module
    Module: ID [Integer | Autoinc, Identifier]
    Module: Type [MAIN|APP]
    Module: Name [String]
    Module: Route [String, Path]
    Module: Description [String, Markdown]
    Module: Icon [String, Path]
```


---

- [x] Setup Github Workflow (with the help of github market place).
- [x] Github Pages.
- [ ] S3 Bucket AWS
- [ ] Empty ECR on Destroy


Changing Approach

1. Github Pages: Host Webapp.
2. AWS Infrasture: Hosts RESTapi and rest of the resources


## Github Workflow

```mermaid

flowchart LR

push[Push]
step1(Create Infra on AWS)
step2(Replace Correct Lambda FURL in Static pages)
step3(Publish site to github pages)

push --> step1
push --> step2
push --> step3

```


Todo
1. Get Site Working
    - Front End Working with proper reporting of error and have correct remote(dns) for backend instance.

## Local Deployement

- Localstack.
    - AWS Lambda with layers
    - S3 Bucket
    - Database

- Intialization of Resources
    - AWS Lambda (Image and Code).
    - S3 Bucket  (Upload and Syncronise Assets).
    - Database
        - SQL ().
        - NoSQL ().


## Complete Deployment

- Intialization of Resources
    - AWS Lambda (Image and Code).
    - S3 Bucket  (Upload and Syncronise Assets).
    - Database
        - SQL ().
        - NoSQL ().


## Requirements

### Deploy app in local

```bash
$ make local
```


### Deploy app in cloud
```bash
$ make cloud
```



## Information

Since when using localstack the deployement cant be with Docker Image therefore Layers must be used for larger pacakages.

### The Layer Code

> Extracted in /opt
therefore must be in pythonpaths.

> Expected zip structure => /python/content


### The Function Code

> Extracted in /var/task



## Resources and References

- [Terraform Remote Backend](https://stackoverflow.com/questions/47913041/initial-setup-of-terraform-backend-using-terraform)
