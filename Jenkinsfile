pipeline {
    agent {
        dockerfile {
            filename 'Dockerfile'
            dir '.'
            label 'docker'
        }
    }

    stages {
        stage('Build & Test'){
            steps{
                sh 'echo "Running inside container"'
                sh 'python --version'
                sh 'python fibo.py'
            }
        }
    }
   // parameters {
   //     choice (name: 'ENV' , choices:['dev','staging','production'] , description:'type of sites' )
   // }
    
    // environment {
    //     // Reference to the Jenkins credentials ID (you created it as 'github' or similar)
    //     GIT_TOKEN = credentials('github_token11')
    //     NAME = 'Afzal'
    // }
    // stages {
    //     stage('Clone Repo') {
    //         steps {
    //             // If your repo is public
    //             git url: 'https://github.com/AFZALGREAT/jenkinsproject.git', branch: 'main' ,
    //             credentialsId: 'github_token111'

    //             // OR if private, using GitHub token stored as Jenkins credentials
    //             // git url: "https://${GIT_TOKEN}@github.com/AFZALGREAT/jenkinsproject.git", branch: 'main'
    //         }
    //     }

    //     stage('Run Fibonacci Script') {

    //         when {
    //             expression {params.ENV == 'production'}
    //         }
    //         steps {
    //             // Run the Python script and provide input (e.g., 7)
    //             sh 'python3 -u fibo.py'
    //             echo NAME
    //         }
    //     }
    // }
}
