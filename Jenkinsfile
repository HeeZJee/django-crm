pipeline {
    agent {
        docker {
            image 'python:3-alpine'
               }
            }
    stages {
        stage('Build') { 
            steps {
                sh 'chown -R ${whoami}:${whoami} .' 
                sh 'python -m venv venv'
                sh 'ls -lah'
                sh 'pip install -r Requirement.txt'
                sh 'pip install  django'
                sh 'django-admin --version'
                sh 'python manage.py makemigrations'
                sh 'python manage.py migrate'
            }
        }
    }
}
