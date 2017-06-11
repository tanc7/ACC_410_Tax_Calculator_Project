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
    # print """
    # # 1. Depreciation Calculator (MACRS, Bonus, and Section 179)
    # # 2. Original Issue Discount Calculator
    # # 3. Converting Personal-Use to Business Income Producing Property, Cost Recovery Calculator
    # # 4. Deathbed Gifts Calculator
    # # 5. Gifts, stock, Calculator
    # # 6. Depreciable gift property calculator
    # # 0. Return to Main Menu
    # """
def opt_1():
    os.system('python /root/Documents/ACC_410_Exam_Calculator_Project/Chapter_4_5/MACRS_calc.py')
    return

def opt_2():
    os.system('python /root/Documents/ACC_410_Exam_Calculator_Project/Chapter_4_5/OID_calc.py')
    return

def opt_3():
    os.system('python /root/Documents/ACC_410_Exam_Calculator_Project/Chapter_4_5/convert_pu_to_busi_income_prop.py')
    return

def opt_4():
    os.system('python /root/Documents/ACC_410_Exam_Calculator_Project/Chapter_4_5/imputed_interest_on_below_market_loans_calc.py')
    return

def opt_5():
    os.system('python /root/Documents/ACC_410_Exam_Calculator_Project/Chapter_4_5/charitable_contribution_calc.py')
    return

def opt_6():
    os.system('python /root/Documents/ACC_410_Exam_Calculator_Project/Chapter_4_5/Gains_Loss_Property_Transactions_Calc.py')
    return

def opt_7():
    os.system('python /root/Documents/ACC_410_Exam_Calculator_Project/Chapter_4_5/realized_gain_loss_basis_calc.py')
    return

def opt_7_a():
    os.system('python ./qual_div_calc.py')
    return

def opt_8():
    os.system('python /root/Documents/ACC_410_Exam_Calculator_Project/Chapter_4_5/investigation_business_calc.py')
    return

def opt_9():
    os.system('python /root/Documents/ACC_410_Exam_Calculator_Project/Chapter_4_5/life_insurance_proceeds_calc.py')
    return

def opt_10():
    os.system("python /root/Documents/ACC_410_Exam_Calculator_Project/Chapter_4_5/marginal_tax_rate_calculator.py")
    return

def opt_11():
    os.system("python /root/Documents/ACC_410_Exam_Calculator_Project/Chapter_4_5/tax_method_calc.py")
    return

def opt_12():
    os.system("python /root/Documents/ACC_410_Exam_Calculator_Project/Chapter_4_5/insolvency_calc.py")
    return

def opt_13():
    os.system("python /root/Documents/ACC_410_Exam_Calculator_Project/Chapter_4_5/cash_accrual_method_calc.py")
    return

def opt_14():
    os.system("python /root/Documents/ACC_410_Exam_Calculator_Project/Chapter_4_5/allowed_allowable_calc.py")
    return

def main():

    print """
    # 1. Depreciation Calculator (MACRS, Bonus, and Section 179)
    # 2. Original Issue Discount Calculator
    # 3. Converting Personal-Use to Business Income Producing Property, Cost Recovery Calculator
    # 4. Below Market Loans & Imputed Interest Calculator (Gift-Loans, Deathbed-Gifts, Corp-Shareholder, Employer-Employee Loans)
    # 5. Charitable Contribution Calculator
    # 6. Gain Loss on Property Transactions
    # 7. Capital Gain on Sale of a Bond Calculator
    # 8. Investigation of a Business Calculator
    # 9. Life Insurance Proceeds Calculator
    # 10. Marginal Tax Rate Calculator
    # 11. Tax Method Calculator
    # 12. Forgiveness from Debt by Insolvency
    # 13. Cash Method versus Accrual Method Net Profit
    # 14. Allowed versus Allowable Depreciation
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
    elif opt_choice == "10":
        os.system('clear')
        opt_10()
    elif opt_choice == "11":
        os.system('clear')
        opt_11()
    elif opt_choice == "12":
        os.system('clear')
        opt_12()
    elif opt_choice == "13":
        os.system('clear')
        opt_13()
    elif opt_choice == "14":
        os.system('clear')
        opt_14()
        return

    else:
        red('You have entered a invalid option')
        main()
    return
main()
