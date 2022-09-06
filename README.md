# Azure-Devops-Building-CI-CD-Pipeline

![alt text](Diagram/Architecture.png)

## Introduction
Continuous Integration(CI) and Continuous Delivery(CD) are two of the five practices that we consider to be at the heart of DevOps.
CI is about Integrating our code in to a source control system so we can get fast feedback on its development where as  CD is about making sure that
every change to our code is ready for release as soon as possible 

In this project, I  build a Github repository from scratch and create a scaffolding that  assist  in performing both CI and CD. I use Github Actions along with a Makefile, requirements.txt and application code to perform an initial lint, test, and install cycle. Next, I integrate this project with [Azure Pipelines](https://azure.microsoft.com/en-us/services/devops/pipelines/) to enable Continuous Delivery to [Azure App Service](https://azure.microsoft.com/en-us/services/app-service/)
