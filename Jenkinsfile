pipeline {
  agent {
    docker {
      image 'python:3.9.2'
    }

  }
  stages {
    //Python does not need to 'build'. But the following build stage installs the needed requirements
    stage('build') {
      steps {
        sh 'pip install -r requirements.txt'
      }
    }

    stage('test') {
      steps {
        sh 'python test.py'
      }

      post {
        always {junit 'test-report/*.xml'}
      }
    }

  }
}