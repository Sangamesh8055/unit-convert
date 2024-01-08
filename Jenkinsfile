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
                    sh "docker run -it -p 8081:8081 sangamesh8055/unit-convert ${params.LENGTH_IN_FEET}"
                }
            }
        }
    }
}
