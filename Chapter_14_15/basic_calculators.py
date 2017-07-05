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
    # timestr = time.strftime("%Y%m%d-%H%M%S")
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

def c_and_t_deductibility_calc():
    print """
    Is this item a...

    1. Casualty?
    2. Theft?
    """
    return
def effects_insur_proceeds_recovery_deductible():
    print """
    Is the likelihood of a reasonable prospect of recovery a...

    1. Full recovery?
    2. Partial recovery?
    """

    opt_choice = float(raw_input(yellow("Enter ANNUAL SALARY: ")).replace(',','').replace('$','').replace('%',''))

    if opt_choice == 1:
        FMV_asset = float(raw_input(yellow("Enter ANNUAL SALARY: ")).replace(',','').replace('$','').replace('%',''))
        reimbursement = float(raw_input(yellow("Enter ANNUAL SALARY: ")).replace(',','').replace('$','').replace('%',''))
        full_recovery_deductible = FMV_asset - reimbursement

    elif opt_choice == 2:
        covered_amount = float(raw_input(yellow("Enter ANNUAL SALARY: ")).replace(',','').replace('$','').replace('%',''))
        not_covered_amt = float(raw_input(yellow("Enter ANNUAL SALARY: ")).replace(',','').replace('$','').replace('%',''))
        partial_recovery_deductible = covered_amount - not_covered_amt

    return

def casualty_loss_calculator():
    print """
    Is the casualty loss...

    1. Completely lost?
    2. Partially lost?
    """

    opt_choice = float(raw_input(yellow("Enter ANNUAL SALARY: ")).replace(',','').replace('$','').replace('%',''))

    if opt_choice == 1:
        adjusted_basis_asset = float(raw_input(yellow("Enter ANNUAL SALARY: ")).replace(',','').replace('$','').replace('%',''))
        insurance_proceeds = float(raw_input(yellow("Enter ANNUAL SALARY: ")).replace(',','').replace('$','').replace('%',''))
        complete_casualty_deduction = adjusted_basis_asset - insurance_proceeds

    elif opt_choice == 2:
        decline_val = float(raw_input(yellow("Enter ANNUAL SALARY: ")).replace(',','').replace('$','').replace('%',''))
        adjusted_basis_asset = float(raw_input(yellow("Enter ANNUAL SALARY: ")).replace(',','').replace('$','').replace('%',''))
        if decline_val < adjusted_basis_asset:
            subtract_from = decline_val

        if adjusted_basis_asset < decline_val:
            subtract_from = adjusted_basis_asset

        partial_casualty_deduction = subtract_from - insurance_proceeds_collected
    return

def nonpersonal_c_and_t_and_gains_calc():
    insurance_proceeds_collected = float(raw_input(yellow("Enter ANNUAL SALARY: ")).replace(',','').replace('$','').replace('%',''))
    adjusted_basis_asset = float(raw_input(yellow("Enter ANNUAL SALARY: ")).replace(',','').replace('$','').replace('%',''))
    ordinary_or_cap_gain_loss = insurance_proceeds_collected - adjusted_basis_asset
    return

def personal_use_c_and_t_loss_calc():
    decline_fmv = float(raw_input(yellow("Enter ANNUAL SALARY: ")).replace(',','').replace('$','').replace('%',''))
    adjusted_basis_asset = float(raw_input(yellow("Enter ANNUAL SALARY: ")).replace(',','').replace('$','').replace('%',''))
    insurance_proceeds_collected = float(raw_input(yellow("Enter ANNUAL SALARY: ")).replace(',','').replace('$','').replace('%',''))
    annual_AGI = float(raw_input(yellow("Enter ANNUAL SALARY: ")).replace(',','').replace('$','').replace('%',''))

    if decline_fmv < adjusted_basis_asset:
        subtract_from = decline_fmv
    elif adjusted_basis_asset < decline_fmv:
        subtract_from = adjusted_basis_asset

    loss_amount = subtract_from - insurance_proceeds_collected
    loss_amount = loss_amount - 100
    loss_amount = loss_amount - (0.1 * annual_AGI) # itemized dedction not subject to the 2% of AGI floor? What does that ean
    return

def amount_realized_from_disposition_calc():
    fmv_asset = float(raw_input(yellow("Enter FMV reduced by selling expenses: ")).replace(',','').replace('$','').replace('%',''))
    property_taxes_seller_to_buyer = float(raw_input(yellow("Enter PROPERTY TAXES imposed on seller paid to buyer: ")).replace(',','').replace('$','').replace('%',''))
    selling_expenses = float(raw_input(yellow("Enter ANNUAL SALARY: ")).replace(',','').replace('$','').replace('%',''))
    fmv_assumed_or_takes = fmv_asset - selling_expenses
    amount_realized_from_disposition = fmv_assumed_or_takes + property_taxes_seller_to_buyer
    return

def adjusted_basis_calc():
    original_cost_or_other_ab = float(raw_input(yellow("Enter ANNUAL SALARY: ")).replace(',','').replace('$','').replace('%',''))
    capital_additions = float(raw_input(yellow("Enter ANNUAL SALARY: ")).replace(',','').replace('$','').replace('%',''))
    capital_recoveries = float(raw_input(yellow("Enter ANNUAL SALARY: ")).replace(',','').replace('$','').replace('%',''))
    adjusted_basis = original_cost_or_other_ab + capital_additions - capital_recoveries
    return
def main():
    print """
    Chapter 6 Calculators:

    # 1. Casualty and Theft Losses Deductibility
    # 2. Effects of Insurance Proceeds Collection, prospects of recovery, and deductibles
    # 3. Casualty loss calculator
    # 4. Nonpersonal C&T Gains Calculator
    # 5. Personal-Use Property C&T Loss Calculator

    Chapter 7 Calculators:

    # [number] Realized Gain or Loss Calculator
    # Amount Realized from Disposition Calculator
    # Adjusted Basis Calculator
    # Going Concern Purchase Calculator
    # Bargain Purchase Calculator
    # Gift Basis Calculator
    # Property Acquired from Decedent Calculator
    # Deathbed Gifts Calculator
    # Wash Sale Penalty Calculator
    # Disallowed Losses Calculator
    # Section 1031, Like-Kind Exchanges Calculator
    # --> Boot Calculator
    # Non-Recognition on Sale of Residence Calculator (Sections 121 & 1041)
    """

    opt_choice = float(raw_input(yellow("Enter ANNUAL SALARY: ")).replace(',','').replace('$','').replace('%',''))

    if opt_choice == 1:
        c_and_t_deductibility_calc()
    elif opt_choice == 2:
        effects_insur_proceeds_recovery_deductible()
    elif opt_choice == 3:
        casualty_loss_calculator()
    elif opt_choice == 4:
        nonpersonal_c_and_t_and_gains_calc()
    elif opt_choice == 5:
        personal_use_c_and_t_loss_calc()
    return
main()
