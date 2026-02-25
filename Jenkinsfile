pipeline {
    agent { label 'python-node' } // This TELLS Jenkins to use your Azure VM

    stages {
        stage('Verify Remote Environment') {
            steps {
                sh 'uname -a'
                sh 'python3 --version'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip3 install flask --break-system-packages' 
            }
        }
        stage('Run Unit Tests') {
            steps {
                sh 'python3 test_app.py'
            }
        }
    }
}