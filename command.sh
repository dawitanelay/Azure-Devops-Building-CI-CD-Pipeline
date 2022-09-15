#!/usr/bin/env bash
git https://github.com/dawitanelay/Azure-Devops-Building-CI-CD-Pipeline.git
cd Azure-Devops-Building-CI-CD-Pipeline
make all
python3 -m venv ~/.Azure-pipline
source ~/.Azure-pipline/bin/activate
az webapp up --name Flaskml-app --resource-group Azuredevops
