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
    print string
    return string
def green(string):
    string = colored(string,'green',attrs=['bold'])
    print string
    return string
def yellow(string):
    string = colored(string,'yellow',attrs=['bold'])
    print string
    return string
def cyan(string):
    string = colored(string,'cyan',attrs=['bold'])
    print string
    return string

def go_back_main_menu_module():
    os.system('python /root/Documents/ACC_410_Exam_Calculator_Project/Chapter_4_5/main.py')
    return

def ask_user_input_float(var_name, string): # apparently this code doesnt work
    var_name = float(raw_input(cyan(string)).replace(',',''))
    return

def calculate_answer(paid_oid, effective_int_rate_cd, maturity_amt, months_to_maturity):
    years_to_maturity = months_to_maturity / 12
    effective_int_rate_cd = effective_int_rate_cd / 100
    print 'YEARS TO MATURITY: ' + str(years_to_maturity)
    # year one
    y_1_taxable_income = effective_int_rate_cd * paid_oid
    print 'YEAR ONE TAXABLE INCOME: ' + str(y_1_taxable_income)
    y_2_taxable_income = effective_int_rate_cd * (paid_oid + y_1_taxable_income)
    print 'YEAR TWO TAXABLE INCOME: ' + str(y_2_taxable_income)
    main()
    return
def gather_var():
    paid_oid = float(raw_input(cyan('Enter the amount paid as a Original Issue Discount: ')).replace(',',''))
    effective_int_rate_cd = float(raw_input(cyan('Enter the Effective Interest Rate for the Certified of Deposit: ')).replace(',','').replace('%',''))
    maturity_amt = float(raw_input(cyan('Enter the amount to receive at maturity: ')).replace(',',''))
    months_to_maturity = float(raw_input(cyan('Enter the months to maturity: ')).replace(',',''))
    calculate_answer(paid_oid, effective_int_rate_cd, maturity_amt, months_to_maturity)
    return paid_oid, effective_int_rate_cd, maturity_amt, months_to_maturity
def main():
    gather_var()
    return
main()
