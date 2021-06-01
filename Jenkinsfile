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
                sh 'pip install --user -r Requirement.txt'
                sh 'python manage.py makemigrations'
                sh 'python manage.py migrate'
            }
        }
    }
}
