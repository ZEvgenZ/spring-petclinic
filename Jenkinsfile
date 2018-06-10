pipeline    {
    
    parameters {
        string(name: 'DB_USER', defaultValue: 'usersql', description: 'User for MariaDB')
        string(name: 'DB_NAME', defaultValue: 'petclinic', description: 'Name of MariaDB')
        string(name: 'DB_PASS', defaultValue: '123456', description: 'Password for MariaDB')
        string(name: 'DB_HOST', defaultValue: 'db', description: 'IP_address of MariaDB')
        string(name: 'DB_PORT', defaultValue: '3306', description: 'Port of MariaDB')
        string(name: 'APP_HOST', defaultValue: 'app', description: 'IP_address of AppHost')
        string(name: 'APP_USER', defaultValue: 'appuser', description: 'User for AppHost')
        string(name: 'APP_PASS', defaultValue: '123456', description: 'Password for AppHost')
    }
    
    agent none

    stages {
    //      stage ('list & instances up') {
    //         agent any

    //         steps { 
    //             withCredentials([[
    //         $class: 'AmazonWebServicesCredentialsBinding',
    //         credentialsId: '321',
    //         accessKeyVariable: 'AWS_ACCESS_KEY_ID',
    //         secretKeyVariable: 'AWS_SECRET_ACCESS_KEY'
    //     ]]) {
    //         sh ('> hosts ')
    //         sh 'AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID} AWS_SECRET_ACCESS_KEY=${AWS_SECRET_ACCESS_KEY} AWS_DEFAULT_REGION=us-east-2 python3 ./start_docker_instance.py' 
    //         }
    //         //sleep 150 // seconds
    //         }
    //     }

        
        
        stage ("Build_Application"){
            agent { 
                
                docker {
                    image 'maven:3.5.3'
                    

                }
            }
            steps {
                checkout scm
                sh 'mvn package'
            }
        }
        stage ("Docker build && push"){
            agent any 
                
           
            steps {
                sh 'docker build -t zevgenz/task3_docker:${BUILD_NUMBER} .'
                sh 'docker tag zevgenz/task3_docker:${BUILD_NUMBER} zevgenz/task3_docker:latest'
                sh 'docker images'
                withDockerRegistry([ credentialsId: "ID_DockerHub", url: ""]) {
                sh 'docker push zevgenz/task3_docker:latest'
                }
                
            }

        }

        stage ('use ansible') {
            
            agent any

            steps {
                withCredentials(bindings: [sshUserPrivateKey(credentialsId: 'AWS_ssh_key',
                                                             keyFileVariable: 'SSH_KEY_FOR_ABC')]) {
                  //create database
                  sh "ANSIBLE_HOST_KEY_CHECKING=False ansible-playbook -i ./hosts --private-key=${SSH_KEY_FOR_ABC} --extra-vars 'db_user=${params.DB_USER} db_name=${params.DB_NAME} db_pass=${params.DB_PASS} db_host=${params.DB_HOST} db_port=${params.DB_PORT} app_pass=${params.APP_PASS} app_host=${params.APP_HOST} app_user=${params.APP_USER}' ./docker_app.yml"
                }

            }
        }
       
    


}
}