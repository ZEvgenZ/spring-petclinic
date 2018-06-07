pipeline    {
    
    agent none

    // agent {
    //     dockerfile true
    //     }

    stages {
        stage ("Build_Application"){
            agent { 
                // docker {
                //     image 'docker:edge'
                //     args '-v  /var/run/docker.sock:/var/run/docker.sock  -v build-volume:/app'
                // }
                docker {
                    image 'maven:3.5.3'
                    args '  -v build-volume:/app'
                    //args '-v  /var/run/docker.sock:/var/run/docker.sock  -v build-volume:/app'

                }
            }
            steps {
                checkout scm
                sh 'mvn package'
            }
        
        stage ("Docker build && push"){
            agent any 
                // docker {
                //     image 'centos7-ansible'
                //     //args '-v build-volume:/app'
                // }
           
            steps {
                //checkout scm
                //sh 'docker run -it maven:3.5.3'
                //sh 'mvn package'
                
                sh 'docker build -t zevgenz/task3_docker:${BUILD_NUMBER} .'
                sh 'docker images'
                withDockerRegistry([ credentialsId: "ID_DockerHub", url: ""]) {
                sh 'docker push zevgenz/task3_docker:${BUILD_NUMBER}'
                }
                // sh 'docker rmi $(docker images | grep anatolek/demo3)'
            }

        }

    }


}