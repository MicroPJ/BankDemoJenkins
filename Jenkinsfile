node {

    stage('Clone repository') {
        /* Let's make sure we have the repository cloned to our workspace */

        git branch: "main",
        url: 'https://github.com/MicroFocus/BankDemo.git'
    }

    stage('Provision VSAM') {
        dir("scripts") {
            script {
                if (TASK == "ProvisionVSAM") {
                   bat 'python MF_Provision_Region.py vsam'
                } else {
                   echo 'NOT ProvisionVSAM'
                }

                //bat 'python MF_Provision_Region.py vsam'
            }
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
