from termcolor import colored
import os
import sys
import socket
import StringIO
import time
import operator
# os.chdir('/root/Documents/ACC_410_Exam_Calculator_Project')
os.chdir('/root/Documents/ACC_410_Exam_Calculator_Project/Chapter_4_5')
def red(string):
    string = colored(string,'red',attrs=['bold'])

    return string
def green(string):
    string = colored(string,'green',attrs=['bold'])

    return string
def yellow(string):
    string = colored(string,'yellow',attrs=['bold'])

    return string
def cyan(string):
    string = colored(string,'cyan',attrs=['bold'])

    return string

def go_back_main_menu_module():
    os.system('python /root/Documents/ACC_410_Exam_Calculator_Project/Chapter_4_5/main.py')
    return
    # timestr = time.strftime("%Y%m%d-%H%M%S")

basis = float(raw_input(yellow("Enter the BASIS of the asset: ")).replace(',',''))
allowed_cr = float(raw_input(yellow("Enter the allow-ED cost recovery amount across the property's useful life: ")).replace(',',''))
allowable_cr = float(raw_input(yellow("Enter the allow-ABLE across the property's useful life: ")).replace(',',''))

if allowed_cr <= allowable_cr:
    allowed_cr = allowable_cr

new_basis = basis - allowable_cr
if new_basis <= 0:
    new_basis = 0

string_new_basis = "NEW BASIS OF ITEM: " + str(new_basis)

print green(string_new_basis)
