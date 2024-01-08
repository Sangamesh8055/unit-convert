pipeline {
    agent any

    parameters {
        string(name: 'LENGTH_IN_FEET', description: 'Length in feet for conversion', defaultValue: '1')
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
                    sh "docker run -i -p 8083:8083 sangamesh8055/unit-convert ${params.LENGTH_IN_FEET}"
                }
            }
        }
    }
}
