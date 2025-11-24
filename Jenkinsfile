pipeline {
  agent any
  environment {}
  stages {
    stage('Checkout') {
      steps {
        git url: 'https://github.com/aabdurahim/Assignment2-3.git', branch: 'main'
      }
    }
    stage('Install dependencies') {
      steps {
        bat '"C:\\Users\\aruzh\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m pip install --upgrade pip'
        bat '"C:\\Users\\aruzh\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m pip install -r requirements.txt'
      }
    }
    stage('Run tests') {
      steps {
        bat '"C:\\Users\\aruzh\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m pytest -q tests\\ --junitxml=results.xml'
      }
    }
  }
  post {
    always {
      junit 'results.xml'
      archiveArtifacts artifacts: 'results.xml', onlyIfSuccessful: false
    }
  }
}