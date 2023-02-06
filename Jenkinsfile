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
                   echo "-- starting region BANKVSAM"
		   echo " "
                   bat 'python MF_Provision_Region.py vsam'
                   echo "-- finished"
                   echo " "
		   echo "ESCWA: http://localhost:10086"
		   echo " "
                }
		    
                if (env.TASK == "removeVSAM") {
                    echo "-- stopping region"
                    echo " "
		    powershell '''
                    (Get-Content -path MF_Region_Stop.py -Raw) -replace 'BANKDEMO','BANKVSAM' | Set-Content -Path MF_Region_Stop.py
                    '''
		    python MF_Region_Stop.py
		    powershell '''
                    (Get-Content -path MF_Region_Stop.py -Raw) -replace 'BANKVSAM','BANKDEMO' | Set-Content -Path MF_Region_Stop.py
		    '''
                    echo "-- removing region"
                    echo " "
		    
	            powershell '''
                    (Get-Content -path MF_Delete_Region.py -Raw) -replace 'BANKDEMO','BANKVSAM' | Set-Content -Path MF_Delete_Region.py
                    '''
		    python MF_Delete_Region.py
			
                    powershell '''
		    (Get-Content -path MF_Delete_Region.py -Raw) -replace 'BANKVSAM','BANKDEMO' | Set-Content -Path MF_Delete_Region.py
                    '''
			
                    echo "-- finished"
                    echo " "

                    
                    
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
