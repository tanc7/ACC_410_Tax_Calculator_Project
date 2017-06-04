#!/usr/bin/env python
# coding=UTF-8
import os
import socket
import operator
from termcolor import colored
import sys
import StringIO
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=64, cols=200)) # sets window to full screen

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

#
# Gross_Income = Income - Exclusions
# Taxable_Income = Gross_Income - Deductions
# TI_FTR = Taxable_Income * Tax_Rate
# Tax_Owed_Or_Refunded = TI_FTR - Tax_Credits

def find_ti_ftr():
    return

def find_gross_income(): # Tested works
    Income = int(raw_input("Enter Income: "))
    Exclusions = int(raw_input("Enter Exclusions: "))
    Gross_Income = Income - Exclusions
    Gross_Income = str(Gross_Income)
    green('Gross Income: ' + Gross_Income)
    return Gross_Income

def find_taxable_income():

    Taxable_Income = Gross_Income - Deductions

    return

def find_tax_owed_or_refunded():
    return

# Gross_Income = Income - Exclusions
# Taxable_Income = Gross_Income - Deductions
# TI_FTR = Taxable_Income * Tax_Rate
# Tax_Owed_Or_Refunded = TI_FTR - Tax_Credits
def main():
    print """
    # 0. Return to Main MENU
    # 1. Find GROSS Income
    # 2. Find TAXABLE Income
    # 3. Find TAX OWED BEFORE TAX Credits
    # 4. Find TAX OWED OR REFUNDED

    ### FIND OTHER VARIABLES ###

    # 5. Find EXCLUSIONS
    # 6. Find INCOME
    # 7. Find DEDUCTIONS
    # 8. Find TAX RATE
    # 9. Find TAX CREDITS
    """
    opt_choice = str(raw_input("Enter a OPTION: "))

    # Income = int(raw_input("Enter Income: "))
    # Exclusions = int(raw_input("Enter Exclusions: "))
    # Deductions = int(raw_input("Enter Deductions: "))
    # Tax_Rate = int(raw_input("Enter Tax Rate, this will be replaced with a auto-calculator soon: "))
    # Tax_Credits = int(raw_input("Enter Tax Credits: "))


    if opt_choice == "1":
        find_gross_income()
    elif opt_choice == "2":
        find_taxable_income()
    elif opt_choice == "3":
        find_ti_ftr()
    elif opt_choice == "4":
        find_tax_owed_or_refunded()
    elif opt_choice == "0":
        os.system('python ./main.py')
    else:
        main()
    return
main()
