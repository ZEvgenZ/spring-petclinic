pipeline {
    agent {
        label 'aws_first'
    }
    tools { 
        maven 'maven_3.5.3' 
    }
    stages {
        
        }
        stage ('list') {
            steps { 
                withCredentials([[
            $class: 'AmazonWebServicesCredentialsBinding',
            credentialsId: '321',
            accessKeyVariable: 'AWS_ACCESS_KEY_ID',
            secretKeyVariable: 'AWS_SECRET_ACCESS_KEY'
        ]]) {
            sh 'AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID} AWS_SECRET_ACCESS_KEY=${AWS_SECRET_ACCESS_KEY} AWS_DEFAULT_REGION=us-east-2 python3 ./list_instances.py'
            sh 'AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID} AWS_SECRET_ACCESS_KEY=${AWS_SECRET_ACCESS_KEY} AWS_DEFAULT_REGION=us-east-2 python3 ./start_instances.py' 
            }
            }
        }
    }
}