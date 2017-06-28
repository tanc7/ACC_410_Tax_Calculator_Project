from termcolor import colored
import os
import sys
import socket
import StringIO
import time
import operator
# os.chdir('/root/Documents/ACC_410_Exam_Calculator_Project')
os.chdir('/root/Documents/ACC_410_Exam_Calculator_Project/Chapter_8_12')
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
    document_name = '/root/Documents/ACC_410_Exam_Calculator_Project/Chapter_8_12/solutions/%s_%s.csv' % (save_name, timestr)
    w = open(document_name,'a+')
    w.write(solution + '\n')
    string = "Your solution is saved as: %s" % document_name
    print yellow(string)
    w.close()
    return
    # timestr = time.strftime("%Y%m%d-%H%M%S")
def calculate_monty_bad_debts_tax_benefit():
    non_business_bad_debts = float(raw_input(yellow("Enter a OPTION: ")).replace(',','').replace('$',''))
    capital_gain_income = float(raw_input(yellow("Enter a OPTION: ")).replace(',','').replace('$',''))
    net_loss = non_business_bad_debts - capital_gain_income
    capital_loss_carryforward = net_loss - capital_loss_deduction_limitation
    last_year_tax_benefit = net_loss
    str_solution = "NET LOSS: %s" % str(net_loss)
    print green(str_solution)
    save_solution('monty_bad_debts',str_solution)
    str_solution = "CAPITAL LOSS CARRYFORWARD: %s" % str(capital_loss_carryforward)
    print green(str_solution)
    save_solution('monty_bad_debts',str_solution)
    str_solution = "LAST YEAR'S TAX BENEFIT: %s" % str(last_year_tax_benefit)
    print green(str_solution)
    save_solution('monty_bad_debts',str_solution)

    return

def calculate_sec_1244_adjusted_gross_income():
    annual_salary = float(raw_input(yellow("Enter ANNUAL SALARY: ")).replace(',','').replace('$','').replace('%',''))
    short_term_capital_loss_nonbusiness_bad_debt = float(raw_input(yellow("Enter SHORT-TERM CAPITAL LOSS from NONBUSINESS BAD DEBT: ")).replace(',','').replace('$',''))
    ordinary_loss_s1244_limit = 100000
    stcg_s1244_stock = annual_salary - ordinary_loss_s1244_limit
    # net_short_term_capital_gain = stcg_s1244_stock - short_term_capital_loss
    net_short_term_capital_gain = stcg_s1244_stock - short_term_capital_loss
    long_term_capital_loss = remain_sec_1244_loss
    net_capital_loss = net_short_term_capital_gain - long_term_capital_loss

    if net_capital_loss > 3000:
        capital_loss_carryforward = net_capital_loss - 3000
        net_capital_loss = 3000

    effect_AGI = stcg_s1244_stock - net_capital_loss

    return

def casualty_theft_loss_hw_problem():

    adjusted_basis_asset = float(raw_input(yellow("Enter ANNUAL SALARY: ")).replace(',','').replace('$','').replace('%',''))
    insurance_proceeds_collected = float(raw_input(yellow("Enter ANNUAL SALARY: ")).replace(',','').replace('$','').replace('%',''))
    annual_AGI = float(raw_input(yellow("Enter ANNUAL SALARY: ")).replace(',','').replace('$','').replace('%',''))
    tax_rate = float(raw_input(yellow("Enter ANNUAL SALARY: ")).replace(',','').replace('$','').replace('%',''))
    total_loss = adjusted_basis_asset - insurance_proceeds_collected
    total_loss = total_loss - 100
    str_solution = "TOTAL LOSS BEFORE 10% OF AGI CONSIDERATION (less $100 per incident): %s" % str(total_loss)
    print green(str_solution)
    save_solution('casualty_theft_loss_homework',str_solution)

    tenth_AGI = 0.1 * annual_AGI
    str_solution = "10% of AGI: %s" % str(tenth_AGI)
    print green(str_solution)
    save_solution('casualty_theft_loss_homework',str_solution)

    total_loss = total_loss - tenth_AGI
    str_solution = "TOTAL LOSS AFTER REDUCING BY 10% OF AGI: %s" % str(total_loss)
    print green(str_solution)
    save_solution('casualty_theft_loss_homework',str_solution)

    tax_savings = total_loss * tax_rate # need to find all of the marginal tax rates on schedule y-1
    str_solution = "TAX SAVINGS (Total Loss x Tax Rate): %s\nTAX RATE: %s" % (str(tax_savings),
        str(tax_rate)
        )
    print green(str_solution)
    save_solution('casualty_theft_loss_homework',str_solution)

    return

def fred_at_risk_investment():
    print """
    Fred's Interest is not considered a passive Activity
    Fred is a Material Partcipant

    Losses can offset active and portfolio income
    """
    invested_in_general_p_ship_2015 = float(raw_input(yellow("Enter ANNUAL SALARY: ")).replace(',','').replace('$','').replace('%',''))
    share_p_ship_losses_2015 = float(raw_input(yellow("Enter ANNUAL SALARY: ")).replace(',','').replace('$','').replace('%',''))
    share_p_ship_losses_2016 = float(raw_input(yellow("Enter ANNUAL SALARY: ")).replace(',','').replace('$','').replace('%',''))

    at_risk_investment_begin_2015 = invested_in_general_p_ship_2015
    str_solution = "AT-RISK INVESTMENT (Beginning of 2015): %s" % str(invested_in_general_p_ship_2015)
    print green(str_solution)
    save_solution('fred_at_risk_investment_homework',str_solution)

    at_risk_investment_end_2015 = invested_in_general_p_ship_2015 - share_p_ship_losses_2015
    str_solution = "AT-RISK INVESTMENT (End of 2015): %s" % str(at_risk_investment_end_2015)
    print green(str_solution)
    save_solution('fred_at_risk_investment_homework',str_solution)

    at_risk_investment_end_2016 = at_risk_investment_end_2015 - share_p_ship_losses_2016
    str_solution = "AT-RISK INVESTMENT (End of 2016): %s" % str(at_risk_investment_end_2016)
    print green(str_solution)
    save_solution('fred_at_risk_investment_homework',str_solution)

    at_risk_suspended_losses = at_risk_investment_end_2015 - share_p_ship_losses_2016
    str_solution = "AT-RISK SUSPENDED LOSSES: %s" % str(at_risk_suspended_losses)
    print green(str_solution)
    save_solution('fred_at_risk_investment_homework',str_solution)

    return

def kay_homework_problem_partnership_interest():
    kay_basis_begin_2015
    share_of_partnership_loss_end_2015
    share_of_partnership_income

    at_risk_investment_end_2015 = kay_basis_begin_2015 - share_of_partnership_loss_end_2015
    income_or_loss_2016 = share_of_partnership_income

    return
def main():
    print"""
    # 1. Calculate Monty Homework Problem
    # 2. Calculate Section 1244 Homework Problem
    # 3. Calculate Casualty & Theft Losses Homework Problem
    # 4. Calculate Fred (At-Risk Investment) Problem
    """

    opt_choice = float(raw_input(yellow("Enter a OPTION: ")).replace(',','').replace('$',''))

    if opt_choice == 0:
        go_back_main_menu_module()
    elif opt_choice == 1:
        calculate_monty_bad_debts_tax_benefit()
    elif opt_choice == 2:
        calculate_sec_1244_adjusted_gross_income()
    elif opt_choice == 3:
        casualty_theft_loss_hw_problem()
    return
main()
