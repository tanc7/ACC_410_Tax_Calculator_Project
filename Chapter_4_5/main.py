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
cyan('Chapters 4 and 5, Exam 1')

def opt_1():
    os.system('python ./realization_princ_calc.py')
    return

def opt_2():
    os.system('python ./fiscal_yr_eligibility_calc.py')
    return

def opt_3():
    os.system('python ./tax_conseq_calc.py')
    return

def opt_4():
    os.system('python ./constructive_receipt_calc.py')
    return

def opt_5():
    os.system('python ./tax_method_calc.py')
    return

def opt_6():
    os.system('python ./income_src_calc.py')
    return

def opt_7():
    os.system('python ./dividends_tax_calc.py')
    return

def opt_7_a():
    os.system('python ./qual_div_calc.py')
    return

def opt_8():
    os.system('python ./life_insurance_proceeds_calc.py')
    return

def opt_9():
    os.system('python ./discharge_cancellation_forgiveness_calc.py')
    return

def main():
    print """
    # 1. Realization Principle Calculator
    # 2. Fiscal Year Eligibility Calculator
    # 3. Tax Consequences Calculator
    # 4. Constructive Receipt Determination Calculator
    # 5. Tax Accounting Method Calculator
    # 6. Income Source Taxability Calculator
    # 7. Dividends Taxation Calculator
    #    7a. Qualified Dividend Calculator
    # 8. Life Insurance Proceeds Calculator
    # 9. Taxability of Discharge from Indebtness/Cancellation/Forgiveness of Debt Calculator
    # 0. Return to Main Menu
    """

    opt_choice = str(raw_input("Enter a OPTION: "))

    if opt_choice == "0":
        os.system('clear')
        go_back_main_menu_module()
        return
    elif opt_choice == "1":
        os.system('clear')
        opt_1()
        return
    elif opt_choice == "2":
        os.system('clear')
        opt_2()
        return
    elif opt_choice == "3":
        os.system('clear')
        opt_3()
        return
    elif opt_choice == "4":
        os.system('clear')
        opt_4()
        return
    elif opt_choice == "5":
        os.system('clear')
        opt_5()
        return
    elif opt_choice == "6":
        os.system('clear')
        opt_6()
        return
    elif opt_choice == "7":
        os.system('clear')
        opt_7()
        return
    elif opt_choice == "8":
        os.system('clear')
        opt_8()
        return
    elif opt_choice == "9":
        os.system('clear')
        opt_9()
        return

    else:
        red('You have entered a invalid option')
        main()
    return
main()
