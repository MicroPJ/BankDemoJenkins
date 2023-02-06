node {

    stage('Clone repository') {
        /* Let's make sure we have the repository cloned to our workspace */

        git branch: "main",
        url: 'https://github.com/MicroFocus/BankDemo.git'
    }

    stage('Provision VSAM') {
        dir("scripts") {
            script {
                if (env.TASK == "provisionVSAM") {
                   echo '*--- START ProvisionVSAM'
                   bat 'python MF_Provision_Region.py vsam'
                   echo '*--- END ProvisionVSAM'
                }
                if (env.TASK == "removeVSAM") {
                   echo '*--- START removeVSAM'
                   echo '*- STOP removeVSAM'
                   bat 'python MF_Region_Stop.py'
                   echo '*- REMOVE removeVSAM'
                   bat 'python MF_Delete_Region.py'
                   echo '*--- END removeVSAM'  
                }

                //bat 'python MF_Provision_Region.py vsam'
            }
         }
    }

    post { 
        always { 
            cleanWs()
        }
    }
    //stage('Provision VSAM') {
    //    /* This builds the actual image; synonymous to
    //     * docker build on the command line */
    //    dir("scripts") {
    //        bat 'python MF_Provision_Region.py vsam'
    //    }
    //}
}
