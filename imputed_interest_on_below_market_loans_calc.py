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

def employer_employee_loan(): # has a 10,000 exception
    timestr = time.strftime("%Y%m%d-%H%M%S")


    imputed_interest = 0
    amt_borrowed = float(raw_input(yellow("Enter the amount borrowed by the entity: ")).replace(',',''))
    tax_afr = float(raw_input(yellow("Enter the Annual Federal Rate for taxation: ")).replace(',','').replace('%',''))
    tax_afr = tax_afr / 100

    if amt_borrowed <= 10000:
        print green('This amount is NOT to be taxed\nUntil it reaches 10,001 dollars')
    else:
        months_of_the_year_beyond_exemption = float(raw_input(yellow("Enter the number of months that the loan has exceeded the $10,000 exemption: ")).replace(',',''))
        imputed_interest = amt_borrowed * tax_afr * (months_of_the_year_beyond_exemption / 12)

    string_borrower_int_expense = "EMPLOYEE BORROWER'S INTEREST EXPENSE: " + str(imputed_interest)
    string_borrower_comp_inc = "EMPLOYEE BORROWER'S COMPENSATION INCOME: " + str(imputed_interest)
    string_lender_int_inc = "EMPLOYER LENDER'S INTEREST INCOME: " + str(imputed_interest)
    string_lender_comp_expense = "EMPLOYER LENDER'S COMPENSATION EXPENSE: " + str(imputed_interest)

    print green(string_borrower_int_expense + '\n' + string_borrower_comp_inc)
    yellow(string_lender_int_inc + '\n' + string_lender_comp_expense)
    saved_answer = './solutions/employer_employee_loan_solution' + timestr + '.csv'
    w = open(saved_answer,'a+')
    w.write(string_borrower_int_expense + '\n')
    w.write(string_borrower_comp_inc + '\n')
    w.write(string_lender_int_inc + '\n')
    w.write(string_lender_comp_expense + '\n')
    w.close()
    main()
    return

def corporation_shareholder_loan(): # no exemptions, considered "tax avoidance"
    timestr = time.strftime("%Y%m%d-%H%M%S")

    current_year_loan_amt = float(raw_input(yellow("Enter the amount of the loan for the current year")).replace(',',''))
    current_year_afr = float(raw_input(yellow("Enter the current year Annual Federal Rate: ")).replace(',',''))
    current_year_months_active = float(raw_input(yellow("Enter the months active for the loan: ")).replace(',',''))
    current_year_afr = current_year_afr / 100

    imputed_interest_current_year = current_year_loan_amt * current_year_afr * (current_year_months_active / 12)
    current_year_principle_plus_int = current_year_loan_amt + imputed_interest_current_year

    following_year_loan_amt = float(raw_input(green("Enter the FOLLOWING YEAR additional loans borrowed: ")).replace(',',''))
    following_year_afr = float(raw_input(green("Enter the FOLLOWING YEAR Annual Federal Rate: ")).replace(',',''))
    following_year_afr = following_year_afr / 100
    following_year_months_active = float(raw_input(green("Enter the FOLLOWING YEAR months active on the loan: ")).replace(',',''))

    current_year_compounded_imputed_interest = current_year_principle_plus_int * following_year_afr
    following_year_new_loan_imputed_int = following_year_loan_amt * following_year_afr * (following_year_months_active / 12)
    total_compounded_imputed_interest = current_year_loan_amt + imputed_interest_current_year + following_year_new_loan_imputed_int + following_year_new_loan_imputed_int

    borrower_total_int_exp = total_compounded_imputed_interest
    borrower_div_inc = total_compounded_imputed_interest
    lender_int_income = total_compounded_imputed_interest
    lender_div_pmt = total_compounded_imputed_interest

    string_borrower_total_int_exp = "TOTAL SHAREHOLDER BORROWER INTEREST EXPENSE: " + str(borrower_total_int_exp)
    string_borrower_total_div_inc = "TOTAL SHAREHOLDER BORROWER DIVIDEND INCOME: " + str(borrower_div_inc)
    string_lender_total_int_income = "TOTAL CORPORATION LENDER INTEREST INCOME: " + str(lender_int_income)
    string_lender_total_div_pmt = "TOTAL CORPORATION LENDER DIVIDEND PAYMENT: " + str(lender_div_pmt)

    print green(string_borrower_total_int_exp + '\n' + string_borrower_total_div_inc)
    print yellow(string_lender_total_int_income + '\n' + string_lender_total_div_pmt)

    saved_answer = './solutions/corporation_shareholder_loan_solution' + timestr + '.csv'
    w = open(saved_answer,'a+')
    w.write(string_borrower_total_int_exp + '\n')
    w.write(string_borrower_total_div_inc + '\n')
    w.write(string_lender_total_int_income + '\n')
    w.write(string_lender_total_div_pmt + '\n')
    w.close()
    main()
    return
def gift_basis_stock():
    donee_gain_basis = 0
    donee_loss_basis = 0
    donee_holding_period = 0
    timestr = time.strftime("%Y%m%d-%H%M%S")
    donor_cost = float(raw_input(yellow('Enter the cost of the donor bought stock: ')).replace(',',''))
    donor_fmv = float(raw_input(yellow('Enter the FMV of the stock currently, prior to being donated: ')).replace(',',''))
    donor_holding_period = float(raw_input(yellow('Enter the holding period in months of the donated stock until the date of donation: ')).replace(',',''))

    if donor_fmv < donor_cost:
        donee_loss_basis = donor_fmv
        donee_gain_basis = donor_cost
        donee_holding_period = 'Date of receipt of the gift'
    elif donor_fmv > donor_cost:
        donee_gain_basis = donor_cost
        donee_loss_basis = donor_cost
        donee_holding_period = donor_holding_period

    string_GAIN_basis = "Recipient's GAIN BASIS: " + str(donee_gain_basis)
    print green(string_GAIN_basis)
    string_LOSS_basis = "Recipient's LOSS BASIS: " + str(donee_loss_basis)
    print yellow(string_LOSS_basis)
    string_HOLDING_period = "Recipient's HOLDING PERIOD: " + str(donee_holding_period)
    print cyan(string_HOLDING_period)

    saved_answer = './solutions/gift_calc_stock' + timestr + '.csv'
    w = open(saved_answer,'a+')
    w.write(string_GAIN_basis + '\n')
    w.write(string_LOSS_basis + '\n')
    w.write(string_HOLDING_period + '\n')
    w.close()
    main()
    return

def depreciable_gift_property():
    donee_loss_basis = 0
    donee_gain_basis = 0
    timestr = time.strftime("%Y%m%d-%H%M%S")

    donor_basis = float(raw_input(yellow('Enter the DONOR basis in the donated property: ')).replace(',',''))
    donor_fmv = float(raw_input(yellow('Enter the DONOR FMV in the donated property: ')).replace(',',''))
    donor_useful_life = float(raw_input(yellow('Enter the DONOR remaining USEFUL LIFE in the donated property in YEARS: ')).replace(',',''))
    salvage_value = float(raw_input(yellow('Ente the anticipated SALVAGE VALUE if any: ')))

    donee_basis = donor_basis
    donee_useful_life = donor_useful_life

    if donor_basis < donor_fmv:
        donee_loss_basis = donor_basis
        donee_gain_basis = donor_fmv
    elif donor_basis > donor_fmv:
        donee_loss_basis = donor_fmv
        donee_gain_basis = donor_basis
    if salvage_value == '':
        salvage_value = 0
    elif salvage_value < 0:
        red('Error, salvage value cannot be negative')
        depreciable_gift_property()
    else:
        pass

    annual_depreciation_straight_line = (donee_basis - salvage_value) / donee_useful_life
    years_passed = float(raw_input(yellow('Enter the number of YEARS that have passed: ')))


    donee_loss_basis = float(donee_loss_basis) - float(annual_depreciation_straight_line * years_passed)

    donee_gain_basis = float(donee_gain_basis) - float(annual_depreciation_straight_line * years_passed)

    if donee_loss_basis <= 0:
        donee_loss_basis = 0
    if donee_gain_basis <= 0:
        donee_gain_basis = 0
    string_GAIN_basis = "DONEE'S GAIN BASIS: " + str(donee_gain_basis)
    string_LOSS_basis = "DONEE'S LOSS BASIS: " + str(donee_loss_basis)
    # string_HOLDING_period = "DONEE'S HOLDING PERIOD: " + str(donee_holding_period)

    print green(string_GAIN_basis)
    print red(string_LOSS_basis)

    saved_answer = './solutions/depreciable_gift_property_solution' + timestr + '.csv'
    w = open(saved_answer,'a+')
    w.write(string_GAIN_basis + '\n')
    w.write(string_LOSS_basis + '\n')
    w.close()

    main()
    return

def deathbed_gifts(): # this one requires more reading to fully understand
    timestr = time.strftime("%Y%m%d-%H%M%S")

    offspring_donor_fmv = float(raw_input(yellow('Enter the FMV from the donor offspring: ')).replace(',',''))
    offspring_donor_cost = float(raw_input(yellow('Enter the COST of the donated property to the donor: ')).replace(',',''))
    offspring_donor_basis = float(raw_input(yellow('Enter the BASIS of the donated property from the donor: ')).replace(',',''))
    donee_elder_time_living = float(raw_input(yellow('Enter the amount of years between when the donee lived and died (while holding the donated property): ')).replace(',',''))
    donee_elder_fmv_death = float(raw_input(yellow('Enter the FMV of the property at time of death: ')).replace(',',''))

    if 0 < donee_elder_time_living <= 1:
        one_year_exception = True
    else:
        one_year_exception = False

    if one_year_exception == True:
        offspring_donor_basis = offspring_donor_basis
    else:
        offspring_donor_basis = donee_elder_fmv_death

    improvements_to_property_before_death = float(raw_input(yellow('Enter the amounts of any improvements made to the property by the elder before death (and after receiving the donated property)')).replace(',',''))

    if improvements_to_property_before_death == '':
        improvements_to_property_before_death = 0

    offspring_donor_basis = offspring_donor_basis + improvements_to_property_before_death

    string_offspring_basis_after_bequeath = 'NEW BASIS FOR OFFSPRING UPON RECEIVING LAND BACK AFTER DONEE DIED: ' + str(offspring_donor_basis)

    print green(string_offspring_basis_after_bequeath)

    saved_answer = './solutions/deathbed_gifts_solution' + timestr + '.csv'
    w = open(saved_answer,'a+')
    w.write(string_offspring_basis_after_bequeath + '\n')
    w.close()
    main()
    return

def gift_loans():
    print """
    # 1. Gift basis on stock
    # 2. Depreciable gift property
    # 3. Deathbed gifts
    """

    opt_choice = float(raw_input(yellow('Enter a OPTION: ')))

    if opt_choice == 0:
        go_back_main_menu_module()
    elif opt_choice == 1:
        gift_basis_stock()
    elif opt_choice == 2:
        depreciable_gift_property()
    elif opt_choice == 3:
        deathbed_gifts()
    else:
        red('You have entered a invalid option')
        gift_loans()
    return

def main():
    print """
    # 1. Employer-Employee Loans
    # 2. Corporation-Shareholder Loans
    # 3. Gift-Loans
    """

    opt_choice = float(raw_input(yellow("Enter a OPTION: ")).replace(',',''))

    if opt_choice == 0:
        go_back_main_menu_module()
    elif opt_choice == 1:
        employer_employee_loan()
    elif opt_choice == 2:
        corporation_shareholder_loan()
    elif opt_choice == 3:
        gift_loans()
    else:
        print red('You have entered a invalid option')
        main()
    return
main()
