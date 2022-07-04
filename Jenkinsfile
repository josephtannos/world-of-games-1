pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checkout out to the repo'
                git branch: 'main',
                credentialsId: 'my_cred_id',
                url: 'git@github.com:josephtannos/world-of-games-1.git'
                sh "ls -lat"
            }
        }
        stage('Build') {
            steps {
                echo 'Bulding..'
                sh "docker build -t app:latest ."
            }
        }

        stage('Run') {
            steps {
                echo 'Running app container'
                sh "docker run -it -d -p 5000:8777 --name webapp app:latest \
                -v /usr/src/app/Scores.txt:/usr/src/app/Scores.txt"
            }
        }

         stage('Test') {
            steps {
                echo 'Running Tests'
                sh "docker exec webapp python -m unittest tests/*"
            }
        }
        stage('Finalize') {
            steps {
                echo 'Finalizing'
                sh "docker stop webapp"
                sh "docker-compose push"
            }
        }
    }
}