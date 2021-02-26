node {
  checkout scm

  def customImage = docker.build('flask-env:1.0', 'tests .')

  customImage.inside{
    sh 'ls'
  // docker build -t flask_tests -f customDockerFile .
  }
}