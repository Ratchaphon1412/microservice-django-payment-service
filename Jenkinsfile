
pipeline {
    agent any
    
    environment {
        SSH_HOST = 'microservice.payment.ratchaphon1412.co'
        SSH_PORT = '22'
        SSH_USER = 'root'
    }
    
    stages {
        stage('SSH to Target Server') {
            steps {
                script {
                  
                    sh """
                        ssh ${SSH_USER}@${SSH_HOST} -y <<EOF
                        cd ~/microservice-django-payment-service
                        docker compose  -f docker-compose.prod.yml down
                        git pull
                        docker compose -f docker-compose.prod.yml up -d --build
                        docker system prune -f
EOF
                    """
                    
                }
            }
        }
    }
}
