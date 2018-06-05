pipeline    {
    
    agent none

    stages {
        stage ("Build_Application"){

            agent { 
                docker {
                    image 'docker:edge'
                    args '-v  /var/run/docker.sock:/var/run/docker.sock  -v build-volume:/app'


                }





            }
            steps {
                ansiColor('xterm') {
                    checkout scm
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


}