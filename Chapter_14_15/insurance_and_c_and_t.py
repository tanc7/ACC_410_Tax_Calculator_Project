from termcolor import colored
import os
import sys
import socket
import StringIO
import time
import operator
# os.chdir('/root/Documents/ACC_410_Exam_Calculator_Project')
os.chdir('/root/Documents/ACC_410_Exam_Calculator_Project/chapter_14_15')
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
    os.system('python /root/Documents/ACC_410_Exam_Calculator_Project/main.py')
    return

def save_solution(save_name, solution):
    timestr = time.strftime("%Y%m%d-%H%M%S")
    document_name = '/root/Documents/ACC_410_Exam_Calculator_Project/Chapter_14_15/solutions/%s_%s.csv' % (save_name, timestr)
    w = open(document_name,'a+')
    w.write(solution + '\n')
    string = "Your solution is saved as: %s" % document_name
    print yellow(string)
    w.close()
    return
    # timestr = time.strftime("%Y%m%d-%H%M%S")

def calculate_full_recovery():
    print red("NO Casualty Loss Permitted")
    print yellow("Deduct in year of settlement any amount not reimbursed")
    reimbursement = float(raw_input(yellow("Enter the reimbursement of the damaged asset: ")).replace(',','').replace('$',''))
    FMV_loss = float(raw_input(yellow("Enter the FMV loss of the damaged asset: ")).replace(',','').replace('$',''))
    deduction_not_reimbursed = FMV_loss - reimbursement

    str_solution = "DEDUCTION: Amount not reimbursed by insurance: %s from: %s - %s" % (
        str(deduction_not_reimbursed),
        str(FMV_loss),
        str(reimbursement)
        )
    print green(str_solution)

    save_solution('insurance_prospect_full_recovery',str_solution)
    return str_solution

def calculate_partial_recovery():
    print yellow("Deduct in year of loss any amount not covered\nRemainder is deducted in year claim is setted")
    FMV_asset = float(raw_input(yellow("Enter the FMV of the damaged asset: ")).replace(',','').replace('$',''))
    covered_amount = float(raw_input(yellow("Enter the COVERED AMOUNT of the damaged asset: ")).replace(',','').replace('$',''))
    deduction_amount_not_covered = FMV_asset - covered_amount
    deduction_after_settlement = covered_amount

    str_solution = "DEDUCTION: Amount NOT covered by insurance: %s from: %s - %s\nNOTE: Upon insurance settlement this amount will be deductible: %s" % (
        str(deduction_amount_not_covered),
        str(FMV_asset),
        str(covered_amount),
        str(deduction_after_settlement)
        )

    print green(str_solution)
    save_solution('partial_recovery_prospect_insurance',str_solution)
    return


def main():
    print cyan("FACTORING INSURANCE INTO CASUALTY AND THEFT LOSSES CALCULATOR")

    print """
    Is there a reasonable prospect of a...

    1. Full recovery?
    2. Partial recovery?
    0. Return to Main Menu
    """

    opt_choice = float(raw_input(yellow("Enter a OPTION: ")))

    if opt_choice == 1:
        os.system('clear')
        calculate_full_recovery()
        main()
    elif opt_choice == 2:
        os.system('clear')
        calculate_partial_recovery()
        main()
    elif opt_choice == 0:
        os.system('clear')
        go_back_main_menu_module()
    else:
        print red("You have entered a invalid option: ")
        main()

    return
main()
