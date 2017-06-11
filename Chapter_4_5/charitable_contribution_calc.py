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

def calculate_individual_cc(charitable_contribution):
    timestr = time.strftime("%Y%m%d-%H%M%S")

    string_charitable_contribution = "CHARITABLE CONTRIBUTION-INDIVIDUAL: " + str(charitable_contribution)
    print green(string_charitable_contribution)

    saved_answer = "./solutions/charitable_contribution_individual" + timestr + '.csv'
    w = open(saved_answer,'a+')
    w.write(
    string_charitable_contribution + '\n'
    )
    w.close()


    return

def calculate_accrual_basis_corp(charitable_contribution):
    timestr = time.strftime("%Y%m%d-%H%M%S")

    Taxable_Income = float(raw_input(yellow("Enter the corporation's taxable_income: ")).replace(',',''))
    charitable_contribution_deduction = charitable_contribution
    # charitable_contribution_deduction = float(raw_input(yellow("Enter your charitable charitable_contribution_deduction")).replace(',',''))
    NOL_and_CL_carryback = float(raw_input(yellow("")).replace(',',''))
    dividends_received_deduction = float(raw_input(yellow("")).replace(',',''))

    domestic_production_activities_deduction = 0 # for this exam

    deduction_limit = (0.1 * taxable_income) - charitable_contribution_deduction - NOL_and_CL_carryback - dividends_received_deduction - domestic_production_activities_deduction

    excess_cc = charitable_contribution_deduction - deduction_limit
    excess_cc_annually = excess_cc / 5

    elect_question_preceding_year = str(raw_input(yellow("Have you made a election to deduct in the preceding year AND paid ON or BEFORE April 15t this year?: ")).replace(',',''))

    if elect_question_preceding_year == "n":
        string_instant_deductible_cc = "CURRENT YEAR Instant-Deductible (CORPORATE) through Charitable Contribution: " + deduction_limit + '\n' + "EXCESS Charitable Contribution to be deducted annually: " + excess_cc_annually
    elif elect_question_preceding_year == "y":
        string_instant_deductible_cc = "PRECEDING YEAR Instant-Deductible (CORPORATE) through Charitable Contribution: " + deduction_limit + '\n' + "EXCESS Charitable Contribution to be deducted annually: " + excess_cc_annually
    else:
        print red("Please enter 'y' or 'n'")
        calculate_accrual_basis_corp(charitable_contribution)
    print green(string_instant_deductible_cc)

    saved_answer = "./solutions/charitable_contribution_corporate" + timestr + '.csv'
    w = open(saved_answer,'a+')
    w.write(
    string_instant_deductible_cc + '\n' + Taxable_Income + '\n' + charitable_contribution_deduction + '\n' + NOL_and_CL_carryback + '\n' + dividends_received_deduction + '\n'
    )
    w.close()

    return

def calculate_corp_cash_basis(charitable_contribution):
    timestr = time.strftime("%Y%m%d-%H%M%S")

    Taxable_Income = float(raw_input(yellow("Enter the corporation's taxable_income: ")).replace(',',''))
    charitable_contribution_deduction = charitable_contribution


    # charitable_contribution_deduction = float(raw_input(yellow("")).replace(',',''))
    NOL_and_CL_carryback = float(raw_input(yellow("")).replace(',',''))
    dividends_received_deduction = float(raw_input(yellow("")).replace(',',''))

    domestic_production_activities_deduction = 0 # for this exam

    deduction_limit = (0.1 * taxable_income) - charitable_contribution_deduction - NOL_and_CL_carryback - dividends_received_deduction - domestic_production_activities_deduction

    excess_cc = charitable_contribution_deduction - deduction_limit
    excess_cc_annually = excess_cc / 5

    string_instant_deductible_cc = "CURRENT YEAR INSTANT-DEDUCTIBLE (CORPORATE) through Charitable Contribution: " + deduction_limit + '\n' + "EXCESS Charitable Contribution to be deducted annually: " + excess_cc_annually
    print green(string_instant_deductible_cc)

    saved_answer = "./solutions/charitable_contribution_corporate" + timestr + '.csv'
    w = open(saved_answer,'a+')
    w.write(
    string_instant_deductible_cc + '\n' + Taxable_Income + '\n' + charitable_contribution_deduction + '\n' + NOL_and_CL_carryback + '\n' + dividends_received_deduction + '\n'
    )
    w.close()
    return charitable_contribution

def main_ctnd(charitable_contribution):
    # charitable_contribution = cash_and_property - tangible_benefit + ordinary_noncash
    debug = "DEBUG: charitable_contribution = %s" % str(charitable_contribution)
    print red(debug)
    if cash_and_property < 250:
        print cyan("You require a receipt for substantiation purposes on your Cash & Property Contributions: ")
    elif 250 <= cash_and_property < 500:
        print cyan("You require a acknowledgement from the Qualified Organization for substantiation purposes  on your Cash & Property Contributions: ")
    elif cash_and_property >= 500:
        print cyan("You require a Form 8283 for substantiation purposes  on your Cash & Property Contributions: ")

    print """
    Are you a...

    1. Individual taxpayer?
    2. Accrual basis CORPORATION?
    3. Corporate taxpayer (cash-basis)?
    """
    tax_accounting_method_question = float(raw_input(yellow("")).replace(',',''))

    if tax_accounting_method_question == 2:
        accrual_basis_corp = True
        corporate = True
    elif tax_accounting_method_question == 3:
        accrual_basis_corp = False
        corporate = True
    else:
        accrual_basis_corp = False
        corporate = False

    if accrual_basis_corp == False and corporate == False:
        calculate_individual_cc(charitable_contribution)
    elif accrual_basis_corp == True and corporate == True:
        calculate_accrual_basis_corp(charitable_contribution)
    elif accrual_basis_corp == False and corporate == True:
        calculate_corp_cash_basis(charitable_contribution)
    return charitable_contribution
def main():
    charitable_contribution = 0
    print """
    Are you a...

    Individual or a Corporation? Donating to a...
    qualified organization?
    and
    Retain only donative intent and nothing more?
    """
    individual_corp_question = str(raw_input(yellow("'y' or 'n': ")).replace(',',''))
    print """
    Are you receiving a tangible benefit?
    """
    tangible_benefit = float(raw_input(yellow("Enter the FMV amount of tangible benefits you are receiving (if any): ")).replace(',',''))

    if individual_corp_question == "y":
        if tangible_benefit == '':
            tangible_benefit = 0
        else:
            tangible_benefit = tangible_benefit
    else:
        print red('You cannot make a charitable contribution')
        main()
    cash_and_property = float(raw_input(yellow("Enter cash and property contributed, NOT SECTION 1231 ASSETS: ")).replace(',',''))
    basis_ordinary_income_and_non_cash = float(raw_input(yellow("Enter the tax basis of Ordinary Income and Non-Cash properties that were contributed: ")).replace(',',''))
    fmv_ordinary_income_and_non_cash = float(raw_input(yellow("Enter the FMV of Ordinary Income and Non-Cash properties that were contributed: ")).replace(',',''))

    if basis_ordinary_income_and_non_cash < fmv_ordinary_income_and_non_cash:
        ordinary_noncash = basis_ordinary_income_and_non_cash
        charitable_contribution = cash_and_property - tangible_benefit + ordinary_noncash
        # main_ctnd(charitable_contribution)
    elif basis_ordinary_income_and_non_cash > fmv_ordinary_income_and_non_cash:
        ordinary_noncash = fmv_ordinary_income_and_non_cash
        charitable_contribution = cash_and_property - tangible_benefit + ordinary_noncash
        # main_ctnd(charitable_contribution)
    # charitable_contribution = cash_and_property - tangible_benefit + ordinary_noncash
    debug = "DEBUG: charitable_contribution = %s" % str(charitable_contribution)
    # print red(debug)
    if cash_and_property < 250:
        print cyan("You require a receipt for substantiation purposes on your Cash & Property Contributions: ")
    elif 250 <= cash_and_property < 500:
        print cyan("You require a acknowledgement from the Qualified Organization for substantiation purposes  on your Cash & Property Contributions: ")
    elif cash_and_property >= 500:
        print cyan("You require a Form 8283 for substantiation purposes  on your Cash & Property Contributions: ")

    print """
    Are you a...

    1. Individual taxpayer?
    2. Accrual basis CORPORATION?
    3. Corporate taxpayer (cash-basis)?
    """
    tax_accounting_method_question = float(raw_input(yellow("")).replace(',',''))

    if tax_accounting_method_question == 2:
        accrual_basis_corp = True
        corporate = True
    elif tax_accounting_method_question == 3:
        accrual_basis_corp = False
        corporate = True
    else:
        accrual_basis_corp = False
        corporate = False

    if accrual_basis_corp == False and corporate == False:
        calculate_individual_cc(charitable_contribution)
        main()
    elif accrual_basis_corp == True and corporate == True:
        calculate_accrual_basis_corp(charitable_contribution)
        main()
    elif accrual_basis_corp == False and corporate == True:
        calculate_corp_cash_basis(charitable_contribution)
        main()
    return charitable_contribution
main()
