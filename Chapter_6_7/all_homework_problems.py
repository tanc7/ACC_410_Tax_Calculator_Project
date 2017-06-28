from termcolor import colored
import os
import sys
import socket
import StringIO
import time
import operator
# os.chdir('/root/Documents/ACC_410_Exam_Calculator_Project')
os.chdir('/root/Documents/ACC_410_Exam_Calculator_Project/Chapter_6_7')
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

def chapter_7_10():
    fmv_asset = float(raw_input(yellow("Enter the FMV of the asset: ")).replace(',','').replace('%','').replace('$',''))
    adj_basis = float(raw_input(yellow("Enter the adjusted basis of the asset: ")).replace(',','').replace('%','').replace('$',''))
    individual_AGI = float(raw_input(yellow("Enter the individual's AGI: ")).replace(',','').replace('%','').replace('$',''))

    print """
    Pick a scenario

    1. Pam sells the boat at a loss
    2. Pam Sells the boat at a gain
    3. Pam exchanges the boat for another boat
    4. The boat ended up being stolen
    """

    opt_choice = float(raw_input(yellow("Enter a OPTION: ")).replace(',','').replace('%','').replace('$',''))

    if opt_choice == 1:
        # calculate loss basis
        print red('Debug')
        if fmv_asset < adj_basis:
            loss_basis = fmv_asset

        if adj_basis < fmv_asset:
            loss_basis = adj_basis
        if adj_basis == fmv_asset:
            print "The loss basises are exactly the same"
            loss_basis = fmv_asset

        amount_realized = float(raw_input(yellow("Enter the amount realized from the LOSS sale: ")).replace(',','').replace('%','').replace('$',''))

        realized_loss = amount_realized - loss_basis

        str_solution = "REALIZED LOSS: %s" % str(realized_loss)
        print green(str_solution)
    elif opt_choice == 2:
        gain_basis = adj_basis
        amount_realized = float(raw_input(yellow("Enter the amount realized from the GAIN sale: ")).replace(',','').replace('%','').replace('$',''))

        realized_recognized_gain = amount_realized - gain_basis

        str_solution = "REALIZED AND RECOGNIZED GAIN: %s" % str(realized_recognized_gain)
        print green(str_solution)
        # calculate gain basis
    elif opt_choice == 3:
        # calculate boat exchanges
        adj_basis_given = float(raw_input(yellow("Enter the adjusted basis of the asset GIVEN: ")).replace(',','').replace('%','').replace('$',''))
        adj_basis_boot_given = float(raw_input(yellow("Enter the adjusted basis of the BOOT GIVEN: ")).replace(',','').replace('%','').replace('$',''))
        gain_recognized = float(raw_input(yellow("Enter the GAIN RECOGNIZED: ")).replace(',','').replace('%','').replace('$',''))
        fmv_boot_received = float(raw_input(yellow("Enter the FMV of the boot recieved: ")).replace(',','').replace('%','').replace('$',''))
        loss_recognized = float(raw_input(yellow("Enter the LOSS RECOGNIZED ")).replace(',','').replace('%','').replace('$',''))
        new_basis = adj_basis_given + adj_basis_boot_given + gain_recognized - fmv_boot_received - loss_recognized

        str_solution = "NEW BASIS IN ASSET: %s" % str(new_basis)
        print green(str_solution)
        # supposedly no difference if a like-kind exchange is done either sold or exchanged at a loss
    elif opt_choice == 4:
        # calculate stolen scenario
        if fmv_asset < adj_basis:
            loss_basis = fmv_asset
        elif adj_basis < fmv_asset:
            loss_basis = adj_basis

        insurance_proceeds_received = float(raw_input(yellow("Enter the insurance proceeds received (if any): ")).replace(',','').replace('%','').replace('$',''))

        deductible = loss_basis - insurance_proceeds_received

        if deductible < 0:
            deductible = 0

        str_solution = "REMAINING DEDUCTIBLE after accounting for RECEIPT OF INSURANCE PROCEEDS: %s" % str(deductible)
        print green(str_solution)

    return

def chapter_7_13_a():

    purchase_price = float(raw_input(yellow("Enter the PURCHASE PRICE: ")).replace(',','').replace('%','').replace('$',''))
    fmv_asset = float(raw_input(yellow("Enter the FMV of the asset: ")).replace(',','').replace('%','').replace('$',''))
    amount_realized = float(raw_input(yellow("Enter the AMOUNT REALIZED by the seller: ")).replace(',','').replace('%','').replace('$',''))
    adj_basis = float(raw_input(yellow("Enter the ADJUSTED BASIS of the asset; ")).replace(',','').replace('%','').replace('$',''))

    goodwill = purchase_price - fmv_asset
    realized_recognized_gain = amount_realized - adj_basis

    str_solution = "REALIZED & RECOGNIZED GAIN: %s" % str(realized_recognized_gain)
    print green(str_solution)
    str_solution = "GOODWILL: %s" % str(goodwill)
    print green(str_solution)
    gw_amortization_monthly = goodwill / (15*12)
    str_solution = "The goodwill wil be amortized over fifteen years at this amount per month: %s" % str(gw_amortization_monthly)
    print yellow(str_solution)

    str_solution = "ADJUSTED BASIS: %s" % str(adj_basis)
    print green(str_solution)

    return

def chapter_7_13_b():
    return

def chapter_7_14():
    amount_realized = float(raw_input(yellow("Amount realized from transaction: ")).replace(',','').replace('%','').replace('$',''))
    adj_basis_donor = float(raw_input(yellow("Adjusted basis from the Donor: ")).replace(',','').replace('%','').replace('$',''))
    fmv_asset = float(raw_input(yellow("FMV of the asset received: ")).replace(',','').replace('%','').replace('$',''))

    gain_basis = fmv_asset
    if adj_basis_donor < fmv_asset:
        loss_basis = adj_basis_donor
    if fmv_asset < adj_basis_donor:
        loss_basis = fmv_asset

    gain_or_loss = amount_realized - adj_basis_donor

    if gain_or_loss > 0:
        recognized_gain = gain_or_loss
    elif gain_or_loss <= 0:
        # personal-use assets, related party sales, non-taxable transaction and wash sales are all disallowed losses
        # this is a recognized loss however
        disallowed_question = str(raw_input(yellow("Is this transaction a Personal-Use Asset (or NOT converted to business use), Related Party Sale, Non-Taxable Transaction, or a Wash Sale?: ")).replace(',','').replace('%','').replace('$',''))
        if disallowed_question == "y":
            disallowed_loss = gain_or_loss
            str_solution = "DISALLOWED LOSS: %s" % disallowed_loss
            print green(str_solution)
        elif disallowed_question == "n":
            recognized_loss = gain_or_loss
            str_solution = "RECOGNIZED LOSS: %s" % recognized_loss
            print green(str_solution)
    return

def chapter_7_23():
    orig_cost_excl_land = float(raw_input(yellow("Enter the ORIGINAL COST EXCLUDING VALUE OF LAND: ")).replace(',','').replace('%','').replace('$',''))
    fmv_asset = float(raw_input(yellow("Enter the FMV at the Date of Conversion: ")).replace(',','').replace('%','').replace('$',''))

    if orig_cost_excl_land < fmv_asset:
        loss_basis = orig_cost_excl_land
    if fmv_asset < orig_cost_excl_land:
        loss_basis = fmv_asset

    gain_basis = adj_basis
    depreciation_basis = loss_basis

    new_rental_property_price = float(raw_input(yellow("New rental property PURCHASE PRICE: ")).replace(',','').replace('%','').replace('$',''))
    old_rental_property_adj_basis = float(raw_input(yellow("Old rental property ADJUSTED BASIS: ")).replace(',','').replace('%','').replace('$',''))
    like_kind_exchange_gain_loss = new_rental_property_price - old_rental_property_adj_basis

    str_solution = "LOSS BASIS: %s" % str(loss_basis)
    print green(str_solution)
    str_solution = "GAIN BASIS: %s" % str(gain_basis)
    print green(str_solution)
    str_solution = "DEPRECIATION BASIS: %s" % str(depreciation_basis)
    print green(str_solution)
    print "IF the old rental property was exchanged for another rental property at the specified value..."

    str_solution = "IF the old rental property was exchanged for another rental property at the specified value..."
    if like_kind_exchange_gain_loss <= 0:
        like_kind_exchange_gain_loss = like_kind_exchange_gain_loss * -1
        str_solution = "DISALLOWED LOSS: %s" % str(like_kind_exchange_gain_loss)
        print yellow(str_solution)
    if like_kind_exchange_gain_loss > 0:
        str_solution = "REALIZED & RECOGNIZED GAIN: %s" % str(like_kind_exchange_gain_loss)
        print yellow(str_solution)
    return

def chapter_7_28():
    adj_basis_asset_given_up = float(raw_input(yellow("Adjusted Basis of asset GIVEN UP")).replace(',','').replace('%','').replace('$',''))
    fmv_asset_given_up = float(raw_input(yellow("FMV of asset GIVEN UP:")).replace(',','').replace('%','').replace('$',''))
    fmv_asset_received = float(raw_input(yellow("FMV of asset RECEIVED: ")).replace(',','').replace('%','').replace('$',''))
    fmv_boot_received = float(raw_input(yellow("FMV of BOOT received: ")).replace(',','').replace('%','').replace('$',''))

    amount_realized = fmv_asset_received + fmv_boot_received

    gain_basis = adj_basis_asset_given_up
    if adj_basis_asset_given_up < fmv_asset_given_up:
        loss_basis = adj_basis_asset_given_up
    if adj_basis_asset_given_up > fmv_asset_given_up:
        loss_basis = fmv_asset_given_up

    gain_or_loss = amount_realized - adj_basis_asset_given_up

    if loss_basis < gain_or_loss < gain_basis:
        print "There is NO GAIN or LOSS recognized: Fell between the gain and loss basises: %s" % gain_or_loss
    if gain_or_loss <= 0:
        gain_or_loss = gain_or_loss * -1
        str_solution = "DISALLOWED LOSS: %s" % str(gain_or_loss)
        return
    if gain_or_loss > 0:
        realized_gain = gain_or_loss
        if realized_gain < fmv_boot_received:
            recognized_gain = realized_gain
            postponed_gain = fmv_boot_received - realized_gain
        if realized_gain > fmv_boot_received:
            recognized_gain = fmv_boot_received
            postponed_gain = realized_gain - fmv_boot_received
        str_solution = "RECOGNIZED GAIN: %s" % str(recognized_gain)
        print green(str_solution)
        str_solution = "POSTPONED GAIN: %s" % str(postponed_gain)
        print green(str_solution)


        basis_new_asset = fmv_asset_received - postponed_gain
        str_solution = "BASIS IN NEW ASSET: %s" % str(basis_new_asset)
        print green(str_solution)

    basis_boot = fmv_boot_received
    str_solution = "BASIS IN BOOT: %s" % str(basis_boot)
    print green(str_solution)
    return

def chapter_7_30():
    print "Does the asset qualify as 'Like-Kind Property?'"
    lke_question = str(raw_input(yellow("Enter 'y' or 'n': ")).replace(',','').replace('%','').replace('$',''))
    adj_basis_asset_given_up = float(raw_input(yellow("Enter the adjusted basis of the ASSET GIVEN UP: ")).replace(',','').replace('%','').replace('$',''))
    fmv_asset_received = float(raw_input(yellow("Enter the FMV of the ASSET RECEIVED: ")).replace(',','').replace('%','').replace('$',''))
    if lke_question == 'y':
        postponed_gain = fmv_asset_received - adj_basis_asset_given_up
        basis = fmv_asset_received - postponed_gain
        str_solution = "BASIS equals FMV minus POSTPONED GAIN: %s" % str(basis)
        print green(str_solution)

    elif lke_question == 'n':
        basis = fmv_asset_received
        str_solution = "BASIS equals FMV: %s" % str(basis)
        print green(str_solution)


    return

def chapter_6_12():
    return

def chapter_6_15():
    short_term_capital_loss = 0
    salaries = float(raw_input(yellow("Enter annual houseold salary for joint filing: ")).replace(',','').replace('%','').replace('$',''))
    # Section 1244 for INDIVIDUALS is ordinary loss
    s1244_ordinary_loss = float(raw_input(yellow("Enter the ordinary loss from S1244 Stock (acquired 2 years ago): ")).replace(',','').replace('%','').replace('$',''))
    s1244_short_term_capital_gain = float(raw_input(yellow("Enter the gain on S1244 Stock (acquired 6 months ago): ")).replace(',','').replace('%','').replace('$',''))
    non_business_bad_debt = float(raw_input(yellow("Enter any NON-BUSINESS bad debt: ")).replace(',','').replace('%','').replace('$',''))
    short_term_capital_loss = short_term_capital_loss + non_business_bad_debt
    remaining_s1244_loss = 0
    if s1244_ordinary_loss > 100000:
        remaining_s1244_loss = s1244_ordinary_loss - 100000
        s1244_ordinary_loss = 100000


    long_term_capital_loss = remaining_s1244_loss
    capital_loss_carry_forward = 0
    if long_term_capital_loss > 3000:
        capital_loss_carry_forward = long_term_capital_loss - 3000
        net_capital_loss = 3000
    else:
        net_capital_loss = long_term_capital_loss
    net_short_term_capital_gain = s1244_short_term_capital_gain - short_term_capital_loss
    adjusted_gross_income = salaries - s1244_ordinary_loss - net_capital_loss

    str_AGI = "Adjusted Gross Income: %s" % str(adjusted_gross_income)
    print green(str_AGI)
    str_CL_CF = "Capital Loss Carry Forward: %s" % str(capital_loss_carry_forward)
    print green(str_CL_CF)

    return

def chapter_6_17():

    adjusted_gross_income = float(raw_input(yellow("Enter the AGI of the household: ")).replace(',','').replace('%','').replace('$',''))
    insurance_proceeds_received = float(raw_input(yellow("Enter the insurance proceeds received as a result of the damage: ")).replace(',','').replace('%','').replace('$',''))
    adj_basis = float(raw_input(yellow("Enter the adjusted basis of the lost property: ")).replace(',','').replace('%','').replace('$',''))
    taxable_income = float(raw_input(yellow("Enter the taxable income: ")).replace(',','').replace('%','').replace('$',''))
    tax_rate = 0
    if 0 < adjusted_gross_income <= 18550:
        tax_rate = 0.1
    if 18550 < adjusted_gross_income <= 75300:
        tax_rate = 0.15
    if 75300 < adjusted_gross_income <= 151900:
        tax_rate = 0.25
    if 151900 < adjusted_gross_income <= 231450:
        tax_rate = 0.28
    if 231450 < adjusted_gross_income <= 413350:
        tax_rate = 0.33
    if 413350 < adjusted_gross_income <= 466950:
        tax_rate = 0.35
    if 466950 < adjusted_gross_income:
        tax_rate = 0.396
    amt_loss_before_agi_limit = adj_basis - insurance_proceeds_received - 100

    total_loss = amt_loss_before_agi_limit - (0.1 * taxable_income)
    if total_loss < 0:
        total_loss = 0

    tax_savings = total_loss * tax_rate

    if tax_savings < 0:
        tax_savings = 0
    disaster_area = 'No'

    disaster_area_question = str(raw_input(cyan("Has the President declared the affected area to be a disaster area? 'y' or 'n': ")).replace(',','').replace('%','').replace('$',''))
    if disaster_area_question == "y":
        print yellow("You could claim last year's loss on this year")
        disaster_area = "Yes"
    elif disaster_area_question == "n":
        print yellow("You can only claim on last year")
        disaster_area = "No"
    else:
        print red('You have entered a invalid option')
        chapter_6_17()

    str_loss_before_AGI = "Total loss BEFORE AGI: %s" % str(amt_loss_before_agi_limit)
    str_tax_savings = "TAX SAVINGS FOR CURRENT YEAR: %s" % str(tax_savings)
    str_tax_rate = "TAX RATE for AGI: %s" % str(tax_rate)
    str_total_loss = "TOTAL LOSS after 10 percent of AGI reduction: %s" % str(total_loss)
    str_AGI = "AGI: %s" % str(adjusted_gross_income)
    str_disaster = "DECLARATION OF DISASTER AREA: %s" % disaster_area

    print red(str_loss_before_AGI)
    print green(str_total_loss)
    print green(str_tax_savings)
    print yellow(str_tax_rate)
    print yellow(str_AGI)
    print yellow(str_disaster)
    return

def chapter_6_20(): # this one is not worth it. Because it requires specific variables, you are basically checking
# for a net change between one year At-Risk Investment and a increase for next-year
    # material participant
    invested_in_general_partnership_2015 = float(raw_input(yellow("Enter the amount invested in the general partnership for 2015: ")).replace(',','').replace('%','').replace('$',''))
    invested_in_general_partnership_2016 = float(raw_input(yellow("Enter the amount invested in the general partnership for 2016: ")).replace(',','').replace('%','').replace('$',''))
    share_of_partnership_losses_2015 = float(raw_input(yellow("Enter the amount of PARTNERSHIP LOSSES for 2015: ")).replace(',','').replace('%','').replace('$',''))
    share_of_partnership_losses_2016 = float(raw_input(yellow("Enter the amount of PARTNERSHIP LOSSES for 2016: ")).replace(',','').replace('%','').replace('$',''))

    at_risk_investment_2015 = invested_in_general_partnership_2015
    deductible_2015 = at_risk_investment_2015
    at_risk_investment_2015 = at_risk_investment_2015 - share_of_partnership_losses_2015
    carryforward_2015 = share_of_partnership_losses_2015 - at_risk_investment_2015

    if at_risk_investment_2015 < 0:
        at_risk_investment_2015 = 0
    if deductible_2015 < 0:
        deductible_2015 = 0
    if carryforward_2015 < 0:
        carryforward_2015 = 0

    str_at_risk_2015 = "At-Risk Investment END 2015: %s" % str(at_risk_investment_2015)
    str_deductible_2015 = "DEDUCTIBLE 2015: %s" % str(at_risk_investment_2015)
    # str_carryforward_2015 = "CARRYFORWARD 2015: %s" % str(carryforward_2015)


    print yellow(str_at_risk_2015)
    print green(str_deductible_2015)
    print yellow(str_carryforward_2015)

    at_risk_investment_2016 = invested_in_general_partnership_2016 + at_risk_investment_2015
    deductible_2016 = at_risk_investment_2016
    at_risk_investment_2016 = at_risk_investment_2016 - share_of_partnership_losses_2016
    carryforward_2016 = share_of_partnership_losses_2016 - at_risk_investment_2016

    if at_risk_investment_2016 < 0:
        at_risk_investment_2016 = 0
    if deductible_2016 < 0:
        deductible_2016 = 0
    if carryforward_2016 < 0:
        carryforward_2016 = 0

    str_at_risk_2016 = "At-Risk Investment END 2016: %s" % str(at_risk_investment_2016)
    str_deductible_2016 = "DEDUCTIBLE 2016: %s" % str(at_risk_investment_2016)
    # str_carryforward_2016 = "CARRYFORWARD 2016: %s" % str(carryforward_2016)
    print yellow(str_at_risk_2016)
    print green(str_deductible_2016)
    print yellow(str_carryforward_2016)
    return

def chapter_6_22():

    # Not material participant
    return

def chapter_6_25():
    return


def main():
    print """
    CHAPTER 6:

    Option 1 # 12
    Option 2 # 15
    Option 3 # 17
    Option 4 # 20
    Option 5 # 22
    Option 6 # 25

    Chapter 7:

    Option 7 # 10
    Option 8 # 13(a) and (b)
    Option 9 # 14
    Option 10 # 23
    Option 11 # 28
    Option 12 # 30
    """

    opt_choice = float(raw_input(yellow("Enter a OPTION: ")).replace(',','').replace('%','').replace('$',''))

    if opt_choice == 1:
        chapter_6_12()
    elif opt_choice == 2:
        chapter_6_15()
    elif opt_choice == 3:
        chapter_6_17()
    elif opt_choice == 4:
        chapter_6_20()
    elif opt_choice == 5:
        chapter_6_22()
    elif opt_choice == 6:
        chapter_6_25()
    elif opt_choice == 7:
        chapter_7_10()
    elif opt_choice == 8:
        chapter_7_13_a()
    elif opt_choice == 9:
        chapter_7_14()
    elif opt_choice == 10:
        chapter_7_23()
    elif opt_choice == 11:
        chapter_7_28()
    elif opt_choice == 12:
        chapter_7_30()
    elif opt_choice == 0:
        go_back_main_menu_module()

main()
