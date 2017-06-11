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

def calculate_deductible_cb():
    print green("DEDUCTION ALLOWED IN YEAR PAID OR INCURRED")
    inv_exp = float(raw_input(yellow("Enter INVESTIGATION EXPENSES: ")).replace(',',''))

    str_inv_exp = "INVESTIGATION EXPENSES: " + str(inv_exp)

    print green(str_inv_exp)

    main()
    return

def calculate_start_up_expenses():
    timestr = time.strftime("%Y%m%d-%H%M%S")
    print cyan("Enter Start-Up Expenses")
    start_up_expenses = float(raw_input(yellow("Enter START-UP EXPENSES: ")).replace(',',''))
    print cyan("Has a election been made to deduct Start-Up Expenses? ")
    elect_question = str(raw_input(yellow("Enter 'y' or 'n': ")).replace(',',''))

    if elect_question == "y":
        remaining_start_up_expenses = start_up_expenses - 5000
        immediate_deduction = 5000
    else:
        remaining_start_up_expenses = start_up_expenses
        immediate_deduction = 0

    annual_amortization_start_up_expenses = remaining_start_up_expenses / 15
    monthly_amortization_start_up_expenses = remaining_start_up_expenses / 180

    if annual_amortization_start_up_expenses < 0:
        annual_amortization_start_up_expenses = 0
    if monthly_amortization_start_up_expenses < 0:
        monthly_amortization_start_up_expenses = 0

    string_deducted_start_up_expenses = "IMMEDIATE DEDUCTED START-UP EXPENSES: " + str(immediate_deduction)
    string_monthly_amortized_start_up_expenses = "AMORTIZED START-UP EXPENSES PER MONTH: " + str(monthly_amortization_start_up_expenses)
    string_annual_amortized_start_up_expenses = "AMORTIZED START-UP EXPENSES PER YEAR: " + str(annual_amortization_start_up_expenses)


    print green(string_deducted_start_up_expenses)
    print yellow(string_monthly_amortized_start_up_expenses)
    print cyan(string_annual_amortized_start_up_expenses)

    saved_answer = "./solutions/amortized_start_up_expenses" + timestr + '.csv'
    w = open(saved_answer,'a+')
    w.write(
    "DEDUCTIBLE INVESTIGATION EXPENSES AND STARTUP EXPENSES " + '\n'
    + string_deducted_start_up_expenses + '\n'
    + string_monthly_amortized_start_up_expenses + '\n'
    + string_annual_amortized_start_up_expenses + '\n'
    )
    w.close()
    return


def main():
    print cyan("Is the taxpayer's current business the same as the business being investigated for purchase?")
    current_business = False
    nature_business = False
    extent_investigation = False
    acquisition_event = False
    business_involvement_question = str(raw_input(yellow("Enter 'y' or 'n': ")).replace(',',''))
    print cyan("Has the business been acquired?")
    acquisition_event_question = str(raw_input(yellow("Enter 'y' or 'n': ")).replace(',',''))
    if business_involvement_question == "y":
        current_business = True
    elif business_involvement_question == "n":
        current_business = False

    if acquisition_event_question == "y":
        acquisition_event = True
    elif acquisition_event_question == "n":
        acquisition_event = False

    if current_business == True:
        calculate_deductible_cb()
    elif current_business == False:
        if acquisition_event == True:
            print yellow("Investigation expense cannot be deducted, please proceed to startup expenses")
            calculate_start_up_expenses()
            go_back_main_menu_module()
        else:
            print red('Investigation expense cannot be deducted neither directly nor as start-up expense')
            main()
    else:
        print red("You have entered a invalid option, please enter 'y' or 'n' lowercase")
        main()
    return
main()
