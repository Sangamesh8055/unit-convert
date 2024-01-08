pipeline {
    agent any

    parameters {
        string(name: 'LENGTH_IN_FEET', description: 'Length in feet for conversion')
    }

    stages {
        stage('Build') {
            steps {
                script {
                    // Use BUILD_NUMBER in the container name
                    def containerName = "unitss-${BUILD_NUMBER}"
                    sh 'docker build -t sangamesh8055/unit-convert .'
                }
            }
        }

        stage('Run') {
            steps {
                script {
                     // Use BUILD_NUMBER in the container name
                    def containerName = "unitss-${BUILD_NUMBER}"
                    sh "docker run -d -p 8083:8083 --name ${containerName} sangamesh8055/unit-convert python unit_converter.py ${params.LENGTH_IN_FEET}"
                }
            }
        }

        stage('Exec') {
            steps {
                script {
                     sh "docker ps -a"
                     sh "docker logs ${containerName}"
                     //sh "docker exec unitss python unit_converter.py ${params.LENGTH_IN_FEET}"
                }
            }
        }
    }
}
