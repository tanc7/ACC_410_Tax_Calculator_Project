import os
import socket
import sys
import operator

print "Installer for ACC 410 Tax Calculator\nChang Tan\nAccounting 410\nDonald Jones' Class\nSummer 2017\ntanc7@unlv.nevada.edu"
print """

All rights NOT RESERVED
GNU Copyleft License
Python 2.7.13

You may do with this, as you wish
Modify it, fork it, put it up your butt, idc.

If you got coding talent, take a shot and modify it and re-release it.
"""
github_URL = "https://github.com/tanc7/ACC_410_Tax_Calculator_Project"
installation_dir = "/root/Documents/ACC_410_Exam_Calculator_Project"
temp_dir = "/tmp"

print "BUILDING MAIN DIRECTORY %s" % installation_dir
os.system("mkdir %s") % installation_dir
print "GIT CLONING LATEST VERSION OF ACC_410_TAX_CALCULATOR"
os.chdir(temp_dir)
cmd_string = "git clone %s" % github_URL
os.system(cmd_string)
os.chdir('./ACC_410_Tax_Calculator_Project')
print "INSTALLING"
cmd_string = "cp -r ./* %s" % installation_dir
os.system(cmd_string)
cmd_string = "chmod 777 %s" % installation_dir
os.system(cmd_string)
print "INSTALLING REQUIRED PYTHON MODULES"
os.system("pip install termcolor")
os.system("pip install StringIO")
print "INSTALLING MAIN EXECUTABLE"
os.system("cp -r /root/Documents/ACC_410_Exam_Calculator_Project/main.py /usr/local/bin/Accounting_410_Tax_Calculator.py")

print "STARTING TAX CALCULATOR"
print "Installation Complete, to run this again, open a terminal and type \n\n\t\t'Accounting_410_Tax_Calculator.py'"

os.system("Accounting_410_Tax_Calculator.py")
print "Installation Complete, to run this again, open a terminal and type \n\n\t\t'Accounting_410_Tax_Calculator.py'"
