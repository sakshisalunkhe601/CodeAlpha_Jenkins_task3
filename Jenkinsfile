pipeline {
    agent { label 'python-node' } // This forces execution on your Azure VM

    stages {
        stage('Verify Remote Environment') {
            steps {
                echo "Proving Remoting: Running on ${env.NODE_NAME}"
                sh 'uname -a'
                sh 'python3 --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                // Installs Flask on the remote Azure Linux environment
                sh 'pip3 install flask --break-system-packages' 
            }
        }

        stage('Run Unit Tests') {
            steps {
                // Executes tests on the remote architecture
                sh 'python3 test_app.py'
            }
        }

        stage('Deploy App') {
            steps {
                script {
                    echo "Starting Flask App in the background..."
                    // 1. Stop any existing version of the app running on port 5000
                    sh 'fuser -k 5000/tcp || true'
                    
                    // 2. Start the app and prevent Jenkins from killing the process
                    // host 0.0.0.0 makes it accessible via your Public IP
                    sh 'JENKINS_NODE_COOKIE=dontKillMe nohup python3 app.py > output.log 2>&1 &'
                }
            }
        }
    }

    post {
        success {
            echo "Successfully remoted into Azure and deployed the app!"
            echo "Access it at http://52.141.17.215:5000"
        }
    }
}