pipeline    {
    
    agent none

    // agent {
    //     dockerfile true
    //     }

    stages {
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
                sh 'docker images'
                withDockerRegistry([ credentialsId: "ID_DockerHub", url: ""]) {
                sh 'docker push zevgenz/task3_docker:${BUILD_NUMBER}'
                }
                
            }

        }

    


}
}