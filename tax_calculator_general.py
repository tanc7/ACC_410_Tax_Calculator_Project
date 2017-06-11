#!/usr/bin/env python
# coding=UTF-8

# PERSONAL WORK OF CHANG TAN
# TESTED IN KALI LINUX 4.9 & Python 2.7

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

# Gross_Income = Income - Exclusions
# Taxable_Income = Gross_Income - Deductions
# TI_FTR = Taxable_Income * Tax_Rate
# Tax_Owed_Or_Refunded = TI_FTR - Tax_Credits

Schedule_X_Dict = {

}

def determine_tax_rate():


    return

def find_TI_FTR():
    Tax_Owed_Or_Refunded = float(raw_input("Enter Tax Owed or Refunded: ").replace(',',''))
    Tax_Credits = float(raw_input("Enter Tax Credits: ").replace(',',''))
    TI_FTR = Tax_Credits + Tax_Owed_Or_Refunded
    green('Tax Owed/Refunded BEFORE Tax Credit Reduction: ' + str(TI_FTR))
    ##save_all_var(Deductions, Exclusions, Gross_Income, Income, Tax_Credits, Tax_Owed_Or_Refunded, Tax_Rate, Taxable_Income, TI_FTR)

    return

def find_gross_income(): # Tested works
    Income = float(raw_input("Enter Income: ").replace(',',''))
    Exclusions = float(raw_input("Enter Exclusions: ").replace(',',''))
    Gross_Income = Income - Exclusions
    Gross_Income = str(Gross_Income)
    green('Gross Income: ' + Gross_Income)
    w = open('./var_gross_income','w+')
    w.write(Gross_Income)
    w.close()
    return Gross_Income

def find_taxable_income():
    Gross_Income = float(raw_input("Enter Gross Income: ").replace(',',''))
    Deductions = float(raw_input("Enter Deductions: ").replace(',',''))
    Taxable_Income = Gross_Income - Deductions
    green('Taxable Income: ' + str(Taxable_Income))
    #save_all_var(Deductions, Exclusions, Gross_Income, Income, Tax_Credits, Tax_Owed_Or_Refunded, Tax_Rate, Taxable_Income, TI_FTR)

    return


def find_tax_owed_or_refunded():
    TI_FTR = float(raw_input("Enter Tax Owed/Refunded BEFORE Tax Credit Reduction: ").replace(',',''))
    Tax_Credits = float(raw_input("Enter the Tax Credits: ").replace(',',''))
    Tax_Owed_Or_Refunded = TI_FTR - Tax_Credits
    green('Tax Owed/Refunded: ' + str(Tax_Owed_Or_Refunded))
    #save_all_var(Deductions, Exclusions, Gross_Income, Income, Tax_Credits, Tax_Owed_Or_Refunded, Tax_Rate, Taxable_Income, TI_FTR)
    return

# Gross_Income = Income - Exclusions
# Taxable_Income = Gross_Income - Deductions
# TI_FTR = Taxable_Income * Tax_Rate
# Tax_Owed_Or_Refunded = TI_FTR - Tax_Credits

def find_exclusions(): # it equals income - gross income
    Income = float(raw_input("Enter the total ANY INCOME: ").replace(',',''))
    Gross_Income = float(raw_input("Enter GROSS INCOME: ").replace(',',''))
    Exclusions = Income - Gross_Income
    green('Exclusions: ' + str(Exclusions))
    #save_all_var(Deductions, Exclusions, Gross_Income, Income, Tax_Credits, Tax_Owed_Or_Refunded, Tax_Rate, Taxable_Income, TI_FTR)
    return

def find_income(): # gross income + exclusions
    Gross_Income = float(raw_input("Enter GROSS INCOME: ").replace(',',''))
    Exclusions = float(raw_input("Enter EXCLUSIONS: ").replace(',',''))
    Income = Gross_Income + Exclusions
    green('Total ANY INCOME: ' + str(Income))

    #save_all_var(Deductions, Exclusions, Gross_Income, Income, Tax_Credits, Tax_Owed_Or_Refunded, Tax_Rate, Taxable_Income, TI_FTR)
    return

def find_deductions(): # gross income minus taxable income
    Gross_Income = float(raw_input("Enter GROSS INCOME: ").replace(',',''))
    Taxable_Income = float(raw_input("Enter TAXABLE INCOME: ").replace(',',''))
    Deductions = Gross_Income - Taxable_Income
    green('DEDUCTIONS: ' + str(Deductions))
    #save_all_var(Deductions, Exclusions, Gross_Income, Income, Tax_Credits, Tax_Owed_Or_Refunded, Tax_Rate, Taxable_Income, TI_FTR)
    return
# TI_FTR = Taxable_Income * Tax_Rate
def find_tax_rate(): #TI_FTR divided by TAXABLE income
    TI_FTR = float(raw_input("Enter TAXABLE INCOME before TAX CREDITS reduction: ").replace(',',''))
    Taxable_Income = float(raw_input("Enter TAXABLE INCOME: ").replace(',',''))
    Tax_Rate = TI_FTR / Taxable_Income
    green('TAX RATE: ' + str(Tax_Rate))
    #save_all_var(Deductions, Exclusions, Gross_Income, Income, Tax_Credits, Tax_Owed_Or_Refunded, Tax_Rate, Taxable_Income, TI_FTR)
    return

def find_tax_credits(): #TI_FTR minus Tax_Owed_Or_Refunded
    TI_FTR = float(raw_input("Enter TAXABLE INCOME before TAX CREDITS reduction: ").replace(',',''))
    Tax_Owed_Or_Refunded = float(raw_input("Enter Tax Owed or Refunded: ").replace(',',''))
    Tax_Credits = TI_FTR - Tax_Owed_Or_Refunded
    green('TAX CREDITS: ' + str(Tax_Credits))
# Tax_Owed_Or_Refunded = TI_FTR - Tax_Credits
    #save_all_var(Deductions, Exclusions, Gross_Income, Income, Tax_Credits, Tax_Owed_Or_Refunded, Tax_Rate, Taxable_Income, TI_FTR)
    return
def get_all_var():
    Income = float(raw_input("Enter Income: ").replace(',',''))
    Exclusions = float(raw_input("Enter Exclusions: ").replace(',',''))
    Deductions = float(raw_input("Enter Deductions: ").replace(',',''))
    Tax_Rate = float(raw_input("Enter Tax Rate, this will be replaced with a auto-calculator soon: "))
    Tax_Rate = Tax_Rate / 100
    Tax_Credits = float(raw_input("Enter Tax Credits: ").replace(',',''))

    # saves the variables in a temporary file, will overwrite if new values are found
    yellow('Saving your data entries for: Income, Exclusions, Deductions, Tax_Rate, Tax_Credits')
    yellow('Saved')
    i = open('./var_income','w+')
    i.write(str(Income))
    i.close()
    e = open('./var_exclusions','w+')
    e.write(str(Exclusions))
    e.close()
    d = open('./var_deductions','w+')
    d.write(str(Deductions))
    d.close()
    t_rate = open('./var_tax_rate','w+')
    t_rate.write(str(Tax_Rate))
    t_rate.close()
    t_credits = open('./var_tax_credits','w+')
    t_credits.write(str(Tax_Credits))
    t_credits.close()
    find_everything(Income, Exclusions, Deductions, Tax_Rate, Tax_Credits)
    return
def find_everything(Income, Exclusions, Deductions, Tax_Rate, Tax_Credits):
    Gross_Income = Income - Exclusions
    Taxable_Income = Gross_Income - Deductions
    TI_FTR = Taxable_Income * Tax_Rate
    Tax_Owed_Or_Refunded = TI_FTR - Tax_Credits
    os.system('clear')
    green('\n\n\t\tResults\n\n')
    print "GROSS INCOME: " + str(Gross_Income)
    print "TAXABLE INCOME: " + str(Taxable_Income)
    print "TAXABLE INCOME BEFORE REDUCING BY TAX CREDITS: " + str(TI_FTR)
    print "TAX OWED OR REFUNDED: " + str(Tax_Owed_Or_Refunded)

    yellow("\n\n\t\tOTHER VARIABLES\n\n")

    print "ANY INCOME: " + str(Income)
    print "EXCLUSIONS: " + str(Exclusions)
    print "TAX RATE: " + str(Tax_Rate)
    print "TAX CREDITS: " + str(Tax_Credits)

    # saves the variables in a temporary file, will overwrite if new values are found
    yellow('Saving your data entries for: Gross Income, Taxable Income, Taxable Income BEFORE Tax Credit Reduction, Tax Owed or Refunded')
    yellow('Saved')
    g = open('./var_gross_income','w+')
    g.write(str(Gross_Income))
    g.close()
    t_income = open('./var_taxable_income','w+')
    t_income.write(str(Taxable_Income))
    t_income.close()
    t_rate = open('./var_TI_FTR','w+')
    t_rate.write(str(Tax_Rate))
    t_rate.close()
    t_o_r = open('./var_tax_owed_or_refunded','w+')
    t_o_r.write(str(Tax_Owed_Or_Refunded))
    t_o_r.close()
    return
def print_last():
    # you have to replace w+ with 'r' because otherwise the temp files get overwritten
    try:
        g = open('./var_gross_income','r').read()
        t_income = open('./var_taxable_income','r').read()
        TI_FTR = open('./var_TI_FTR','r').read()
        t_o_r = open('./var_tax_owed_or_refunded','r').read()
        i = open('./var_income','r').read()
        e = open('./var_exclusions','r').read()
        d = open('./var_deductions','r').read()
        t_rate = open('./var_tax_rate','r').read()
        t_credits = open('./var_tax_credits','r').read()

        # its the 'cat' command that sucks, it prints a new line by itself
        green('\n\n\t\tLast Variables\n\n')
        print "GROSS INCOME: " + g
        print "TAXABLE INCOME: " + t_income
        print "TAXABLE INCOME BEFORE REDUCING BY TAX CREDITS: " + TI_FTR
        print "TAX OWED OR REFUNDED: " + t_o_r

        yellow("\n\n\t\tOTHER VARIABLES\n\n")

        print "ANY INCOME: " + i
        print "EXCLUSIONS: " + e
        print "TAX RATE: " + t_rate
        print "TAX CREDITS: " + t_credits
    except Exception:
        red('Error: You need to first do #10, Find Everything, before using this!')
        main()
    return
def main():
    cyan('\tACC 410 CALCULATOR')
    green('\tPERSONAL WORK OF CHANG TAN\n\t\tTESTED IN KALI LINUX 4.9 & Python 2.7\n\t\ttanc7@unlv.nevada.edu')
    yellow('\tWARNING: I did not write this to please anyone. \n\t\tI wrote this to help pass my fucking class. \n\t\tAll bug reports will be ignored. \n\t\tFuck off.')
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
    # 10. Find EVERYTHING

    ### OTHER ###

    # 11. Print LAST CALCULATED
    """
    opt_choice = str(raw_input("Enter a OPTION: "))

    # Income = float(raw_input("Enter Income: "))
    # Exclusions = float(raw_input("Enter Exclusions: "))
    # Deductions = float(raw_input("Enter Deductions: "))
    # Tax_Rate = float(raw_input("Enter Tax Rate, this will be replaced with a auto-calculator soon: "))
    # Tax_Credits = float(raw_input("Enter Tax Credits: "))


    if opt_choice == "1":
        os.system('clear')
        find_gross_income()
        main()
    elif opt_choice == "2":
        os.system('clear')

        find_taxable_income()
        main()
    elif opt_choice == "3":
        os.system('clear')
        find_TI_FTR()
        main()

    elif opt_choice == "4":
        os.system('clear')
        find_tax_owed_or_refunded()
        main()
    elif opt_choice == "5":
        os.system('clear')
        find_exclusions()
        main()
    elif opt_choice == "6":
        os.system('clear')
        find_income()
        main()
    elif opt_choice == "7":
        os.system('clear')
        find_deductions()
        main()
    elif opt_choice == "8":
        os.system('clear')
        find_tax_rate()
        main()
    elif opt_choice == "9":
        os.system('clear')
        find_tax_credits()
        main()
    elif opt_choice == "10":
        os.system('clear')
        get_all_var()
        main()
    elif opt_choice == "11":
        os.system('clear')
        print_last()
        main()
    elif opt_choice == "0":
        os.system('python ./main.py')
    else:
        main()
    return
main()
