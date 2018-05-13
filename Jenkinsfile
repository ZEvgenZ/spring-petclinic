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
                  sh('python /home/zevgenz/my_AWS_progects/task2/list_instances.py') 
                }
        }
    }
}