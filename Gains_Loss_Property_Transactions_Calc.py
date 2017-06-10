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

def find_realized_gain_loss():
    timestr = time.strftime("%Y%m%d-%H%M%S")


    amt_realized = float(raw_input(yellow("Enter the amount of income realized: ")).replace(',',''))
    adj_basis = float(raw_input(yellow("Enter the adjusted basis: ")).replace(',',''))
    realized_gain_loss = amt_realized - adj_basis

    string_gain_loss = "REALIZED GAIN: " + str(realized_gain_loss)
    print green(string_gain_loss)
    saved_answer = "./solutions/gain_loss_property_trans_calc" + timestr + '.csv'
    w = open(saved_answer,'a+')
    w.write(
    string_gain_loss + '\n'
    )
    w.close()
    return

def find_amount_realized():
    timestr = time.strftime("%Y%m%d-%H%M%S")

    selling_prc = float(raw_input(yellow("Enter the selling price of the sold property: ")).replace(',',''))
    costs_dispose = float(raw_input(yellow("Enter the disposal costs of the sold property: ")).replace(',',''))
    amount_realized = selling_prc - costs_dispose

    string_amount_realized = "AMOUNT REALIZED AND TAXABLE: " + str(amount_realized)

    print green(string_amount_realized)

    saved_answer = "./solutions/gain_loss_property_trans_calc" + timestr + '.csv'
    w = open(saved_answer,'a+')
    w.write(
    string_amount_realized + '\n'
    )
    w.close()
    return

def find_adjusted_basis():
    timestr = time.strftime("%Y%m%d-%H%M%S")

    cost_buy = float(raw_input(yellow("Enter the PURCHASE PRICE of the property: ")).replace(',',''))
    capital_additions = float(raw_input(yellow("Enter the CAPITAL ADDITIONS and IMPROVEMENTS made to the property: ")).replace(',',''))
    cost_recovery = float(raw_input(yellow("Enter the COST RECOVERY available to this property: ")).replace(',',''))
    adjusted_basis = cost_buy + capital_additions - cost_recovery

    string_adjusted_basis = "ADJUSTED BASIS: " + str(adjusted_basis)
    print green(string_adjusted_basis)
    saved_answer = "./solutions/gain_loss_property_trans_calc" + timestr + '.csv'
    w = open(saved_answer,'a+')
    w.write(
    string_amount_realized + '\n'
    )
    w.close()
    return

def find_everything():
    timestr = time.strftime("%Y%m%d-%H%M%S")

    cost_buy = float(raw_input(yellow("Enter the initial purchase price of the property: ")))
    capital_additions = float(raw_input(yellow("Enter any capital additions (improvements): ")))
    cost_recovery = float(raw_input(yellow("Enter the amount of cost recovery: ")))
    selling_prc = float(raw_input(yellow("Enter the selling price at which the property was sold at: ")))
    costs_dispose = float(raw_input(yellow("Enter the disposal costs (if any): ")))


    adjusted_basis = cost_buy + capital_additions - cost_recovery
    amount_realized = selling_prc - costs_dispose
    realized_gain_loss = amt_realized - adj_basis

    string_gain_loss = "GAIN RECOGNIZED: " + str(realized_gain_loss)
    string_amount_realized = "AMOUNT REALIZED: " + str(amount_realized)
    string_adjusted_basis = "ADJUSTED BASIS: " + str(adjusted_basis)

    print green(string_gain_loss)
    print yellow(string_amount_realized)
    print yellow(string_adjusted_basis)

    saved_answer = "./solutions/gain_loss_property_trans_calc" + timestr + '.csv'
    w = open(saved_answer,'a+')
    w.write(
    "GAIN LOSS PROPERTY TRANSACTIONS " + '\n'
    string_gain_loss + '\n'
    string_amount_realized + '\n'
    string_adjusted_basis + '\n'
    )
    #w.write("LIFE INSURANCE: CANCELS POLICY AND RECEIVES SURRENDER VALUE " + '\n' + string_gain_recognized + '\n' + string_loss_not_recognized + '\n' + string_amount_received + '\n' + string_premiums_policy)
    w.close()
    return

def main():
    print """

    # 1. Find REALIZED GAIN/LOSS (taxable) from Amt Realized and Adjusted basis
    # 2. Find AMOUNT REALIZED from Selling Price and Cost to Dispose
    # 3. Find ADJUSTED BASIS from Cost and Capital Additions
    # 4. Find EVERYTHING

    """

    opt_choice = float(raw_input(yellow("Enter a OPTION: ")).replace(',',''))

    if opt_choice == 1:
        find_realized_gain_loss()
    elif opt_choice == 2:
        find_amount_realized()
    elif opt_choice == 3:
        find_adjusted_basis()
    elif opt_choice == 4:
        find_everything()
    else:
        print red('You have entered a invalid option')
        main()
    return
main()
