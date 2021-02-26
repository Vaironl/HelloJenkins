pipeline {
  agent {
    dockerfile {
      dir 'tests'
      additionalBuildArgs '--build-arg -t flasks_tests_demo .'
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