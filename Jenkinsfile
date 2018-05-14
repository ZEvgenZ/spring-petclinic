pipeline {
    agent {
        label 'label1'
    }
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
        stage ('list') {
            steps { 
                  sh('./list_instances.py') 
                }
        }
    }
}