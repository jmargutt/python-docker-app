# python-docker-app
template for python docker app

## Requirements
Locally:
1. Python 3.*
2. [Docker Desktop](https://www.docker.com/products/docker-desktop)
3. [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/what-is-azure-cli)

In Azure:
1. An [Azure Resource Group](https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/overview) (BEST PRACTICE: make a new resource group for each project)
2. An [Azure Container Registry](https://docs.microsoft.com/en-us/azure/container-registry/container-registry-intro) to store your docker image

## Basic setup
1. Choose a custom name for your python app. Example: `myapp`
2. Add your code into `myapp/src/myapp`
3. Configure `myapp/setup.py`
4. Configure `Dockerfile`
5. Build a docker image
```
docker build -t myregistry.azurecr.io/my-docker-app:latest .
```
6. Create a container locally and test that everything is running fine
```
docker run -it --name  test-container --entrypoint /bin/bash myregistry.azurecr.io/my-docker-app:latest
```
7. Push your docker image to an Azure Container Registry
```
az login
az acr login -n myregistry 
docker image push myregistry.azurecr.io/my-docker-app:latest
```

## Data, Passwords, Secrets
* Download/upload data from/to Azure datalake using [azure-storage-blob](https://pypi.org/project/azure-storage-blob/)
* Get passwords and secrets from Azure key vault using [azure-keyvault-secrets](https://pypi.org/project/azure-keyvault-secrets/) (BEST PRACTICE: do NOT store them in the docker image)
