from termcolor import colored
import os
import sys
import socket
import StringIO
import time
import operator
# os.chdir('/root/Documents/ACC_410_Exam_Calculator_Project')
os.chdir('/root/Documents/ACC_410_Exam_Calculator_Project/Chapter_14_15')
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

    fmv_contributed = float(raw_input(yellow("Enter the FMV of the property the partner is contributing: ")).replace(',','').replace('%','').replace('$',''))
    adj_basis_contributed = float(raw_input(yellow("Enter the ADJUSTED BASIS of the property that the parner is contributing: ")).replace(',','').replace('%','').replace('$',''))
    realized_gain = fmv_contributed - adj_basis_contributed
    partner_interest = adj_basis_contributed
    partnership_basis_received = adj_basis_contributed

    str_solution = """

    ***CONTRIBUTING PARTNER***

    REALIZED GAIN = {0}
    FROM:
    Fair Market value: {1}
    Less: Adjusted Basis: {2}
    ____________________________________________________________________
    Equals: Realized Gain of: {0}

    RECOGNIZED GAIN = ZERO, as long as the individual is a partner

    ***PARTNERSHIP RECEIVING THE PROPERTY***

    BASIS IN RECEIVED PROPERTY = {2}
    Same as Adjusted Basis

    PARTNERSHIP DEPRECIATION RULES ON RECEIVED PROPERTY
    DEPRECIABLE/USEFUL LIFE = REMAINING
    DEPRECIAION RATES = SAME/REMAINING
    """.format(
        str(realized_gain),
        str(fmv_contributed),
        str(adj_basis_contributed)
    )

    print yellow(str_solution)

    return

def option_two(): # Problem #15, land contributions to a LLC

    adj_basis_contributed = float(raw_input(yellow("Enter the ADJUSTED BASIS of the contributed LAND from the partner/LLC member: ")).replace(',','').replace('%','').replace('$',''))
    amt_realized = float(raw_input(yellow("Enter the AMOUNT REALIZED from the land sale: ")).replace(',','').replace('%','').replace('$',''))

    contributor_basis = adj_basis_contributed
    allocated_gain_loss_to_contributor = amt_realized - adj_basis_contributed
    gain_or_loss = ""
    if allocated_gain_loss_to_contributor <= 0:
        gain_or_loss = "LOSS"
    if allocated_gain_loss_to_contributor > 0:
        gain_or_loss = "GAIN"
    post_sale_basis = adj_basis_contributed + allocated_gain_loss_to_contributor

    str_solution = """
    PARTNER/LLC's HOLDING PERIOD: Includes Holding Period provided by the contributor

    CONTRIBUTOR's BASIS in the PARTNERSHIP/LLC = {0}
    Equals Adjusted Basis of the land contributed

    ***IF THE PARTNER/LLC were to sell the land for ${1} amount of dollars***

    According to Section 722, all of the Unrealized Gain is allocated to the contributing member

    {2} to CONTRIBUTING MEMBER = {3}
    FROM:
    Amount Realized: {1}
    Less: Adjusted Basis of Sold Land: {0}
    ____________________________________________________________________
    Equals: {3}

    Contributing Member's Post-Sale Basis in Partnership Interest = {4}
    """.format(
        str(adj_basis_contributed),
        str(amt_realized),
        str(gain_or_loss),
        str(allocated_gain_loss_to_contributor),
        str(post_sale_basis)
    )

    print green(str_solution)
    return

def option_three(): #16 Beginning and Ending Capital Accounts

    percentage_ownership = float(raw_input(yellow("Enter the percentage of ownership of the partner: ")).replace(',','').replace('%','').replace('$',''))
    percentage_ownership = percentage_ownership / 100
    total_partnership_debt = float(raw_input(yellow("Enter the total amount Partnership's TOTAL Recourse Debts Payable to Unrelated Parties: ")).replace(',','').replace('%','').replace('$',''))
    begin_year_capital_account = float(raw_input(yellow("Enter the beginning balance of partner's CAPITAL ACCOUNT: ")).replace(',','').replace('%','').replace('$',''))
    share_of_partnership_debt = total_partnership_debt * percentage_ownership

    begin_year_interest_in_partnership = begin_year_capital_account + share_of_partnership_debt

    taxable_income = float(raw_input(yellow("Enter the TOTAL amount of the Partnership's TAXABLE INCOME: ")).replace(',','').replace('%','').replace('$',''))
    interest_income = float(raw_input(yellow("Enter the TOTAL amount of the Partnership's INTEREST INCOME: ")).replace(',','').replace('%','').replace('$',''))
    netted_gains_and_losses = float(raw_input(yellow("Enter the NET amount of the Partnership's NETTED GAINS AND LOSSES: ")).replace(',','').replace('%','').replace('$',''))
    share_of_taxable_income = percentage_ownership * taxable_income
    share_of_interest_income = percentage_ownership * interest_income
    share_of_netted_gains_and_losses = percentage_ownership * netted_gains_and_losses
    charitable_contributions = float(raw_input(yellow("Enter the amount of any CHARITABLE CONTRIBUTIONS made by the partnership: ")).replace(',','').replace('%','').replace('$',''))
    cash_distributions = float(raw_input(yellow("Enter the amount of any CASH DISTRIBTIONS that were made to partner: ")).replace(',','').replace('%','').replace('$',''))


    end_year_interest_in_partnership = begin_year_capital_account + share_of_taxable_income + share_of_interest_income + share_of_netted_gains_and_losses - charitable_contributions - cash_distributions + share_of_partnership_debt

    str_solution = """
    ***BEGINNING OF YEAR***
    Partner's Basis in Partnership Interest: {0}
    from:
    Partner's Capital Account: {1}
    Add: Partner's Share of Partnership Debt: {2}
    ____________________________________________________________________
    Equals: Partner's Beginning Year Partnership Interest: {0}

    ***END OF YEAR***

    Partner's Basis in Partnership: {3}
    from:
    Beginning Year's Capital Account {1}
    Add:
        Share of Taxable Income {4}
        Share of Interest Income {5}
        Share of Net Gains and Losses {6}
        Share of Partnership Debt {2}
    Less:
        Charitable Contributions by Partnership {7}
        Cash Distributions made to the Partner {8}
    ____________________________________________________________________
    Equals: Partner's End-Year Basis in Partnership Interest: {4}
    """.format(
        str(begin_year_interest_in_partnership),
        str(begin_year_capital_account),
        str(share_of_partnership_debt),
        str(end_year_interest_in_partnership),
        str(share_of_taxable_income),
        str(share_of_interest_income),
        str(share_of_netted_gains_and_losses),
        str(charitable_contributions),
        str(cash_distributions)
    )

    print green(str_solution)
    return

def option_four(): #30 Contributionswith Qualified Nonrecourse Debt (Real Estate) and Schedule K-1 Reporting
    partnership_interest = float(raw_input(yellow("Enter the amount of partnership interest that the contributor is going to receive by contributing real estate: ")).replace(',','').replace('%','').replace('$',''))
    partnership_interest = partnership_interest / 100
    adjusted_basis_contributed_real_estate = float(raw_input(yellow("Enter the adjusted basis of the contributed real estate: ")).replace(',','').replace('%','').replace('$',''))
    qualified_nonrecourse_debt = float(raw_input(yellow("Enter the amount of the PARTNER'S qualified nonrecourse debt that was transferred to partnership: ")).replace(',','').replace('%','').replace('$',''))

    debt_relief_assumed_by_partnership = qualified_nonrecourse_debt
    share_of_partnership_nonrecourse_debt = partnership_interest * qualified_nonrecourse_debt

    contributor_partnership_interest = adjusted_basis_contributed_real_estate + debt_relief_assumed_by_partnership + share_of_partnership_nonrecourse_debt

    sales = float(raw_input(yellow("NET SALES: ")).replace(',','').replace('%','').replace('$',''))
    util_and_other_operating_exp = float(raw_input(yellow("Utilites, Salary, and Other Operating Expenses: ")).replace(',','').replace('%','').replace('$',''))
    netted_gains_and_losses = float(raw_input(yellow("Netted Gains and Losses: ")).replace(',','').replace('%','').replace('$',''))
    tax_exempt_interest_income = float(raw_input(yellow("Tax Exempt Interest Income: ")).replace(',','').replace('%','').replace('$',''))
    charitable_contributions = float(raw_input(yellow("Charitable Contributions: ")).replace(',','').replace('%','').replace('$',''))
    cash_distributions = float(raw_input(yellow("Cash Distributions Made to Partners: ")).replace(',','').replace('%','').replace('$',''))
    recourse_debt = float(raw_input(yellow("End Year Balance of Recourse Debt: ")).replace(',','').replace('%','').replace('$',''))
    partnership_qualified_nonrecourse_debt = float(raw_input(yellow("End Year Balance of Qualified Nonrecourse Debt: ")).replace(',','').replace('%','').replace('$',''))

    pship_ordinary_income = sales - util_and_other_operating_exp
    pship_sep_stated = netted_gains_and_losses
    pship_tax_exempt_int_inc = tax_exempt_interest_income
    pship_chari_contri = charitable_contributions

    partner_ordinary_income = partnership_interest * pship_ordinary_income
    partner_netted_gains_and_losses = partnership_interest * netted_gains_and_losses
    partner_tax_exempt_int_inc = partnership_interest * tax_exempt_interest_income
    partner_chari_contri = partnership_interest * charitable_contributions
    str_solution = """

    # Contributing Real Estate with Qualified Non-Recourse Debt

    Contributor's Partnership Interest: {0}
    from:
    Adjusted Basis of Contributed Real Estate (With Qualified Nonrecourse Debt):
    Add: Debt Relief Assumed by Partnership: {1}
    Less: Contributor's Share of Qualified Non Recourse Debt: {2}
    ____________________________________________________________________
    Equals: Partnership Interest: {0}

    # Partner K-1

    Partner's Percentage of Interest in Partnership: {3}%

    Share of Ordinary Income: {4}
    Share of Netted Gains and Losses: {5}
    Share of Tax Exempt Interest Income: {6}
    Share of Charitable Contributions: {7}

    # Partnership K-1

    Ordinary Income: {8}
    Separately Stated Items: {9}
    Tax Exempt Interest Income: {10}
    Charitable Contributions: {11}

    """.format(
        str(contributor_partnership_interest),
        str(debt_relief_assumed_by_partnership),
        str(share_of_partnership_nonrecourse_debt),
        str(partnership_interest * 100),
        str(partner_ordinary_income),
        str(partner_netted_gains_and_losses),
        str(partner_tax_exempt_int_inc),
        str(partner_chari_contri),
        str(pship_ordinary_income),
        str(pship_sep_stated),
        str(pship_tax_exempt_int_inc),
        str(pship_chari_contri)
    )

    print green(str_solution)

    return

def option_five(): # CHapter 12 problem #12, Net Operating Losses, Suspended, and CArryforwards

    share_s_corp_nol = float(raw_input(yellow("Shareholder's Share of NOL from S-Corp: ")).replace(',','').replace('%','').replace('$',''))
    share_s_corp_stock_basis = float(raw_input(yellow("Shareholder's Share of S-Corp's Stock Basis: ")).replace(',','').replace('%','').replace('$',''))
    excess_nol_over_basis = share_s_corp_nol - share_s_corp_stock_basis

    str_solution = """
    Excess of NOL over Stock Basis in S-Corporation: {0}

    This amount...
        1. Can be claimed entirely as a Net Operating Loss, reducing basis to 0
        2. Then suspended and carried forwards

    from:
    Share of S-Corp NOL: {1}
    Less: Share of S-Corp Stock Basis: {2}
    ____________________________________________________________________
    Equals:
    """.format(
        str(excess_nol_over_basis),
        str(share_s_corp_nol),
        str(share_s_corp_stock_basis)
    )

    print green(str_solution)
    return
5
def option_six(): #17 loss allocation of sold s-corp stock

    day_of_sale = float(raw_input(yellow("The day of sale out of 365 days: ")).replace(',','').replace('%','').replace('$',''))
    loss_amount = float(raw_input(yellow("The amount of loss incurred by the S-Corp on the shares of stock: ")).replace(',','').replace('%','').replace('$',''))

    percentage_sold_to_recipient = float(raw_input(yellow("Percentage of the stock sold to recipient: ")).replace(',','').replace('%','').replace('$',''))
    percentage_sold_to_recipient = percentage_sold_to_recipient / 100
    days_held_by_recipient = 365 - day_of_sale
    total_loss_allocated_to_recipient = loss_amount * percentage_sold_to_recipient
    loss_allocated_to_recipient = total_loss_allocated_to_recipient * (days_held_by_recipient / 365)

    str_solution = """
    Loss Allocated to Recipient Purchaser of S-Corp Stock with Losses: {0}
    from:
    Amount of S-Corp Loss on Stock: {1}
    Multiply: Percentage of S-Corp Stock sold to recipient: {2}%
    ____________________________________________________________________
    Total Possible Loss allocated: {3}
    Multiply: Days Held: {4} Divided By 365 Days
    ____________________________________________________________________
    Equals: Loss Allocated to Recipient: {0}
    """.format(
        str(loss_allocated_to_recipient),
        str(loss_amount),
        str(percentage_sold_to_recipient * 100),
        str(total_loss_allocated_to_recipient),
        str(days_held_by_recipient)
    )

    print green(str_solution)
    return

def option_seven(): # Problem 21: Analyzing AAA, AEP Accounts
    stock_basis = float(raw_input(yellow("Stock basis: ")).replace(',','').replace('%','').replace('$',''))
    aaa_balance = float(raw_input(yellow("Accumulated Adjustments Account Balance: ")).replace(',','').replace('%','').replace('$',''))
    aep_balance = float(raw_input(yellow("Accumulated Earnings and Profits Balance: ")).replace(',','').replace('%','').replace('$',''))
    distribution_received = float(raw_input(yellow("Distribution Received: ")).replace(',','').replace('%','').replace('$',''))
    remaining_stock_basis = stock_basis - aaa_balance
    to_calc_capital_gain = distribution_received - (aaa_balance + aep_balance)
    capital_gain = to_calc_capital_gain - remaining_stock_basis
    dividend = aep_balance

    str_solution = """
    Remaining Stock Basis to reduce Stock Basis to Zero: {0}
    Capital Gain = {1}
    Dividend = {2}, which equals the AEP Account

    From:
    Stock Basis {3}
    Less: Accumulated Adjustments Account Balance {4}
    ____________________________________________________________________
    Equals: Remaining Stock Basis {0}

    Distribution received {5}
    Less: Sum of AAA and AEP (Accumulated Earnings and Profits) {6}
    ____________________________________________________________________
    Equals: Amount to calculate Capital Gain {7}
    Less: Remaining Stock Basis {0}
    ____________________________________________________________________
    Equals: Capital Gain {1}

    """.format(
        str(remaining_stock_basis),
        str(capital_gain),
        str(dividend),
        str(stock_basis),
        str(aaa_balance),
        str(distribution_received),
        str(aaa_balance + aep_balance),
        str(to_calc_capital_gain)
    )

    print green(str_solution)
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
    # CHAPTER 14 Homework Problems:

    # 1 Problem # 11. Contributing Partner's Gain/Loss, Partnership Interest, and Partnership's Basis and Depreciation matters
    # 2 Problem # 15, land contributions to a LLC
    # 3 Problem # 16 Beginning and Ending Capital Accounts
    # 4 Problem # 30 Contributions with Qualified Nonrecourse Debt (Real Estate) and Schedule K-1 Reporting

    # Chapter 15 Homework Problems:

    # 5 Problem #12, Net Operating Losses, Suspended, and CArryforwards
    # 6 Problem #17 loss allocation of sold s-corp stock
    # 7 Problem #21: Analyzing AAA, AEP Accounts

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
