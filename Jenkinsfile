pipeline {
    agent any
    stages {
        stage('Build') { 
            steps {
                sh 'python -m venv virtualenv' 
                sh 'source ./virtualenv/bin/activate' 
                sh 'pip install -r requirements.txt'
                sh 'python manage.py makemigrations'
                sh 'python manage.py migrate'
            }
        }
    }
}
