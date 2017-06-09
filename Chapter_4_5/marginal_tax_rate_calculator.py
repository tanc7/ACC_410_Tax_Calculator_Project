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

def calculate_average_tax_rate():
    timestr = time.strftime("%Y%m%d-%H%M%S")

    tax_liability = float(raw_input(yellow("Enter the total tax liablity that the taxpayer owes: ")).replace(',',''))
    taxable_income = float(raw_input(yellow("Enter the total taxable income as it is shown in the income tax calculator: ")).replace(',',''))
    average_tax_rate = tax_liability / taxable_income
    average_tax_rate = average_tax_rate * 100
    string_average_tax_rate = "Average Tax Rate: " + str(average_tax_rate) + '%'
    print green(string_average_tax_rate)
    saved_answer = './solutions/average_tax_rate_solution' + timestr + '.csv'
    w = open(saved_answer,'a+')
    w.write(saved_answer)
    w.close()
    main()
    return
def main():
    return
main()
