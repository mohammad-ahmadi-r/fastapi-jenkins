pipeline {
    agent any

    environment {
        APP_NAME = "fastapi-app"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/mohammad-ahmadi-r/fastapi-jenkins.git',
                    credentialsId: 'github-https-creds'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${APP_NAME}:latest ."
            }
        }

        stage('Deploy') {
            steps {
                sh "echo Deploying ${APP_NAME}..."
            }
        }
    }
}
