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

def calculate(assets_fmv, assets_basis, entity_liabilities, Gross_Income):

    debt_cancellation = float(raw_input(yellow("Enter the DEBT CANCELLATION of the Lender: ")).replace(',',''))
    capitalloss_carryforward = float(raw_input(yellow("Enter any existing CAPITAL LOSS CARRYFORWARD by the lender: ")).replace(',',''))
    nol_carryforward = float(raw_input(yellow("Enter any existing NET OPERATING LOSS CARRYFORWARD of the lender: ")).replace(',',''))
    certain_tax_credits = float(raw_input(yellow("Enter any qualified CERTAIN TAX CREDITS of the lender: ")).replace(',',''))
    passiveloss_carryforward = float(raw_input(yellow("Enter any PASSIVE LOSS CARRYFORWARD of the lender: ")).replace(',',''))
    first_deduct = capitalloss_carryforward + nol_carryforward + certain_tax_credits + passiveloss_carryforward

    if debt_cancellation > assets_fmv:
        cancellation_income = debt_cancellation - assets_fmv

        if cancellation_income > 0:
            string_cancel_income = "CANCELLATON INCOME: %s" % str(cancellation_income)
            print green(string_cancel_income)

    # expenses = float(raw_input(yellow("")).replace(',',''))
    try:
        debt_cancellation = debt_cancellation - first_deduct
    except first_deduct == 0:
        print debt_cancellation
        print first_deduct
        pass

    string_basis_reduction = "BASIS REDUCTION: %s" % str(debt_cancellation)

    print green(string_basis_reduction)
    if debt_cancellation > 0:
        try:
            assets_basis = assets_basis - debt_cancellation
        except assets_basis == 0:
            pass

    string_new_basis = "NEW ASSETS BASIS: %s" % str(assets_basis)
    print yellow(string_new_basis)
    exit(0)

    return

def main():
    assets_fmv = float(raw_input(yellow("Enter the FMV of the Lender's Assets: ")).replace(',',''))
    assets_basis = float(raw_input(yellow("Enter the Taxable BASIS of the Lender's Assets: ")).replace(',',''))
    entity_liabilities = float(raw_input(yellow("Enter the total LIABILITIES of the Lender's Assets: ")).replace(',',''))
    Gross_Income = float(raw_input(yellow("Enter the GROSS INCOME of the Lender: ")).replace(',',''))

    if entity_liabilities > assets_fmv:
        string = "The entity is found to be INSOLVENT, proceeding to calculate deductions"
        print red(string)
        calculate(assets_fmv, assets_basis, entity_liabilities, Gross_Income)
    else:
        string = "The entity is NOT INSOLVENT, exiting"
        print yellow(string)
        exit(0)

    return
main()
