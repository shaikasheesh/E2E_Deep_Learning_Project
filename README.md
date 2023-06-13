# chicken-Disease classification

## workflows
1.Update config.yaml

2.Update secrets.yaml [Optional]

3.Update params.yaml

4.Update the entity

5.Update the configuration manager in src config

6.Update the components

7.Update the pipeline

8.Update the main.py

9.Update the dvc.yaml

# AZURE-CICD-Deployment-with-Github-Actions steps

Save pass:
save the password from Azure container

Run from terminal:
docker build -t appclassifier.azurecr.io/dltest:latest .

docker login appclassifier.azurecr.io

docker push appclassifier.azurecr.io/dltest:latest

Deployment Steps:
Build the Docker image of the Source Code

Push the Docker image to Container Registry

Launch the Web App Server in Azure

Pull the Docker image from the container registry to Web App server and run