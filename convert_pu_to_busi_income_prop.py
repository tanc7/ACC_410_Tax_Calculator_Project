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

def calculate_tax_basis():
    timestr = time.strftime("%Y%m%d-%H%M%S")

    purchase_prc = float(raw_input(yellow('Enter the amount that the land was originally purchase for: ')).replace(',',''))
    current_fmv = float(raw_input(yellow('Enter the FMV that was current prior to conversion into business income producing property: ')).replace(',',''))

    if current_fmv < purchase_prc:
        tax_basis = current_fmv
    elif current_fmv > purchase_prc:
        tax_basis = purchase_prc

    string_tax_basis = 'NEW TAX BASIS FOR COST RECOVERY PURPOSES: ' + str(tax_basis)
    print green(string_tax_basis)
    saved_answer = './solutions/convert_personal_use_to_business_use_solution' + timestr + '.csv'
    w = open(saved_answer,'a+')
    w.write(string_tax_basis)
    w.close()
    main()
    return

def main():
    calculate_tax_basis()
    go_back_main_menu_module()
    return
main()
