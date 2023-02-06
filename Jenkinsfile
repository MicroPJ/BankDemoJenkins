node {

    stage('Clone repository') {
        /* Let's make sure we have the repository cloned to our workspace */
        //cleanWs()
	git branch: "main",
        url: 'https://github.com/MicroFocus/BankDemo.git'
    }

    stage('Provision VSAM') {
        dir("scripts") {
            script {
                if (env.TASK == "Provision BANKVSAM") {
		   dir ('BANKVSAM') {
		       deleteDir()
		   }
		   echo "-- starting region BANKVSAM"
		   echo " "
                   bat 'python MF_Provision_Region.py vsam'
                   echo "-- finished"
                   echo " "
		   echo "ESCWA: http://localhost:10086"
		   echo " "
		   //cleanWs()
                }
		    
                if (env.TASK == "Provision BANKPOSTGRES") {
		   dir ('BANKVSAM') {
		       deleteDir()
		   }
		   echo "-- starting region BANKVSAM"
		   echo " "
                   bat 'python MF_Provision_Region.py vsam_postgres'
                   echo "-- finished"
                   echo " "
		   echo "ESCWA: http://localhost:10086"
		   echo " "
		   //cleanWs()
                }
		    
                if (env.TASK == "Remove BANKVSAM") {
                    echo "-- stopping region"
                    echo " "
		    powershell '''
                    (Get-Content -path MF_Region_Stop.py -Raw) -replace 'BANKDEMO','BANKVSAM' | Set-Content -Path MF_Region_Stop.py
                    '''
		    bat 'python MF_Region_Stop.py'
		    powershell '''
                    (Get-Content -path MF_Region_Stop.py -Raw) -replace 'BANKVSAM','BANKDEMO' | Set-Content -Path MF_Region_Stop.py
		    '''
                    echo "-- removing region"
                    echo " "
		    
	            powershell '''
                    (Get-Content -path MF_Delete_Region.py -Raw) -replace 'BANKDEMO','BANKVSAM' | Set-Content -Path MF_Delete_Region.py
                    '''
		    bat 'python MF_Delete_Region.py'
			
                    powershell '''
		    (Get-Content -path MF_Delete_Region.py -Raw) -replace 'BANKVSAM','BANKDEMO' | Set-Content -Path MF_Delete_Region.py
                    '''
			
                    echo "-- finished"
                    echo " "
		    //cleanWs()                   
                }

            }
         }
    }
}
