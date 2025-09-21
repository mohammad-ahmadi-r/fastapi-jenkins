pipeline {
    agent any

    environment {
        IMAGE_NAME = 'fastapi-app'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'git@github.com:mohammad-ahmadi-r/fastapi-jenkins.git',
                    credentialsId: 'ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIKwNO393cTmbzUGH1AL12zyh1s84NKg6m8a9fYk2e24j jenkins@server'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${IMAGE_NAME} ."
            }
        }

        stage('Run Container') {
            steps {
                echo "Running Docker container for testing..."
                sh "docker run -d --name ${IMAGE_NAME} -p 8000:8000 ${IMAGE_NAME}"
                sh "sleep 5" // give server a few seconds to start
                sh "curl -f http://localhost:8000/ || exit 1"
                sh "docker stop ${IMAGE_NAME} && docker rm ${IMAGE_NAME}"
            }
        }
    }
}

