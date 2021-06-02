pipeline {
    agent {
        docker {
            image 'python:3-alpine'
               }
            }
    stages {
        stage('Build') { 
            steps {
                sh 'python -m venv env'
                sh 'source ./env/bin/activate' 
                sh './env/bin/pip install -r Requirement.txt'
                sh './env/bin/pip install django'
                sh 'python manage.py makemigrations'
                sh 'python manage.py migrate'
            }
        }
    }
}
