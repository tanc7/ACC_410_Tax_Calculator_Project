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

def costs():
    Expenses = float(raw_input("Enter the total EXPENSES to build property: ").replace(',',''))
    costs == True
    return Expenses

def FMV():
    FMV = float(raw_input("Enter the FMV after the property is completed: ").replace(',',''))
    return FMV
def sold():
    question = str(raw_input("Has the property actually been SOLD?!? Y or N: "))

    if question == "Y" or "y":
        return True
    elif question == "N" or "n":
        return False
    else:
        red('You have entered a invalid option')
        sold()
    return


def Find_Gain(FMV, Expenses):
    Taxable_Income = FMV - Expenses
    return Taxable_Income

Realized = False
def main():

    Expenses = float(raw_input("Enter the total EXPENSES to build property: ").replace(',',''))
    FMV = float(raw_input("Enter the FMV after the property is completed: ").replace(',',''))
    question = str(raw_input("Has the property actually been SOLD?!? Y or N: "))
    string = 'DEBUG: Value Entered = %s' % question

    # this is correct
    yellow(string)
    Taxable_Income = Find_Gain(FMV, Expenses)

    if question == "Y":
        # but this is NOT correct it automatically stays true for no dumb reason
        # sold = True
        # Realized = True
        # print sold, Realized
        string = '$%s REALIZED GAIN, TAXABLE' % Taxable_Income
        green(string)
        go_back_main_menu_module()
    elif question == "N":
        # sold = False
        # Realized = False
        # print sold, Realized
        string = '$%s UN-REALIZED GAIN, TAXABLE' % Taxable_Income
        red(string)
        go_back_main_menu_module()
            # if Expenses == True and FMV == True and sold == True:
    # if sold == True:
    #     Realized = True
    # elif sold == False:
    #     Realized = False
    # Taxable_Income = Find_Gain(FMV, Expenses)
    #
    # if Realized:
    #     string = '$%s REALIZED GAIN, TAXABLE' % Taxable_Income
    #     green(string)
    #     go_back_main_menu_module()
    # elif Realized == False:
    #     string = '$%s NOT REALIZED GAIN, NOT TAXABLE' % Taxable_Income
    #     red(string)
    #     go_back_main_menu_module()

    return
main()
