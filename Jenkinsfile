pipeline {
  agent {
    dockerfile {
      dir 'tests'
      additionalBuildArgs '.'
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