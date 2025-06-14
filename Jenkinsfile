pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                // If your repo is public
                git url: 'https://github.com/AFZALGREAT/jenkinsproject.git', branch: 'main'

                // OR if private, using GitHub token stored as Jenkins credentials
                // git url: "https://${GIT_TOKEN}@github.com/your-username/your-repo.git", branch: 'main'
            }
        }

        stage('Run Fibonacci Script') {
            steps {
                // Run the Python script and provide input (e.g., 7)
                sh 'python3 fibo.py'
            }
        }
    }
}
