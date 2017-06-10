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



def paid_solely():
    print green("This payment is entirely tax exempt")
    main()
    return

def cancels_policy_receives_surrender():
    timestr = time.strftime("%Y%m%d-%H%M%S")
    amount_received = float(raw_input(yellow("Enter the amount received from cash surrender value: ")).replace(',',''))
    premiums_paid_on_policy = float(raw_input(yellow("Enter the total premiums paid on the policy that is cancelled: ")).replace(',',''))
    gain_recognized_or_lost = amount_received - premiums_paid_on_policy

    string_gain_recognized = "GAIN RECOGNIZED: " + str(gain_recognized_or_lost)
    string_loss_not_recognized = "LOSS IS NEVER RECOGNIZED"
    string_amount_received = "DATA ENTRY-AMOUNT RECEIVED: " + str(amount_received)
    string_premiums_policy = "DATA ENTRY-PREMIUMS PAID ON POLICY: " + str(premiums_paid_on_policy)

    print green(string_gain_recognized)
    print red(string_loss_not_recognized)
    print yellow(string_amount_received)
    print yellow(string_premiums_policy)

    saved_answer = "./solutions/life_insurance_proceeds_calc" + timestr + '.csv'
    w = open(saved_answer,'a+')
    w.write("LIFE INSURANCE: CANCELS POLICY AND RECEIVES SURRENDER VALUE " + '\n' + string_gain_recognized + '\n' + string_loss_not_recognized + '\n' + string_amount_received + '\n' + string_premiums_policy)
    w.close()
    return

def traded():
    timestr = time.strftime("%Y%m%d-%H%M%S")

    proceeds_received = float(raw_input(yellow("Enter the proceeds received from the transaction")).replace(',',''))
    amount_paid_for_policy = float(raw_input(yellow("Enter the amount paid for policy: ")).replace(',',''))
    subsequent_premium_paid = float(raw_input(yellow("Enter the subsequent premiums paid: ")).replace(',',''))
    taxable_amount_for_transferee = proceeds_received - amount_paid_for_policy + subsequent_premium_paid

    string_taxable_amount_for_transferee = "TAXABLE AMOUNT FOR TRANSFEREE: " + str(taxable_amount_for_transferee)
    string_proceeds_received = "PROCEEDS RECEIVED: " + str(proceeds_received)
    string_amount_paid_for_policy = "AMOUNT PAID FOR POLICY: " + str(amount_paid_for_policy)
    string_subsequent_premium_paid = "SUBSEQUENT PREMIUMS PAID: " + str(subsequent_premium_paid)

    print green(string_taxable_amount_for_transferee)
    print yellow(string_proceeds_received + '\n' + string_amount_paid_for_policy + '\n' + string_subsequent_premium_paid)



    saved_answer = "./solutions/life_insurance_proceeds_calc" + timestr + '.csv'
    w = open(saved_answer,'a+')
    w.write("LIFE INSURANCE: TRADED FOR VALUE CONSIDERATION " + '\n' + string_taxable_amount_for_transferee + '\n' + string_proceeds_received + '\n' + string_amount_paid_for_policy + '\n' + string_subsequent_premium_paid)
    w.close()
    return

def reinvested():
    timestr = time.strftime("%Y%m%d-%H%M%S")

    # earnings are Taxable_Income
    # if insrance is collected in installments, interest added to gross income for taxation
    print """
    The

    1. Investment earnings
    2. Interest portion of each installment (if paid in installments)

    is included in Gross Income
    """
    investment_earnings = float(raw_input(yellow("Enter the amount of investment_earnings from reinvestment of life insurance proceeds: ")).replace(',',''))
    gross_income = float(raw_input(yellow("Enter the amount of gross income: ")).replace(',',''))
    installment_payments = float(raw_input(yellow("Enter the installment payments (if any): ")).replace(',',''))
    gross_income = gross_income + investment_earnings + installment_payments

    string_gross_income = "NEW GROSS INCOME: " + str(gross_income)
    string_investment_earnings = "INVESTMENT EARNINGS: " + str(investment_earnings)
    string_installment_payments = "INSTALLMENT PAYMENTS: " + str(installment_payments)

    print green(string_gross_income)
    print yellow(string_investment_earnings)
    print yellow(string_installment_payments)

    saved_answer = "./solutions/life_insurance_proceeds_calc" + timestr + '.csv'
    w = open(saved_answer,'a+')
    w.write("LIFE INSURANCE PROCEEDS REINVESTED: "
    + '\n' + string_gross_income
    + '\n' + string_investment_earnings
    + '\n' + string_installment_payments
    + '\n'
    )
    w.close()
    return

def exceptions():
    buy_sell_question = str(raw_input(green("Was this transaction made to facilitate buy-sell agreements?: ")))
    if buy_sell_question == "y":
        print green("The proceeds are not taxable")
        # main()
    elif tax_free_exchange_question == "y":
        print green("The proceeds are not taxable")
        # main()
    elif received_policy_as_gift_question == "y":
        print green('The proceeds are not taxable')
        # main()
    else:
        print yellow("The proceeds are taxable, please proceed to the rest of the question")
    return

def main():
    print """
    # 1. Paid solely to the due of the insured
    # 2. Cancels the policy and receives cash surrender Value
    # 3. Traded for value consideration
    # 4. Reinvested
    """

    opt_choice = float(raw_input(yellow("Enter a OPTION: ")).replace(',',''))

    if opt_choice == 1:
        paid_solely()
    elif opt_choice == 2:
        cancels_policy_receives_surrender()
    elif opt_choice == 3:
        exceptions()
        traded()
    elif opt_choice == 4:
        reinvested()
    elif opt_choice == 0:
        go_back_main_menu_module()
    else:
        print red('You have entered a invalid option')
        main()
    return
main()
