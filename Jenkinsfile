node (Built-In){

    stage('Clone repository') {
        /* Let's make sure we have the repository cloned to our workspace */

        git branch: "main",
        url: 'https://github.com/MicroFocus/BankDemo.git'
    }

    stage('Provision VSAM') {
        /* This builds the actual image; synonymous to
         * docker build on the command line */
        dir("") {
            cd scripts
            python MF_Provision_Region.py vsam
        }
    }
}
