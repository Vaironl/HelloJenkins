pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'echo test'
                sh 'python --version'
                sh 'python Driver.py'
            }
        }
    }
}
