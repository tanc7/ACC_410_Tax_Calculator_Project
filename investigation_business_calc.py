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
    print cyan("Enter Start-Up Expenses")
    start_up_expenses = float(raw_input(yellow("Enter START-UP EXPENSES: ")).replace(',',''))
    print cyan("Has a election been made to deduct Start-Up Expenses? ")
    elect_question = str(raw_input(yellow("Enter 'y' or 'n': ")).replace(',',''))

    if elect_question == "y":
        deducted_start_up_expenses = float(raw_input(yellow("Enter the deducted Start Up Expenses: ")).replace(',',''))
        if deducted_start_up_expenses > 5000:
            deducted_start_up_expenses = 5000
        elif deducted_start_up_expenses <= 0:
            deducted_start_up_expenses = 0
    else:
        deducted_start_up_expenses = 0

    remaining_start_up_expenses = start_up_expenses - deducted_start_up_expenses
    remaining_start_up_expenses = remaining_start_up_expenses - 50000

    amortized_start_up_expenses_per_month = remaining_start_up_expenses / 180

    if amortized_start_up_expenses_per_month <= 0:
        print red("No Start-Up Expense reduction permitted, exceeded dollar for dollar limit (5,000 extra - 5,000 dollar for dollar)")
        main()

    string_deducted_start_up_expenses = "DEDUCTED START-UP EXPENSES: " + str(deducted_start_up_expenses)
    string_amortized_start_up_expenses = "AMORTIZED START-UP EXPENSES PER MONTH: " + str(amortized_start_up_expenses_per_month)

    print green(string_deducted_start_up_expenses)
    print yellow(string_amortized_start_up_expenses)

    saved_answer = "./solutions/amortized_start_up_expenses" + timestr + '.csv'
    w = open(saved_answer,'a+')
    w.write(
    "DEDUCTIBLE INVESTIGATION EXPENSES AND STARTUP EXPENSES " + '\n'
    + string_deducted_start_up_expenses + '\n'
    + string_amortized_start_up_expenses + '\n'
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
        else:
            print red('Investigation expense cannot be deducted neither directly nor as start-up expense')
            main()
    else:
        print red("You have entered a invalid option, please enter 'y' or 'n' lowercase")
        main()
    return
main()
