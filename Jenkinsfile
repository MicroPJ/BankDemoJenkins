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
		    
                if (env.TASK == "Provision BANKMFDB") {
		   dir ('BANKMFDB') {
		       deleteDir()
		   }
		   echo "-- starting region BANKMFDB"
		   echo " "
                   bat 'python MF_Provision_Region.py vsam_postgres'
                   echo "-- finished"
                   echo " "
		   echo "ESCWA: http://localhost:10086"
		   echo " "
		   //cleanWs()
                }
		
                if (env.TASK == "Provision BANKSQL") {
		   dir ('BANKMFDB') {
		       deleteDir()
		   }
		   echo "-- starting region BANKSQL"
		   echo " "
		   powershell '''
                    (Get-Content -path MF_Provision_Region.py -Raw) -replace 'PostgreSQL ANSI(x64)','PostgreSQL ODBC Driver(ANSI)' | Set-Content -Path MF_Provision_Region.py
                   '''
                   bat 'python MF_Provision_Region.py sql_postgres'
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
		    
                if (env.TASK == "Remove BANKMFDB") {
                    echo "-- stopping region"
                    echo " "
		    powershell '''
                    (Get-Content -path MF_Region_Stop.py -Raw) -replace 'BANKDEMO','BANKMFDB' | Set-Content -Path MF_Region_Stop.py
                    '''
		    bat 'python MF_Region_Stop.py'
		    powershell '''
                    (Get-Content -path MF_Region_Stop.py -Raw) -replace 'BANKMFDB','BANKDEMO' | Set-Content -Path MF_Region_Stop.py
		    '''
                    echo "-- removing region"
                    echo " "
		    
	            powershell '''
                    (Get-Content -path MF_Delete_Region.py -Raw) -replace 'BANKDEMO','BANKMFDB' | Set-Content -Path MF_Delete_Region.py
                    '''
		    bat 'python MF_Delete_Region.py'
			
                    powershell '''
		    (Get-Content -path MF_Delete_Region.py -Raw) -replace 'BANKMFDB','BANKDEMO' | Set-Content -Path MF_Delete_Region.py
                    '''
			
                    echo "-- finished"
                    echo " "
		    //cleanWs()                   
                }
		    
                if (env.TASK == "Remove BANKSQL") {
                    echo "-- stopping region"
                    echo " "
		    powershell '''
                    (Get-Content -path MF_Region_Stop.py -Raw) -replace 'BANKDEMO','BANKSQL' | Set-Content -Path MF_Region_Stop.py
                    '''
		    bat 'python MF_Region_Stop.py'
		    powershell '''
                    (Get-Content -path MF_Region_Stop.py -Raw) -replace 'BANKSQL','BANKDEMO' | Set-Content -Path MF_Region_Stop.py
		    '''
                    echo "-- removing region"
                    echo " "
		    
	            powershell '''
                    (Get-Content -path MF_Delete_Region.py -Raw) -replace 'BANKDEMO','BANKSQL' | Set-Content -Path MF_Delete_Region.py
                    '''
		    bat 'python MF_Delete_Region.py'
			
                    powershell '''
		    (Get-Content -path MF_Delete_Region.py -Raw) -replace 'BANKSQL','BANKDEMO' | Set-Content -Path MF_Delete_Region.py
                    '''
			
                    echo "-- finished"
                    echo " "
		    //cleanWs()                   
                }
            }
         }
    }
}
