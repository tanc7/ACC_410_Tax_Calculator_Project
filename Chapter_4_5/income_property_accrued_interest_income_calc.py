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

def ask_user_input_float(var_name, string): # apparently this code doesnt work
    var_name = float(raw_input(cyan(string)).replace(',',''))
    return

def calculate_answer(face_amount_paid, interest_rate, amount_received_from_sale, months_elapsed, cost_of_bond):
    timestr = time.strftime("%Y%m%d-%H%M%S")
    filename = './answer_income_property_accrued_interest_income' + timestr + '.csv'
    string = 'Your computed file is located here: ' + filename
    red(string)
    w = open(filename,'a+')
    interest_rate = interest_rate / 100
    accrued_int_income_recognized = (face_amount_paid * interest_rate) * (months_elapsed / 12)
    selling_prc_of_bond_less_int = amount_received_from_sale - accrued_int_income_recognized
    capital_gain_recognized_on_sale = selling_prc_of_bond_less_int - cost_of_bond

    print 'FACE AMOUNT PAID: ' + str(face_amount_paid)
    print 'INTEREST RATE: ' + str(interest_rate) + '%'
    print 'AMOUNT RECEIVED FROM SALE: ' + str(amount_received_from_sale)
    print 'MONTHS ELAPSED: ' + str(months_elapsed)
    print 'COST OF BOND: ' + str(cost_of_bond)
    os.system('clear')
    string = 'CAPITAL GAIN RECOGNIZED ON SALE: ' + str(capital_gain_recognized_on_sale)
    green(string)
    w.write(string + '\n')
    string = 'SELLING PRICE OF BOND, LESS INTEREST: ' + str(selling_prc_of_bond_less_int)
    yellow(string)
    w.write(string + '\n')
    string = 'ACCRUED INTEREST INCOME RECOGNIZED: ' + str(accrued_int_income_recognized)
    yellow(string)
    w.write(string + '\n')
    w.close()
    return

def gather_var():
    # ask_user_input_float(face_amount_paid,'Enter the face amount paid: ')
    face_amount_paid = float(raw_input(cyan('Enter the face amount paid: ')).replace(',',''))
    # ask_user_input_float('interest_rate','Enter the bond interest rate: ')
    interest_rate = float(raw_input(cyan('Enter the bond interest rate: ')).replace(',','').replace('%',''))
    # ask_user_input_float('amount_received_from_sale','Enter the amount received from the sale: ')
    amount_received_from_sale = float(raw_input(cyan('Enter the amount received from the sale: ')).replace(',',''))
    # ask_user_input_float('months_elapsed','Ener the months elapsed prior to the sale: ')
    months_elapsed = float(raw_input(cyan('Enter the months elapsed prior to the sale: ')).replace(',',''))
    # ask_user_input_float('cost_of_bond', 'Enter the cost of the bond that was originally purchased at: ')
    cost_of_bond = float(raw_input(cyan('Enter the cost of the bond that was originally purchased at: ')).replace(',',''))
    calculate_answer(face_amount_paid, interest_rate, amount_received_from_sale, months_elapsed, cost_of_bond)
    return face_amount_paid, interest_rate, amount_received_from_sale, months_elapsed
def main():
    gather_var()
    go_back_main_menu_module()
    return
main()
