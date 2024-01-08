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
                    sh "docker run -d -p 8083:8083 --name units sangamesh8055/unit-convert python unit_converter.py ${params.LENGTH_IN_FEET}"
                }
            }
        }

        stage('Exec') {
            steps {
                script {
                     sh "docker ps -a"
                     sh "docker logs units"
                     //sh "docker exec units python unit_converter.py ${params.LENGTH_IN_FEET}"
                }
            }
        }
    }
}
