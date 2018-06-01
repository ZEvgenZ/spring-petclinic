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





        }



    }


}