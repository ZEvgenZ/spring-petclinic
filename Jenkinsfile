pipeline {
    agent {
        label 'aws_first'
    }
    parameters {
        string(name: 'DB_USER', defaultValue: 'usersql', description: 'User for MariaDB')
        string(name: 'DB_NAME', defaultValue: 'petclinic', description: 'Name of MariaDB')
        string(name: 'DB_PASS', defaultValue: '123456', description: 'Password for MariaDB')
        string(name: 'DB_HOST', defaultValue: '10.0.10.100', description: 'IP_address of MariaDB')
        string(name: 'DB_PORT', defaultValue: '3306', description: 'Port of MariaDB')
        string(name: 'APP_HOST', defaultValue: '10.0.10.200', description: 'IP_address of AppHost')
        string(name: 'APP_USER', defaultValue: 'appuser', description: 'User for AppHost')
        string(name: 'APP_PASS', defaultValue: '123456', description: 'Password for AppHost')
    }
    tools { 
        maven 'maven_3.5.3' 
    }
    stages {
        
        
        stage ('list & deploy') {
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
            steps {
                withCredentials(bindings: [sshUserPrivateKey(credentialsId: 'ec2-user',
                                                             keyFileVariable: 'SSH_KEY_FOR_ABC')]) {
                  //create database
                  sh '${SSH_KEY_FOR_ABC}' ansible-playbook ./playbook.yml
                                                             }
                }

            }
        }
    }
}