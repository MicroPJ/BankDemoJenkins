#!/usr/bin/python3
"""
Copyright (C) 2010-2021 Micro Focus.  All Rights Reserved.
This software may be used, modified, and distributed 
(provided this notice is included without modification)
solely for internal demonstration purposes with other 
Micro Focus software, and is otherwise subject to the EULA at
https://www.microfocus.com/en-us/legal/software-licensing.

THIS SOFTWARE IS PROVIDED "AS IS" AND ALL IMPLIED 
WARRANTIES, INCLUDING THE IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE,
SHALL NOT APPLY.
TO THE EXTENT PERMITTED BY LAW, IN NO EVENT WILL 
MICRO FOCUS HAVE ANY LIABILITY WHATSOEVER IN CONNECTION
WITH THIS SOFTWARE.

Description:  A script to build application. 
"""

import os
import sys
import subprocess

from pathlib import Path
from utilities.output import write_log 
from utilities.misc import set_MF_environment


def build_programs():

    os_type = 'Windows'
    dataversion = 'vsam'
    set64bit = 'true'

    #determine where the Micro Focus product has been installed
    install_dir = set_MF_environment (os_type)
    if install_dir is None:
        write_log("Unable to determine COBDIR")
        sys.exit(1)

    #check that ANT_HOME is set
    ant_home = None
    if "ANT_HOME" in os.environ:
        ant_home = os.environ["ANT_HOME"]
    if ant_home == None:
        write_log("Ant not found, set ANT_HOME")
        sys.exit(1)

    #set the COBOL environment
    cobdir = str(Path(install_dir).parents[0])
    write_log('Setting COBDIR={}'.format(cobdir))
    os.environ["COBDIR"] = cobdir
    mfant_jar = os.path.join(cobdir, 'bin', 'mfant.jar')

    #ant_home - this value should be set in ANT_HOME
    ant_exe = os.path.join(ant_home, 'bin', 'ant')
 
    #set source and asset repo locations
    cwd = os.getcwd()
    build_file = os.path.join(cwd, 'ant_Build_Win_x64.xml')
    source_dir = 'C:\\ProgramData\\Jenkins\\.jenkins\\workspace\\CSP_MVP_Pipeline\\BankDemo\\sources'
    # This may a better location rather than asset_repo: everything in one place - may need change to Jenkinsfile to create loadlib dir?
    asset_repo = 'C:\\ProgramData\\Jenkins\\.jenkins\\workspace\\CSP_MVP_Pipeline\\build\\Release-jenkins-CSP_MVP_Jenkinsfile\\system\\loadlib'
    #asset_repo = 'C:\Asset_Repo\BANKDEMO\system\loadlib'

    #execute ant
    ant_cmd = [ant_exe, '-lib', mfant_jar, '-f', build_file, '-Dbasedir', source_dir, '-Dloaddir', asset_repo, '-Ddataversion', dataversion, '-D64bitset', set64bit]
    #ant_cmd = [ant_exe, '-lib', mfant_jar, '-f', build_file, '-Dbasedir', source_dir, '-Dloaddir', loadlib_dir, '-Ddataversion', dataversion, '-D64bitset', set64bit]
    useShell = True
    write_log(ant_cmd)
    
    with open('build.txt', "w") as outfile:
        subprocess.run(ant_cmd, stdout=outfile, stderr=outfile, shell=useShell, check=True)
   
if __name__ == '__main__':
    build_programs()
