pipeline {
    agent any

    parameters {
        string(name: 'LENGTH_IN_FEET', description: 'Length in feet for conversion')
    }

    stages {
        stage('Build') {
            steps {
                script {
                    // Define containerName at the beginning of the script
                    def containerName = "unitss-${BUILD_NUMBER}"

                    // Build the Docker image
                    sh "docker build -t sangamesh8055/unit-convert ."
                }
            }
        }

        stage('Run') {
            steps {
                script {
                    // Use the same containerName in subsequent stages
                    def containerName = "unitss-${BUILD_NUMBER}"

                    // Run the Docker container
                    sh "docker run -i -p 8083:8083 --name ${containerName} sangamesh8055/unit-convert"
                }
            }
        }

        stage('Exec') {
            steps {
                script {
                    // Use the same containerName in subsequent stages
                    def containerName = "unitss-${BUILD_NUMBER}"

                    // Show container information
                    sh "docker ps -a"
                    sh "docker logs ${containerName}"
                    // sh "docker exec ${containerName} python unit_converter.py ${params.LENGTH_IN_FEET}"
                }
            }
        }
    }
}
