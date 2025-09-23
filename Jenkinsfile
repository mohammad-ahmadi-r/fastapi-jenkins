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

        stage('Build') {
            steps {
                echo "Building FastAPI app..."
            }
        }

        stage('Test') {
            steps {
                echo "Running tests..."
            }
        }
    }
}
