from termcolor import colored
import os
import sys
import socket
import StringIO
import time
import operator
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

def ask_questions():
    corp_question = str(raw_input("Is the entity a corporation excl S-Corps?: "))
    part_corp_question = str(raw_input("Is the entity a partnership that has corporate partners?: "))
    busi_tp_inv_question = str(raw_input("Is it a business taxpayer with inventory?: "))
    inv_to_income_question = str(raw_input("Is inventory sold to generate income?: "))
    tax_shelter_q = str(raw_input("Is the entity a tax shelter?: "))
    if corp_question or part_corp_question or busi_tp_inv_question or inv_to_income_question or tax_shelter_q == "y":
        red('ACCRUAL METHOD IS MANDATORY')
    else:
        red('Accrual Method not mandatory, but you will need to elect alternative methods in your tax return')

    farmer_q = str(raw_input("Is the entity a farmer?: "))
    qualified_pers_serv_q = str(raw_input("Is it a 'Qualified Personal Service Corporation' such as Lawyers and Architects?: "))
    gross_recv_q = str(raw_input("In the last 3 years, is the average gross receipts below or equal to $5 million?: "))

    if gross_recv_q == "y":
        tax_shelter_q = str(raw_input("Is the entity NOT a tax shelter?: "))
        if tax_shelter_q == "y":
            green('Election to cash method is available')
        else:
            green('Cash Method NOT available')

    if farmer_q or qualified_pers_serv_q or gross_recv_q == "y":
        green('Election to cash method is available')
    else:
        green('Cash Method NOT available')
    construction_q = str(raw_input("Are you in the construction business?: "))
    if construction_q == "y":
        yellow('Election to PERCENTAGE OF COMPLETION METHOD is available')
    else:
        yellow('Percentage Completion Method NOT available')

    return

# def compare_results():
#     if corp_question or part_corp_question or busi_tp_inv_question or inv_to_income_question == "y":
#
#     return
def main():
    ask_questions()
    go_back_main_menu_module()
    return
main()
