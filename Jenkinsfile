node {
  checkout scm

  def customImage = docker.build('flask-env:1.0', '-f tests/Dockerfile .')

  customImage.inside{
    sh 'echo Running Python tests'
    sh 'echo '
    sh 'pytest tests/test_basic.py'
    sh 'pytest tests/test_driver.py'
  }
}