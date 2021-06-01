pipeline {
    agent {
        docker {
            image 'python:2-alpine'
               }
            }
    stages {
        stage('Build') { 
            steps {
                sh 'apt get install python'
                sh 'python -m pip install Django'
                sh 'python -m venv virtualenv' 
                sh 'source ./virtualenv/bin/activate' 
                sh 'pip install -r requirements.txt'
                sh 'python manage.py makemigrations'
                sh 'python manage.py migrate'
            }
        }
    }
}
