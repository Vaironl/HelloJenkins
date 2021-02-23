pipeline {
  agent {
    docker {
      image 'python:3.9.2'
    }

  }
  stages {
    stage('run main') {
      steps {
        sh 'python Driver.py'
      }
    }

    stage('run tests') {
      steps {
        sh 'python Test.py'
      }
    }

  }
}