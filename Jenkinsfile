pipeline {
    agent any

    parameters {
        string(name: 'LENGTH_IN_FEET', description: 'Length in feet for conversion')
    }

    stages {
        stage('Build') {
            steps {
                script {
                    sh 'docker build -t sangamesh8055/unit-convert .'
                }
            }
        }

        stage('Run') {
            steps {
                script {
                    sh "docker run -i -p 8083:8083 --name unit sangamesh8055/unit-convert python unit_converter.py ${params.LENGTH_IN_FEET}"
                }
            }
        }
       stage('exec') {
           steps {
               script {
                   sh "docker exec unit python unit_converter.py 1"
               }
           }
       }
    }
}
