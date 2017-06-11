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

revenue = float(raw_input(yellow("Enter the total REVENUES: ")).replace(',',''))
expenses = float(raw_input(yellow("Enter the total EXPENSES: ")).replace(',',''))
net_ar = float(raw_input(yellow("Enter the NET ACCOUNTS RECEIVABLES: ")).replace(',',''))
net_ap = float(raw_input(yellow("Enter the NET ACCOUNTS PAYABLES: ")).replace(',',''))


profit_cash_method = revenue - expenses
net_receivables_payables = net_ar - net_ap
profit_accrual_method = profit_cash_method + net_receivables_payables

string_profit_cash = "Profit CASH METHOD: %s" % str(profit_cash_method)
string_profit_accrual = "Profit ACCRUAL METHOD: %s" % str(profit_accrual_method)

print green(string_profit_cash)
print green(string_profit_accrual)
