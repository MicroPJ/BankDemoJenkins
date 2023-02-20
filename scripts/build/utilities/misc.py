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

Description:  Miscelaneous utility functions. 
"""

#import os
import winreg
from utilities.output import write_log 
#from pathlib import Path

def set_MF_environment (os_type):

    localMachineKey = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
    cobolKey = winreg.OpenKey(localMachineKey, r"SOFTWARE\\Micro Focus\\Visual COBOL")
    defaultVersion = winreg.QueryValueEx(cobolKey, "DefaultVersion")
    installKeyString =  r'{}\\COBOL\\Install'.format(defaultVersion[0])
    write_log('Found COBOL version: {}'.format(defaultVersion[0]))
    installKey = winreg.OpenKey(cobolKey, installKeyString)
    install_dir = winreg.QueryValueEx(installKey, "BIN")
    winreg.CloseKey(installKey)
    winreg.CloseKey(cobolKey)
    winreg.CloseKey(localMachineKey)
    return install_dir[0]

