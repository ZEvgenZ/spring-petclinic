pipeline {
    agent any
    tools { 
        maven 'maven_3.5.3' 
    }
    stages {
        stage ('Build') {
            steps {
                checkout scm
                echo 'This is a minimal pipeline.'
                sh 'mvn package'
            }
        }
        stage ('print') {
            steps {
                  sh('/home/ubuntu/print.sh') 
                }
        }
    }
}