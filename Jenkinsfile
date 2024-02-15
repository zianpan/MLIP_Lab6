pipeline {
    agent any

    stages {
        stage('Prebuild Conda Setup') {
            steps {
                CONDA_PATH=$HOME/zekail/miniconda3
                eval "$($CONDA_PATH/bin/conda shell.bash hook)"
            }
        }
        stage('Build') {
            steps {
                echo 'In C or Java, we can compile our program in this step'
                echo 'In Python, we can build our package here or skip this step'
            }
        }
        stage('Test') {
            steps {
                echo 'Test Step: We run testing tool like pytest here'
                conda run -n mlip python -m pytest
                // TODO: Run pytest command here
                // echo 'Pytest Not Run!!'
                // exit 1
            }
        }
        stage('Deploy') {
            steps {
                echo 'In this step, we deploy our porject'
                echo 'Depending on the context, we may publish the project artifact or upload pickle files'
            }
        }
    }
}
