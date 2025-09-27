## Fastapi with jenkins

This project is a FastAPI application with a Dockerfile and a Jenkinsfile for automated CI/CD. Jenkins will use the Jenkinsfile to build, test, and deploy the application in a containerized environment.

---

## Features

✅ FastAPI backend application.

✅ Dockerized for easy deployment.

✅ Jenkins pipeline integration (Jenkinsfile) for CI/CD:

	Build Docker image.
	Run tests.
	Deploy container.

✅ Supports GitHub integration for automated builds.

---

## Prerequisites

- Docker installed on the target machine.(https://docs.docker.com/engine/install)
- Jenkins server with Docker permissions.(https://github.com/mohammad-ahmadi-r/ansible-jcasc.git)
- GitHub repository containing this project.

---

## Securing
Create a personal access token in github

Create a credential in Jenkins with given PAT (personal access token).

Jenkins assigns it an ID (you can see or set this in Jenkins UI).

When your pipeline uses credentialsId, Jenkins automatically uses those credentials for Git operations.

Here we have:
	```bash
		credentialsId: 'github-https-creds'
	```

---

## Jenkins pipeline

Ensure your Jenkins server has the Git and Docker plugins installed.

Add a pipeline job pointing to your GitHub repository.

Jenkins will automatically pick up the Jenkinsfile and execute the pipeline:

Checkout code from GitHub.

Build Docker image.

Run tests and/or deploy.

---

## Triggering Builds

Push code to GitHub → Jenkins pipeline will trigger automatically (if webhook is configured).

Or manually trigger via Jenkins UI

Or via jenkins API Call. 