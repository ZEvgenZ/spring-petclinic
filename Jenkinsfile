pipeline    {
    
    agent none

    stages {
         stage ('list & instances up') {
            agent any

            steps { 
                withCredentials([[
            $class: 'AmazonWebServicesCredentialsBinding',
            credentialsId: '321',
            accessKeyVariable: 'AWS_ACCESS_KEY_ID',
            secretKeyVariable: 'AWS_SECRET_ACCESS_KEY'
        ]]) {
            sh ('> hosts ')
            sh 'AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID} AWS_SECRET_ACCESS_KEY=${AWS_SECRET_ACCESS_KEY} AWS_DEFAULT_REGION=us-east-2 python3 ./start_docker_instance.py' 
            }
            //sleep 150 // seconds
            }
        }

        
        
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
                  sh "ANSIBLE_HOST_KEY_CHECKING=False ansible-playbook -i ./hosts ./docker_app.yml"
                }

            }
        }
       
    


}
}