# Azure-Devops-Building-CI-CD-Pipeline



## Introduction
Continuous Integration(CI) and Continuous Delivery(CD) are two of the five practices that we consider to be at the heart of DevOps.
CI is about Integrating our code in to a source control system so we can get fast feedback on its development where as  CD is about making sure that
every change to our code is ready for release as soon as possible 

In this project, I  build a Github repository from scratch and create a scaffolding that  assist  in performing both CI and CD. I use Github Actions along with a Makefile, requirements.txt and application code to perform an initial lint, test, and install cycle. Next, I integrate this project with [Azure Pipelines](https://azure.microsoft.com/en-us/services/devops/pipelines/) to enable Continuous Delivery to [Azure App Service](https://azure.microsoft.com/en-us/services/app-service/)
## Project Plan
I've included a quarterly and yearly plan in this [spreadsheet](https://docs.google.com/spreadsheets/d/1mVYLtcZ6-ncupYgM3m-HbbmeYRWQXq58leF58VNuDiM/edit#gid=0). There is also an estimated week by week deliverables with a time of difficulty for each task.
## Trello Board
Project management [Trello Board](https://trello.com/b/OIFZz5HW/azure-devops) 
## Architectural Diagram
![alt text](Diagram/Architecture.png)
## CI: Set Up Azure Cloud Shell
   * Create a [Github](https://github.com/) repository
   * Launch an Azure Cloud Shell environment and create ssh-keys. Upload these keys to your GitHub account
   
 ![alt text](Images/ssk-keygen.png)
  
 ![alt text](Images/cloud-shell-gitclone.png)
 * type  ` cat /home/odl_user/.ssh/id_ed25519.pub ` 
 * Copy the generated public key and go to GitHub. Click the settings and paste the key.
  ![alt text](Images/github-ssh.png)
  
 
 
   
   
