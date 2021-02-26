pipeline {
  agent {
    dockerfile {
      dir 'tests'
    }
  }

  stages {
    stage('test') {
      steps {
        sh 'echo PWD'
        sh 'ls'
      }
    }
  }
}