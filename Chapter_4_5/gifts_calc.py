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

def gift_basis_stock():
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
    green(string_GAIN_basis)
    string_LOSS_basis = "Recipient's LOSS BASIS: " + str(donee_loss_basis)
    yellow(string_LOSS_basis)
    string_HOLDING_period = "Recipient's HOLDING PERIOD: " + str(donee_holding_period)
    cyan(string_HOLDING_period)

    saved_answer = './solutions/gift_calc_stock' + timestr + '.csv'
    w = open(saved_answer,'a+')
    w.write(string_GAIN_basis + '\n')
    w.write(string_LOSS_basis + '\n')
    w.write(string_HOLDING_period + '\n')
    w.close()
    main()
    return

def depreciable_gift_property():
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


    donee_loss_basis = donee_loss_basis - (annual_depreciation_straight_line * years_passed)

    donee_gain_basis = donee_gain_basis - (annual_depreciation_straight_line * years_passed)

    if donee_loss_basis <= 0:
        donee_loss_basis = 0
    if donee_gain_basis <= 0:
        donee_gain_basis = 0
    string_GAIN_basis = "DONEE'S GAIN BASIS: " + str(donee_gain_basis)
    string_LOSS_basis = "DONEE'S LOSS BASIS: " + str(donee_loss_basis)
    # string_HOLDING_period = "DONEE'S HOLDING PERIOD: " + str(donee_holding_period)

    green(string_GAIN_basis)
    red(string_LOSS_basis)

    saved_answer = './solutions/depreciable_gift_property_solution' + timestr + '.csv'
    w = open(saved_answer,'a+')
    w.write(string_GAIN_basis + '\n')
    w.write(string_LOSS_basis + '\n')
    w.close()

    main()
    return

def deathbed_gifts(): # this one requires more reading to fully understand

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

    green(string_offspring_basis_after_bequeath)

    saved_answer = './solutions/deathbed_gifts_solution' + timestr + '.csv'
    w = open(saved_answer,'a+')
    w.write(string_offspring_basis_after_bequeath + '\n')
    w.close()
    main()
    return

def main():
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
        main()
    return
main()
