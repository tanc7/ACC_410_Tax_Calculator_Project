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

def option_one():
    return

def option_two():

    amt_realized = float(raw_input(yellow("Enter the AMOUNT REALIZED from the sale: ")).replace(',','').replace('%','').replace('$',''))
    adjusted_basis = float(raw_input(yellow("Enter the ADJUSTED BASIS of the asset that is sold: ")).replace(',','').replace('%','').replace('$',''))
    held_for_investment_question = str(raw_input("Is this item held for investment? ('y' or 'n'): "))
    holding_period = float(raw_input(yellow("Enter the MONTHS that the asset has been held: ")).replace(',','').replace('%','').replace('$',''))

    if held_for_investment_question == "y":
        held_for_investment = True
    if held_for_investment_question == "n":
        held_for_investment = False

    gain_loss_type = ''
    if held_for_investment == True:
        asset_type = 'Capital Asset'
        gain_loss_type = 'CAPITAL'
    else:
        asset_type = 'Not Capital Asset'
        gain_loss_type = 'ORDINARY'

    print "DEBUG gain_loss_type: %s" % gain_loss_type
    if holding_period > 12:
        gain_or_loss_attribute = 'Long-Term'
    else:
        gain_or_loss_attribute = 'Short-Term'

    gain_or_loss_amt = amt_realized - adjusted_basis

    if gain_or_loss_amt > 0:
        gain_or_loss_str = 'GAIN'
    else:
        gain_or_loss_str = 'LOSS'
        gain_or_loss_amt = gain_or_loss_amt * -1

    str_solution = "AMOUNT: %s %s %s" % (
        str(gain_or_loss_amt),
        gain_or_loss_attribute,
        # str(gain_or_loss_type),
        gain_or_loss_str
    )

    print green(str_solution)
    return

def option_three():
    entity_agi = float(raw_input(yellow("Enter the ADJUSTED GROSS INCOME OF THE ENTITY: ")).replace(',','').replace('%','').replace('$',''))
    lt_capital_gain = float(raw_input(yellow("Enter the LONG-TERM Capital GAIN: ")).replace(',','').replace('%','').replace('$',''))
    lt_capital_loss = float(raw_input(yellow("Enter the LONG-TERM Capital LOSS: ")).replace(',','').replace('%','').replace('$',''))
    st_capital_gain = float(raw_input(yellow("Enter the SHORT-TERM Capital GAIN: ")).replace(',','').replace('%','').replace('$',''))
    st_capital_loss = float(raw_input(yellow("Enter the SHORT-TERM Capital LOSS: ")).replace(',','').replace('%','').replace('$',''))
    lt_capital_g_or_l = lt_capital_gain - lt_capital_loss
    st_capital_g_or_l = st_capital_gain - st_capital_loss

    if lt_capital_g_or_l > 0:
        lt_capital_g_or_l_type = "GAIN"
    else:
        lt_capital_g_or_l_type = "LOSS"

    if st_capital_g_or_l > 0:
        st_capital_g_or_l_type = "GAIN"
    else:
        st_capital_g_or_l_type = "LOSS"


    net_capital = lt_capital_g_or_l + st_capital_g_or_l

    # if lt_capital_g_or_l > 0 and st_capital_g_or_l < 0 or st_capital_g_or_l > 0 and lt_capital_g_or_l < 0:
    #     net_capital = lt_capital_g_or_l + st_capital_g_or_l
    # elif lt_capital_g_or_l > 0 and st_capital_g_or_l > 0:
    #     net_capital = lt
    if net_capital > 0:
        net_capital_type = "GAIN"
    else:
        net_capital_type = "LOSS"

    str_solution = "NET CAPITAL %s: %s\nLONG-TERM CAPITAL %s: %s\nADD: SHORT-TERM CAPITAL %s: %s" % (
        str(net_capital_type),
        str(net_capital),
        str(lt_capital_g_or_l_type),
        str(lt_capital_g_or_l),
        str(st_capital_g_or_l_type),
        str(st_capital_g_or_l)
    )

    print green(str_solution)

    return

def option_four():
    return

def option_five():
    return

def option_six():

    amt_realized = float(raw_input(yellow("Enter the AMOUNT REALIZED from the sale: ")).replace(',','').replace('%','').replace('$',''))
    cost = float(raw_input(yellow("Enter the ORIGINAL COST of the asset (original adjusted basis): ")).replace(',','').replace('%','').replace('$',''))
    accumulated_depreciation = float(raw_input(yellow("Enter the DEPRECIATON TAKEN on the property before sale: ")).replace(',','').replace('%','').replace('$',''))
    adjusted_basis = cost - accumulated_depreciation
    gain_or_loss = amt_realized - adjusted_basis

    if gain_or_loss >= 0:
        gain_or_loss_attribute = 'GAIN'
    else:
        gain_or_loss_attribute = 'LOSS'
        gain_or_loss = gain_or_loss * -1

    if gain_or_loss < accumulated_depreciation:
        gain_or_loss_type = 'ORDINARY'
    else:
        gain_or_loss_type = 'S1231 or CAPITAL'

    str_solution = """
    %s %s: %s
    FROM:
    Amount Realized: %s
    LESS: Adjusted Basis: %s = Cost: %s - Accumulated Depreciation: %s
    ____________________________________________________________________
    EQUALS: %s
    TYPE: %s
    GAIN OR LOSS: %s
    """ % (
        str(gain_or_loss_type),
        str(gain_or_loss_attribute),
        str(gain_or_loss),
        str(amt_realized),
        str(adjusted_basis),
        str(cost),
        str(accumulated_depreciation),
        str(gain_or_loss),
        str(gain_or_loss_type),
        str(gain_or_loss_attribute)
    )
    print green(str_solution)
    return

def option_seven():
    gross_income = float(raw_input(yellow("Enter the GROSS INCOME of the Business: ")).replace(',','').replace('%','').replace('$',''))
    operating_expenses = float(raw_input(yellow("Enter the OPERATING EXPENSES of the business: ")).replace(',','').replace('%','').replace('$',''))
    cash_distributions = float(raw_input(yellow("Enter the TOTAL amount of CASH DISTRIBUTIONS made to participants in business: ")).replace(',','').replace('%','').replace('$',''))
    lt_capital_gain_or_loss = float(raw_input(yellow("Enter the amount of LONG-TERM Capital GAIN (positive) or LOSS (negative): ")).replace(',','').replace('%','').replace('$',''))
    amt_participants = float(raw_input(yellow("Enter the amount of participants with equal representation: ")).replace(',','').replace('%','').replace('$',''))
    net_profit = gross_income - operating_expenses
    per_person_net_profit = net_profit / amt_participants
    per_person_ltcg_or_l = lt_capital_gain_or_loss / amt_participants
    per_person_dividend_income = cash_distributions / amt_participants

    print "DEBUG: per_person_dividend_income = %s" % per_person_dividend_income
    corp_taxable_income = gross_income - operating_expenses + lt_capital_gain_or_loss
    # Partnerships
    str_solution = """
    FOR EACH PARTNER:
    Net Profit = %s
    Long-Term Capital Gain = %s, subject to the 0/15/20 Percent Preferential Tax Rate that applies to LTCG or L
    """ % (
        str(per_person_net_profit),
        str(per_person_ltcg_or_l)
    )

    print green(str_solution)
    # S-Corporations
    str_solution = """
    FOR EACH SHAREHOLDER IN A S-CORPORATION:
    Net Profit = %s
    Long-Term Capital Gain = %s, subject to Capital Loss Limitations
    """ % (
        str(per_person_net_profit),
        str(per_person_ltcg_or_l)
    )

    print cyan(str_solution)

    # C-Corporations
    # str_solution = """
    # FOR THE CORPORATION:
    # Taxable Income: %s
    #
    # FOR EACH SHAREHOLDER OF THE C-CORPORATION:
    # Dividend Income: %s, Subject to the preferential tax rate of 0/15/20%
    # """ % (
    #     str(corp_taxable_income),
    #     str(per_person_dividend_income)
    # )

    str_solution = """
    FOR THE CORPORATION:
    Taxabe Income: {0}

    FOR EACH SHAREHOLDEROF THE C-CORPORATION:
    Dividend Income: {1}, Subject to the preferential tax rat of 0/15/20%
    """.format(
        str(corp_taxable_income),
        str(per_person_dividend_income)
    )

    print red(str_solution)
    return

def option_eight():
    return

def option_nine():
    transferor_basis = float(raw_input(yellow("Enter the transferor's Adjusted Basis prior to exchange: ")).replace(',','').replace('%','').replace('$',''))
    fmv_transfer = float(raw_input(yellow("Enter the FMV of the asset transferred to Corporation: ")).replace(',','').replace('%','').replace('$',''))
    boot_received = float(raw_input(yellow("Enter the AMOUNT of BOOT received by the contributor (if any): ")).replace(',','').replace('%','').replace('$',''))
    value_per_share = float(raw_input(yellow("Enter the value PER SHARE issued to contributor: ")).replace(',','').replace('%','').replace('$',''))
    amt_of_shares_issued = float(raw_input(yellow("Enter the AMOUNT of shares issued to contributor: ")).replace(',','').replace('%','').replace('$',''))
    # if inventory transferred to Corporation
    gain_or_loss = fmv_transfer - (value_per_share * amt_of_shares_issued)
    if gain_or_loss == 0 and boot_received != 0:
        str_solution = """
        ORDINARY GAIN: %s (boot received)
        """

        print green(str_solution)
    # if Equipment

    # if proprietary process

    # if cash
    return

def option_ten():
    return

def option_eleven():
    adjusted_basis = float(raw_input(yellow("Enter the adjusted basis of the property given to Corporation (Cost - Accumulated Depreciation): ")).replace(',','').replace('%','').replace('$',''))
    fmv_property = float(raw_input(yellow("Enter the FMV of the property: ")).replace(',','').replace('%','').replace('$',''))
    liabilities_assumed = float(raw_input(yellow("Enter the LIABILITIES assumed by the Corporation on the property: ")).replace(',','').replace('%','').replace('$',''))

    # basis to contributor
    gain_recognized_contributor = liabilities_assumed - adjusted_basis
    basis_stock = adjusted_basis - liabilities_assumed + gain_recognized_contributor
    # basis to corporation
    basis_prop_transferred_corp = adjusted_basis + gain_recognized_contributor

    str_solution = """
    CONTRIBUTOR:
    Gain Recognized: %s (Liabilities Assumed by Corp: %s - Basis in Transferred Property: %s)
    Basis in Corporation Stock: %s (Basis in Transferred Property: %s - Liabilities Assumed by Corp: %s + Gain Recognized by Contributor: %s)

    CORPORATION:
    Basis in Property Received from Contributor: %s + Gain Recognized by Contributor: %s
    """ % (
        str(gain_recognized_contributor),
        str(liabilities_assumed),
        str(adjusted_basis),
        str(basis_stock),
        str(adjusted_basis),
        str(liabilities_assumed),
        str(gain_recognized_contributor),
        str(basis_prop_transferred_corp),
        str(gain_recognized_contributor)
    )

    print green(str_solution)
    return

def option_twelve():
    return

def option_thirteen():
    return

def option_fourteen():
    net_income_per_books = float(raw_input(yellow("Enter the NET INCOME per books: ")).replace(',','').replace('%','').replace('$',''))
    federal_income_tax_per_books = float(raw_input(yellow("Enter the AMOUNT of FEDERAL INCOME TAX per books: ")).replace(',','').replace('%','').replace('$',''))
    tax_exempt_int_income = float(raw_input(yellow("Enter the amount of TAX EXEMPT INTEREST INCOME: ")).replace(',','').replace('%','').replace('$',''))
    life_insurance_proceeds = float(raw_input(yellow("Enter the amount of LIFE INSURANCE PROCEEDS RECEIVED: ")).replace(',','').replace('%','').replace('$',''))
    interest_on_loan_to_purch_tax_exempt_bonds = float(raw_input(yellow("Enter the amount on INTEREST on LOAN TO PURCHASE TAX EXEMPT BONDS: ")).replace(',','').replace('%','').replace('$',''))
    excess_of_capital_losses_over_gains = float(raw_input(yellow("Enter the amount of EXCESS OF CAPITAL LOSSES OVER GAINS: ")).replace(',','').replace('%','').replace('$',''))
    premiums_paid_on_life_insurance_policy = float(raw_input(yellow("Enter the amount of PREMIUMS PAID ON LIFE INSURANCE POLICY: ")).replace(',','').replace('%','').replace('$',''))

    add_to_net_income = federal_income_tax_per_books + excess_of_capital_losses_over_gains + interest_on_loan_to_purch_tax_exempt_bonds + premiums_paid_on_life_insurance_policy
    subtract_from_net_income = tax_exempt_int_income + life_insurance_proceeds

    taxable_income = net_income_per_books + add_to_net_income - subtract_from_net_income

    str_solution = """
                CORPORATION'S SCHEDULE M-1

    CORPORATION'S TAXABLE INCOME: {0}
    FROM:
    NET INCOME {1}
    Add To: {2}
        FEDERAL INCOME TAX per books {3}
        EXCESS CAPITAL LOSS over GAINS {4}
        INTEREST on LOAN to purchase tax-exempt bonds {5}
        PREMIUMS PAID on life insurance policy on life of Albatross's President {6}
    Subtract From: {7}
        TAX EXEMPT Interest Income {8}
        Life insurance PROCEEDS RECEIVED {9}
    ____________________________________________________________________
    EQUALS: TAXABLE INCOME {0}

    """.format(
        str(taxable_income),
        str(net_income_per_books),
        str(add_to_net_income),
        str(federal_income_tax_per_books),
        str(excess_of_capital_losses_over_gains),
        str(interest_on_loan_to_purch_tax_exempt_bonds),
        str(premiums_paid_on_life_insurance_policy),
        str(subtract_from_net_income),
        str(tax_exempt_int_income),
        str(life_insurance_proceeds)
    )

    print green(str_solution)
    return

def option_15(): #Corporate Tax Formula
    gross_income = float(raw_input(yellow("Enter the GROSS INCOME of the CORPORATION: ")).replace(',','').replace('%','').replace('$',''))
    deductions = float(raw_input(yellow("Enter the DEDUCTIONS: ")).replace(',','').replace('%','').replace('$',''))
    charitable_contributions = float(raw_input(yellow("Enter the CHARITABLE CONTRIBUTIONS (if any, else, enter 0): ")).replace(',','').replace('%','').replace('$',''))
    dividends_received_deduction = float(raw_input(yellow("Enter the DIVIDENDS RECEIVED DEDUCTION: ")).replace(',','').replace('%','').replace('$',''))
    nol_cb = float(raw_input(yellow("Enter NOL Carryback: ")).replace(',','').replace('%','').replace('$',''))
    stcl_cb = float(raw_input(yellow("Enter the SHORT-TERM CAPITAL LOSS CARRYBACK: ")).replace(',','').replace('%','').replace('$',''))

    ti_for_charitable_limit = gross_income - deductions
    str_solution = """
    TAXABLE INCOME before CHARITABLE CONTRIBUTION LIMIT: {0}\n FROM: GROSS INCOME {1} - DEDUCTIONS {2}
    """.format(
        str(ti_for_charitable_limit),
        str(gross_income),
        str(deductions)
    )
    print yellow(str_solution)
    ti_for_drd = ti_for_charitable_limit - charitable_contributions
    str_solution = """
    TAXABLE INCOME for DIVIDENDS RECEIVED DEDUCTION: {0}\n FROM: TI FOR CC {1} - CHARITABLE CONTRIBUTIONS {2}
    """.format(
        str(ti_for_drd),
        str(ti_for_charitable_limit),
        str(charitable_contributions)
    )
    print yellow(str_solution)
    ti_before_cb = ti_for_drd - dividends_received_deduction
    taxable_income = ti_before_cb - nol_cb - stcl_cb
    str_solution = """
    TAXABLE INCOME before CARRYBACKS: {0}\n FROM: TI for DRD {1} - DIVIDENDS RECEIVED DEDUCTION {2}
    """.format(
        str(ti_before_cb),
        str(ti_for_drd),
        str(dividends_received_deduction)
    )
    print yellow(str_solution)
    str_solution = """TAXABLE INCOME: {0}\n FROM: TI before CB {1} - NOL CB {2} - STCL CB {3}
    """.format(
        str(taxable_income),
        str(ti_before_cb),
        str(nol_cb),
        str(stcl_cb)
    )
    print green(str_solution)
    return

def option_16(): # shareholder and corporaton basises
    basis_xferred_assets = float(raw_input(yellow("Enter the BASIS the SHAREHOLDER transferred to CORPORATION: ")).replace(',','').replace('%','').replace('$',''))
    gain_recognized_on_exchange = float(raw_input(yellow("Enter the GAIN RECOGNIZED by the SHAREHOLDER: ")).replace(',','').replace('%','').replace('$',''))
    boot_received = float(raw_input(yellow("Enter any BOOT RECEIVED: ")).replace(',','').replace('%','').replace('$',''))
    liabilities_xferred_to_corp = float(raw_input(yellow("Enter the AMOUNT OF LIABILITIES assumed by the CORPORATION: ")).replace(',','').replace('%','').replace('$',''))
    adj_basis_for_loss_prop = float(raw_input(yellow("If elected, enter the ADJUSTED BASIS of the LOSS PROPERTY: ")).replace(',','').replace('%','').replace('$',''))

    # stockholder
    basis_stock_received_by_shareholder = basis_xferred_assets + gain_recognized_on_exchange - boot_received - liabilities_xferred_to_corp - adj_basis_for_loss_prop

    str_solution = """
    BASIS of stock received by SHAREHOLDER: {0}
    FROM:
    Basis of Assets transferred {1}
    ADD: Gain recognized on exchange {2}
    LESS: Boot received {3}
    LESS: Liabilities assumed by Corporation {4}
    LESS: IF elected, adjusted basis for LOSS PROPERTY {5}
    ____________________________________________________________________
    EQUALS: Basis of Stock received by S/H {0}
    """.format(
        str(basis_stock_received_by_shareholder),
        str(basis_xferred_assets),
        str(gain_recognized_on_exchange),
        str(boot_received),
        str(liabilities_xferred_to_corp),
        str(adj_basis_for_loss_prop)
    )

    print green(str_solution)

    # Corporation
    basis_of_assets_corporate = basis_xferred_assets + gain_recognized_on_exchange - adj_basis_for_loss_prop
    str_solution = """
    BASIS of assets transferred to CORPORATION: {0}
    FROM:
    Basis of Assets transferred {1}
    ADD: Gain recognized on exchange {2}
    LESS: IF elected, adjusted basis for LOSS PROPERTY {3}
    ____________________________________________________________________
    EQUALS: Basis of assets transferred to CORPOATION {0}
    """.format(
        str(basis_of_assets_corporate),
        str(basis_xferred_assets),
        str(gain_recognized_on_exchange),
        str(adj_basis_for_loss_prop)
    )

    print green(str_solution)
    return
def main():
    title_str = """
    # CHAPTER 8 Homework Problems:

    # 1. Problem #12: Garage Sale
    # 2. COMPLETE Problem #15: Classic Video Games Held for Investment
    # 3. COMPLETE Problem #26: Netting Capital Gains and Losses
    # 4. Problem #27: Gain on Sale of Art that has Appreciated in Value
    # 5. Problem #35: S1231 Gain or Losses
    # 6. COMPLETE Problem #37: Selling S1231 Assets and Recapture Provisions


    # Chapter 12 Homework Problems:

    # 7. COMPLETE Problem #13: Partnerships v. S-Corporations v. C-Corporations
    # 8. Problem #15: Leasing Equipment to Corporations, avoiding Dividend Classification
    # 9. Problem #16: Contributions in exchange for Stock and Ownership in a Corporations
    # 10. Problem #20: Control of a Corporation after subsequent Transfers of Ownership to Family, Section 318 & 351
    # 11. COMPLETE Problem #22: Transferring Property with Liabilities Assumed by Corporation
    # 12. Problem #34: Organizational Expenditures and Section 248
    # 13. Problem #36: Determining Income Tax Liability of a Corporation
    # 14. COMPLETE Problem #38: Filling Schedule M-1 for a Corporation

    # Calculators
    # 15. COMPLETE Corporate Tax Formula
    # 16. COMPLETE Shareholder and Corporation's Basises upon transfer of property with liabilities assumed by corporation
    """

    print cyan(title_str)
    opt_choice = float(raw_input(yellow("Enter a OPTION: ")).replace(',','').replace('%','').replace('$',''))

    if opt_choice == 1:
        os.system('clear')
        option_one()
        main()
        return
    elif opt_choice == 2:
        os.system('clear')
        option_two()
        main()

        return
    elif opt_choice == 3:
        os.system('clear')
        option_three()
        main()

        return
    elif opt_choice == 4:
        os.system('clear')
        option_four()
        main()

        return
    elif opt_choice == 5:
        os.system('clear')
        option_five()
        main()

        return
    elif opt_choice == 6:
        os.system('clear')
        option_six()
        main()

        return
    elif opt_choice == 7:
        os.system('clear')
        option_seven()
        main()

        return
    elif opt_choice == 8:
        os.system('clear')
        option_eight()
        main()

        return
    elif opt_choice == 9:
        os.system('clear')
        option_nine()
        main()

        return
    elif opt_choice == 10:
        os.system('clear')
        option_ten()
        main()

        return
    elif opt_choice == 11:
        os.system('clear')
        option_eleven()
        main()

        return
    elif opt_choice == 12:
        os.system('clear')
        option_twelve()
        main()

        return
    elif opt_choice == 13:
        os.system('clear')
        option_thirteen()
        main()

        return
    elif opt_choice == 14:
        os.system('clear')
        option_fourteen()
        main()

        return
    elif opt_choice == 15:
        os.system('clear')
        option_15()
        main()
    elif opt_choice == 16:
        os.system('clear')
        option_16()
        main()
    elif opt_choice == 0:
        go_back_main_menu_module()
        return

    else:
        print red("You have entered a invalid option")
        main()
    return
main()
