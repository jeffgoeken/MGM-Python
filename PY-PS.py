# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import subprocess
result = subprocess.run([r'C:\WINDOWS\system32\WindowsPowerShell\\v1.0\\powershell.exe', r'.\\Untitled1.ps1'],stdout=subprocess.PIPE, stderr=subprocess.STDOUT,shell = True)
print(result.stdout.decode('utf-8'))