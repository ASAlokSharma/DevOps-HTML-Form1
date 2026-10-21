pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                retry(3) {
                    checkout scm
                }
            }
        }

        stage('Verify Files') {
            steps {
                sh 'ls -la'
            }
        }

        stage('Test HTML Form') {
            steps {
                sh 'python3 test_form.py'
            }
        }
    }

    post {
        success { echo 'All form tests passed.' }
        failure { echo 'Form tests failed. Check the Console Output.' }
    }
}
