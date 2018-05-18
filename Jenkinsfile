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
        
        
        stage ('list & instances up') {
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
            //sleep 200 // seconds
            }
        }
        
        
        stage ('use ansible') {

            steps {
                withCredentials(bindings: [sshUserPrivateKey(credentialsId: 'e145d958-9659-4471-9506-1f860bc75401',
                                                             keyFileVariable: 'SSH_KEY_FOR_ABC')]) {
                  //create database
                  sh "ANSIBLE_HOST_KEY_CHECKING=False ansible-playbook -i ./hosts --private-key=${SSH_KEY_FOR_ABC} --extra-vars 'db_user=${params.DB_USER} db_name=${params.DB_NAME} db_pass=${params.DB_PASS} db_host=${params.DB_HOST} db_port=${params.DB_PORT} app_pass=${params.APP_PASS} app_host=${params.APP_HOST} app_user=${params.APP_USER}' ./playbook.yml"
                  //sh "ANSIBLE_HOST_KEY_CHECKING=False ansible-playbook -i ./hosts --private-key=${SSH_KEY_FOR_ABC} --extra-vars 'db_user=${params.DB_USER} db_name=${params.DB_NAME} db_pass=${params.DB_PASS} db_host=${params.DB_HOST} db_port=${params.DB_PORT} app_pass=${params.APP_PASS} app_host=${params.APP_HOST} app_user=${params.APP_USER}' ./playbook_db.yml"
                  sh "ANSIBLE_HOST_KEY_CHECKING=False ansible-playbook -i ./hosts --private-key=${SSH_KEY_FOR_ABC} --extra-vars 'db_user=${params.DB_USER} db_name=${params.DB_NAME} db_pass=${params.DB_PASS} db_host=${params.DB_HOST} db_port=${params.DB_PORT} app_pass=${params.APP_PASS} app_host=${params.APP_HOST} app_user=${params.APP_USER}' ./playbook_app.yml"
                }

            }
        }
        

    }
}