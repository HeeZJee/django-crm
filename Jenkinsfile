pipeline {
    agent {
        docker {
            image 'python:3-alpine'
               }
            }
    stages {
        stage('Build') { 
            steps {
                sh 'python3 -m venv env'
                sh 'source ./env/bin/activate' 
                sh 'python3 -m pip install -r Requirement.txt'
                sh 'python3 manage.py makemigrations'
                sh 'python3 manage.py migrate'
            }
        }
    }
}
