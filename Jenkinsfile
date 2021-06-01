pipeline {
    agent {
        docker {
            image 'python:3-alpine'
               }
            }
    stages {
        stage('Build') { 
            steps {
                sh 'python -m pip install Django --user'
                sh 'python -m venv virtualenv' 
                sh 'source ./virtualenv/bin/activate' 
                sh 'pip install -r requirements.txt'
                sh 'python manage.py makemigrations'
                sh 'python manage.py migrate'
            }
        }
    }
}
