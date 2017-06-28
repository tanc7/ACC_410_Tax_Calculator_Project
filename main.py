#!/usr/bin/env python
# coding=UTF-8

from termcolor import colored
import os
import sys
import socket
import StringIO

os.chdir('/root/Documents/ACC_410_Exam_Calculator_Project')
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

def main():
    cyan('MAIN MENU\n\nFEDERAL TAX CLASS UTILITIES\nCHANG TAN\nACC 410\nInstructor: Donald Jones\nSemester: Summer 2017')
    print """
    # 0. Tax Calculator, for Gross Income, Taxable Income, Refunds, etc.
    # 1. Chapter 4 and 5
    # 2. Chapter 6 and 7
    # 3. Chapter 8 and 12
    # 4. Chapter 14 and 15
    """

    opt_choice = str(raw_input("Enter a OPTION: "))

    if opt_choice == "1":
        os.system('clear')
        os.system('python ./Chapter_4_5/main.py')
    elif opt_choice == "2":
        os.system('clear')
        os.system('python ./Chapter_6_7/main.py')
    elif opt_choice == "3":
        os.system('clear')
        os.system('python ./Chapter_8_12/homework_problems.py')
    elif opt_choice == "4":
        os.system('clear')
        os.system('python ./Chapter_14_15/main.py')
    elif opt_choice == "0":
        os.system('clear')
        os.system('python ./tax_calculator_general.py')
        return
    else:
        # print 'You have entered a invalid option'
        red('You have entered a invalid option')
        main()
    return
main()
