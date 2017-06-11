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

def main():

    print """
    Which automobile are you buying?

    1. Passenger automobile
    2. SUV that weighs more than 6,000 pouds and not more than 14,000 pounds

    """
    opt_choice = float(raw_input(yellow("Enter a OPTION: ")).replace(',',''))

    if opt_choice == 1:
        listed_property_s179_limit = 3160
    elif opt_choice == 2:
        listed_property_s179_limit = 25000
    else:
        print red('You have entered a invalid option')
        main()

    # s179_deduction = float(raw_input(yellow("Enter your Section 179 deduction: ")).replace(',',''))
    # additional_50_depr = float(raw_input(yellow("Enter your Bonus 50% ")))
    # auto_cost = float(raw_input(yellow("Enter the cost of the automobile: ")).replace(',','').replace('%',''))
    # percent_busi_use = float(raw_input(yellow("Enter the percentage of business use: ")).replace(',','').replace('%',''))
    # percent_busi_use = percent_busi_use / 100
    listed_property_50_limit = 8000

    total_deductible = listed_property_s179_limit + listed_property_50_limit

    string = "TOTAL DEDUCTIBLE YEAR ONE: %s" % total_deductible
    print green(string)
    exit(0)
    return
main()
