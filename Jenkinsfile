pipeline {
    agent {
        docker {
            image 'python:3-alpine'
               }
            }
    stages {
        stage('Build') { 
            steps {
                sh 'pip install virtualenv'
                sh 'virtualenv venv' 
                sh 'pip install -r Requirement.txt'
                sh 'pip install django'
                sh 'python manage.py makemigrations'
                sh 'python manage.py migrate'
            }
        }
    }
}
