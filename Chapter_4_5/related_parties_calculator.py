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
    amt_borrowed = float(raw_input(yellow("Enter the amount borrowed by the entity: ")).replace(',',''))
    tax_afr = float(raw_input(yellow("Enter the Annual Federal Rate for taxation: ")).replace(',',''))
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

    green(string_borrower_int_expense + '\n' + string_borrower_comp_inc)
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

def main():
    print """
    # 1. Employer-Employee Loans
    # 2. Corporation-Shareholder Loans
    """

    opt_choice = float(raw_input(yellow("Enter a OPTION: ")).replace(',',''))

    if opt_choice == 0:
        go_back_main_menu_module()
    elif opt_choice == 1:
        employer_employee_loan()
    elif opt_choice == 2:
        corporation_shareholder_loan()
    else:
        print red('You have entered a invalid option')
        main()
    return
main()
