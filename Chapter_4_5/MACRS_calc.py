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

statutory_life = 0
convention = None

# need to put entire macrs table in here
def determine_convention():
    if forty_percent_rule == True:
        convention = 'mid_quarter'
    else:
        convention = 'half_year'

    return

def calc_macrs_mid_quarter():

    recovery_year = float(raw_input(cyan('What recovery YEAR is it?: ')).replace(',',''))
    type_property = float(raw_input(cyan('What year-type property is it?: ')).replace(',',''))
    recovery_quarter = float(raw_input(yellow('What recovery QUARTER is it?: ')).replace(',',''))
    acquisition_cost = float(raw_input(red('What is the ACQUISITION COST: ')).replace(',',''))
    if type_property == 3:
        if recovery_year == 1:
            macrs_dict = {
                1: 58.33,
                2: 41.67,
                3: 25,
                4: 8.33
            }
            applicable_percentage = macrs_dict[recovery_quarter]
            string = 'Your MACRS Applicable Percentage is: ' + string_applicable_percentage
            yellow(string)
            applicable_percentage = applicable_percentage / 100
            macrs_depr = acquisition_cost * applicable_percentage

            string = 'Your CURRENT YEAR MACRS Depreciation is: ' + str(macrs_depr)
            green(string)
        elif recovery_year == 2:
            macrs_dict = {
                1: 27.78,
                2: 38.89,
                3: 50,
                4: 61.11
            }
            applicable_percentage = macrs_dict[recovery_quarter]
            string = 'Your MACRS Applicable Percentage is: ' + string_applicable_percentage
            yellow(string)
            applicable_percentage = applicable_percentage / 100
            macrs_depr = acquisition_cost * applicable_percentage

            string = 'Your CURRENT YEAR MACRS Depreciation is: ' + str(macrs_depr)
            green(string)

        else:
            red('You have specified a INVALID Recovery Year')
            calc_macrs_mid_quarter()

    elif type_property == 5:
        if recovery_year == 1:
            macrs_dict = {
                1: 35,
                2: 25,
                3: 15,
                4: 5
            }
            applicable_percentage = macrs_dict[recovery_quarter]
            string = 'Your MACRS Applicable Percentage is: ' + string_applicable_percentage
            yellow(string)
            applicable_percentage = applicable_percentage / 100
            macrs_depr = acquisition_cost * applicable_percentage

            string = 'Your CURRENT YEAR MACRS Depreciation is: ' + str(macrs_depr)
            green(string)

        elif recovery_year == 2:
            macrs_dict = {
                1: 26,
                2: 30,
                3: 34,
                4: 38
            }
            applicable_percentage = macrs_dict[recovery_quarter]
            string = 'Your MACRS Applicable Percentage is: ' + string_applicable_percentage
            yellow(string)
            applicable_percentage = applicable_percentage / 100
            macrs_depr = acquisition_cost * applicable_percentage

            string = 'Your CURRENT YEAR MACRS Depreciation is: ' + str(macrs_depr)
            green(string)

        else:
            red('You have specified a INVALID Recovery Year')
            calc_macrs_mid_quarter()


    elif type_property == 7:
        if recovery_year == 1:
            macrs_dict = {
                1: 25,
                2: 17.85,
                3: 10.71,
                4: 3.57
            }
            applicable_percentage = macrs_dict[recovery_quarter]
            string = 'Your MACRS Applicable Percentage is: ' + string_applicable_percentage
            yellow(string)
            applicable_percentage = applicable_percentage / 100
            macrs_depr = acquisition_cost * applicable_percentage

            string = 'Your CURRENT YEAR MACRS Depreciation is: ' + str(macrs_depr)
            green(string)

        elif recovery_year == 2:
            macrs_dict = {
                1: 21.43,
                2: 23.47,
                3: 25.51,
                4: 27.55
            }
            applicable_percentage = macrs_dict[recovery_quarter]
            string = 'Your MACRS Applicable Percentage is: ' + string_applicable_percentage
            yellow(string)
            applicable_percentage = applicable_percentage / 100
            macrs_depr = acquisition_cost * applicable_percentage

            string = 'Your CURRENT YEAR MACRS Depreciation is: ' + str(macrs_depr)
            green(string)

        else:
            red('You have specified a INVALID Recovery Year')
            calc_macrs_mid_quarter()


    else:
        red('You have specified a INVALID Year-Type Property')
        calc_macrs_mid_quarter()

    # write the answer to a csv file
    timestr = time.strftime("%Y%m%d-%H%M%S")
    saved_answer = './solutions/answer_MACRS_calculation_mid_quarter' + timestr + '.csv'
    w = open(saved_answer,'a+')
    write_string = 'MACRS Applicable Percentage: ' + str(applicable_percentage) + '%' + '\n'
    w.write(write_string)
    write_string = 'MACRS ANNUAL Depreciation: ' + str(macrs_depr) + '\n'
    w.write(write_string)
    w.close()
    string = 'Your answers are saved at: ' + saved_answer
    green(string)
    main()
    return

def calc_macrs_half_year():
    recovery_year = float(raw_input(cyan('What recovery_year is it?: ')).replace(',',''))
    type_property = float(raw_input(cyan('What year-type property is it?: ')).replace(',',''))
    acquisition_cost = float(raw_input(cyan('What is the acquisition_cost? (Enter the remaining basis if from the comprehensive question): ')).replace(',',''))
    if type_property == 3:
        macrs_dict = {
            1: 33.33,
            2: 44.45,
            3: 14.81,
            4: 7.41
        }
        applicable_percentage = macrs_dict[recovery_year]
        string_applicable_percentage = str(applicable_percentage)
        string = 'Your MACRS Applicable Percentage is: ' + string_applicable_percentage
        yellow(string)
        applicable_percentage = applicable_percentage / 100
        macrs_depr = acquisition_cost * applicable_percentage

        string = 'Your CURRENT YEAR MACRS Depreciation is: ' + str(macrs_depr)
        green(string)

    elif type_property == 5:
        macrs_dict = {
            1: 20,
            2: 32,
            3: 19.20,
            4: 11.52,
            5: 11.52,
            6: 5.76
        }
        applicable_percentage = float(macrs_dict[recovery_year])
        string_applicable_percentage = str(applicable_percentage) + '%'
        applicable_percentage = applicable_percentage / 100
        macrs_depr = acquisition_cost * applicable_percentage
        string = 'Your MACRS Applicable Percentage is: ' + string_applicable_percentage
        yellow(string)
        string = 'Your CURRENT YEAR MACRS Depreciation is: ' + str(macrs_depr)
        green(string)


    elif type_property == 7:
        macrs_dict = {
            1: 14.29,
            2: 24.49,
            3: 17.49,
            4: 12.49,
            5: 8.93,
            6: 8.92,
            7: 8.93,
            8: 4.46
        }
        applicable_percentage = macrs_dict[recovery_year]
        string_applicable_percentage = str(applicable_percentage) + '%'
        string = 'Your MACRS Applicable Percentage is: ' + string_applicable_percentage
        yellow(string)
        applicable_percentage = applicable_percentage / 100
        macrs_depr = acquisition_cost * applicable_percentage

        string = 'Your CURRENT YEAR MACRS Depreciation is: ' + str(macrs_depr)
        green(string)


    elif type_property == 10:
        macrs_dict = {
            1: 10.00,
            2: 18.00,
            3: 14.40,
            4: 11.52,
            5: 9.22,
            6: 7.37,
            7: 6.55,
            8: 6.55,
            9: 6.56,
            10: 6.55,
            11: 3.28
        }
        applicable_percentage = macrs_dict[recovery_year]
        string = 'Your MACRS Applicable Percentage is: ' + string_applicable_percentage
        yellow(string)
        applicable_percentage = applicable_percentage / 100
        macrs_depr = acquisition_cost * applicable_percentage

        string = 'Your CURRENT YEAR MACRS Depreciation is: ' + str(macrs_depr)
        green(string)


    elif type_property == 15:
        macrs_dict = {
            1: 5,
            2: 9.5,
            3: 8.55,
            4: 7.7,
            5: 6.93,
            6: 6.23,
            7: 5.9,
            8: 5.9,
            9: 5.91,
            10: 5.9,
            11: 5.91,
            12: 5.9,
            13: 5.91,
            14: 5.9,
            15: 5.91,
            16: 2.95
        }
        applicable_percentage = macrs_dict[recovery_year]
        string = 'Your MACRS Applicable Percentage is: ' + string_applicable_percentage
        yellow(string)
        applicable_percentage = applicable_percentage / 100
        macrs_depr = acquisition_cost * applicable_percentage

        string = 'Your CURRENT YEAR MACRS Depreciation is: ' + str(macrs_depr)
        green(string)


    elif type_property == 20:
        macrs_dict = {
            1: 3.75,
            2: 7.219,
            3: 6.677,
            4: 6.177,
            5: 5.713,
            6: 5.285,
            7: 4.888,
            8: 4.522,
            9: 4.462,
            10: 4.461,
            11: 4.462,
            12: 4.461,
            13: 4.462,
            14: 4.461,
            15: 4.462,
            16: 4.461,
            17: 4.462,
            18: 4.461,
            19: 4.462,
            20: 4.461,
            21: 2.231
        }
        applicable_percentage = macrs_dict[recovery_year]
        string = 'Your MACRS Applicable Percentage is: ' + string_applicable_percentage
        yellow(string)
        applicable_percentage = applicable_percentage / 100
        macrs_depr = acquisition_cost * applicable_percentage

        string = 'Your CURRENT YEAR MACRS Depreciation is: ' + str(macrs_depr)
        green(string)



    else:
        red('You have entered a invalid MACRS property type')
        calc_macrs_half_year()

    # write the answer to a csv file
    timestr = time.strftime("%Y%m%d-%H%M%S")
    saved_answer = './solutions/answer_MACRS_calculation_half_year' + timestr + '.csv'
    w = open(saved_answer,'a+')
    write_string = 'MACRS Applicable Percentage: ' + str(applicable_percentage) + '%' + '\n'
    w.write(write_string)
    write_string = 'MACRS ANNUAL Depreciation: ' + str(macrs_depr) + '\n'
    w.write(write_string)
    w.close()
    string = 'Your answers are saved at: ' + saved_answer
    green(string)

    main()
    return macrs_depr
def calc_macrs_realty_top():
    yellow('27.5 Year Non-residential real property')
    recovery_year = float(raw_input(cyan('What recovery year is it?: ')))
    if recovery_year == 1:
        recovery_month = float(raw_input(cyan('What recovery month is it?: ')))
        applicable_percentage_dict = {
            1: 3.485,
            2: 3.182,
            3: 2.879,
            4: 2.576,
            5: 2.273,
            6: 1.970,
            7: 1.667,
            8: 1.364,
            9: 1.061,
            10: 0.758,
            11: 0.455,
            12: 0.152
        }
        applicable_percentage = applicable_percentage_dict[recovery_month]
        applicable_percentage = applicable_percentage / 100
        string = 'Your applicable percentage rate is: ' + str(applicable_percentage)
        yellow(string)
        acquisition_cost = float(raw_input(cyan('Enter the acquisition cost for the asset: ')).replace(',',''))
        macrs_depr = acquisition_cost * applicable_percentage
        print green('Your CURRENT YEAR MACRS Depreciation is: ' + str(macrs_depr))
        return macrs_depr
    elif 2 <= recovery_year <= 18:
        recovery_month = float(raw_input(cyan('What recovery month is it?: ')))
        applicable_percentage = 3.636
        applicable_percentage = applicable_percentage / 100
        string = 'Your applicable percentage rate is: ' + str(applicable_percentage)
        yellow(string)
        acquisition_cost = float(raw_input(cyan('Enter the acquisition cost for the asset: ')).replace(',',''))
        macrs_depr = acquisition_cost * applicable_percentage
        print green('Your CURRENT YEAR MACRS Depreciation is: ' + str(macrs_depr))
        return macrs_depr
    elif 19 <= recovery_year <= 27:
        applicable_percentage = 3.637
        applicable_percentage = applicable_percentage / 100
        string = 'Your applicable percentage rate is: ' + str(applicable_percentage)
        yellow(string)
        acquisition_cost = float(raw_input(cyan('Enter the acquisition cost for the asset: ')).replace(',',''))
        macrs_depr = acquisition_cost * applicable_percentage
        print green('Your CURRENT YEAR MACRS Depreciation is: ' + str(macrs_depr))
        return macrs_depr
    elif recovery_year == 28:
        applicable_percentage_dict = {
            1: 3.485,
            2: 3.182,
            3: 2.879,
            4: 2.576,
            5: 2.273,
            6: 1.970,
            7: 1.667,
            8: 1.364,
            9: 1.061,
            10: 0.758,
            11: 0.455,
            12: 0.152
        }
        recovery_month = float(raw_input(cyan('What recovery month is it?: ')))
        if 7 <= recovery_month <= 12:
            applicable_percentage = 3.636
        else:
            applicable_percentage = applicable_percentage_dict[recovery_month]
        applicable_percentage = applicable_percentage / 100
        string = 'Your applicable percentage rate is: ' + str(applicable_percentage)
        yellow(string)
        acquisition_cost = float(raw_input(cyan('Enter the acquisition cost for the asset: ')).replace(',',''))
        macrs_depr = acquisition_cost * applicable_percentage
        print green('Your CURRENT YEAR MACRS Depreciation is: ' + str(macrs_depr))
        main()
        return macrs_depr
    elif recovery_year == 29:
        applicable_percentage_dict = {
            7: 0.152,
            8: 0.455,
            9: 0.758,
            10: 1.061,
            11: 1.364,
            12: 1.667
        }

        recovery_month = float(raw_input("What recovery month is it? Enter a number: ").replace(',',''))
        if 1 <= recovery_month <= 6:
            applicable_percentage = 0.000
        else:
            applicable_percentage = applicable_percentage_dict[recovery_month]
        applicable_percentage = applicable_percentage / 100
        string = 'Your applicable percentage rate is: ' + str(applicable_percentage)
        yellow(string)
        acquisition_cost = float(raw_input(cyan('Enter the acquisition cost for the asset: ')).replace(',',''))
        macrs_depr = acquisition_cost * applicable_percentage
        print green('Your CURRENT YEAR MACRS Depreciation is: ' + str(macrs_depr))
        main()
        return macrs_depr
    else:
        red('This asset cannot be recovered')
        main()
    recovery_month = float(raw_input(cyan('What recovery month is it?: ')))
    return macrs_depr
def calc_macrs_realty_middle():
    yellow('31.5 Year Non-residential Real Property')
    recovery_year = float(raw_input(cyan('What recovery year is it?: ')))
    if recovery_year == 1:
        applicable_percentage_dict = {
            1: 3.042,
            2: 2.778,
            3: 2.513,
            4: 2.249,
            5: 1.984,
            6: 1.720,
            7: 1.455,
            8: 1.190,
            9: 0.926,
            10: 0.661,
            11: 0.397,
            12: 0.132
        }
        recovery_month = float(raw_input(cyan('What recovery month is it?: ')))
        applicable_percentage = applicable_percentage_dict[recovery_month]
        applicable_percentage = applicable_percentage / 100
        string = 'Your applicable percentage rate is: ' + str(applicable_percentage)
        yellow(string)
        acquisition_cost = float(raw_input(cyan('Enter the acquisition cost for the asset: ')).replace(',',''))
        macrs_depr = acquisition_cost * applicable_percentage
        print green('Your CURRENT YEAR MACRS Depreciation is: ' + str(macrs_depr))
        main()

    elif 2 <= recovery_year <= 19:
        applicable_percentage = 3.175
        applicable_percentage = applicable_percentage / 100
        string = 'Your applicable percentage rate is: ' + str(applicable_percentage)
        yellow(string)
        acquisition_cost = float(raw_input(cyan('Enter the acquisition cost for the asset: ')).replace(',',''))
        macrs_depr = acquisition_cost * applicable_percentage
        print green('Your CURRENT YEAR MACRS Depreciation is: ' + str(macrs_depr))
        main()
    elif 20 <= recovery_year <= 31:
        applicable_percentage = 3.174
        applicable_percentage = applicable_percentage / 100
        string = 'Your applicable percentage rate is: ' + str(applicable_percentage)
        yellow(string)
        acquisition_cost = float(raw_input(cyan('Enter the acquisition cost for the asset: ')).replace(',',''))
        macrs_depr = acquisition_cost * applicable_percentage
        print green('Your CURRENT YEAR MACRS Depreciation is: ' + str(macrs_depr))
        main()
    elif recovery_year == 32:
        applicable_percentage_dict = {
            1: 1.720,
            2: 1.984,
            3: 2.249,
            4: 2.513,
            5: 2.778,
            6: 3.042
        }
        recovery_month = float(raw_input("Enter the recovery MONTH: "))
        if 7 <= recovery_month <= 12:
            applicable_percentage = 3.175
        else:
            applicable_percentage = applicable_percentage_dict[recovery_month]
        applicable_percentage = applicable_percentage / 100
        string = 'Your applicable percentage rate is: ' + str(applicable_percentage)
        yellow(string)
        acquisition_cost = float(raw_input(cyan('Enter the acquisition cost for the asset: ')).replace(',',''))
        macrs_depr = acquisition_cost * applicable_percentage
        print green('Your CURRENT YEAR MACRS Depreciation is: ' + str(macrs_depr))
        main()
    elif recovery_year == 33:
        recovery_month = float(raw_input(cyan('What recovery MONTH is it?: ')))
        if 1 <= recovery_month <= 6:
            applicable_percentage = 0.0000
        else:
            applicable_percentage_dict = {
                7: 0.132,
                8: 0.397,
                9: 0.661,
                10: 0.926,
                11: 1.190,
                12: 1.455
            }
            applicable_percentage = applicable_percentage_dict[recovery_month]
        applicable_percentage = applicable_percentage / 100
        string = 'Your applicable percentage rate is: ' + str(applicable_percentage)
        yellow(string)
        acquisition_cost = float(raw_input(cyan('Enter the acquisition cost for the asset: ')).replace(',',''))
        macrs_depr = acquisition_cost * applicable_percentage
        print green('Your CURRENT YEAR MACRS Depreciation is: ' + str(macrs_depr))
        main()
    # write the answer to a csv file
    timestr = time.strftime("%Y%m%d-%H%M%S")
    saved_answer = './solutions/answer_MACRS_calculation_realty_mid_month_convention' + timestr + '.csv'
    w = open(saved_answer,'a+')
    write_string = 'MACRS Applicable Percentage: ' + str(applicable_percentage) + '%' + '\n'
    w.write(write_string)
    write_string = 'MACRS ANNUAL Depreciation: ' + str(macrs_depr) + '\n'
    w.write(write_string)
    w.close()
    string = 'Your answers are saved at: ' + saved_answer
    green(string)
    return
def calc_macrs_realty_bottom():
    yellow('39-YEAR Non-residential Real Property')
    recovery_year = float(raw_input(cyan('What recovery year is it?: ')).replace(',',''))

    if recovery_year == 1:
        applicable_percentage_dict = {
            '1': 2.461,
            '2': 2.247,
            '3': 2.033,
            '4': 1.819,
            '5': 1.605,
            '6': 1.391,
            '7': 1.177,
            '8': 0.963,
            '9': 0.749,
            '10': 0.535,
            '11': 0.321,
            '12': 0.107
        }

        recovery_month = str(raw_input("What recovery month is it? Enter a number: ").replace(',',''))
        applicable_percentage = applicable_percentage_dict[recovery_month]
        applicable_percentage = applicable_percentage / 100
        string = 'Your applicable percentage rate is: ' + str(applicable_percentage)
        yellow(string)
        acquisition_cost = float(raw_input(cyan('Enter the acquisition cost for the asset: ')).replace(',',''))
        macrs_depr = acquisition_cost * applicable_percentage
        print green('Your CURRENT YEAR MACRS Depreciation is: ' + str(macrs_depr))
        main()


    elif 2 <= recovery_year <= 39:
        applicable_percentage = 2.564
        applicable_percentage = applicable_percentage / 100
        string = 'Your applicable percentage rate is: ' + str(applicable_percentage)
        yellow(string)
        acquisition_cost = float(raw_input(cyan('Enter the acquisition cost for the asset: ')).replace(',',''))
        macrs_depr = acquisition_cost * applicable_percentage
        print green('Your CURRENT YEAR MACRS Depreciation is: ' + str(macrs_depr))
        main()
    elif recovery_year == 40:
        applicable_percentage_dict = {
            '1': 0.107,
            '2': 0.321,
            '3': 0.535,
            '4': 0.749,
            '5': 0.963,
            '6': 1.177,
            '7': 1.391,
            '8': 1.605,
            '9': 1.819,
            '10': 2.033,
            '11': 2.247,
            '12': 2.461
        }
        recovery_month = str(raw_input(cyan("What recovery month is it? Enter a number: ")).replace(',',''))
        applicable_percentage = applicable_percentage_dict[recovery_month]
        applicable_percentage = applicable_percentage / 100
        string = 'Your applicable percentage rate is: ' + str(applicable_percentage)
        yellow(string)
        acquisition_cost = float(raw_input(cyan('Enter the acquisition cost for the asset: ')).replace(',',''))
        macrs_depr = acquisition_cost * applicable_percentage
        print green('Your CURRENT YEAR MACRS Depreciation is: ' + str(macrs_depr))
    # write the answer to a csv file
    timestr = time.strftime("%Y%m%d-%H%M%S")
    saved_answer = './solutions/answer_MACRS_calculation_realty_mid_month_convention' + timestr + '.csv'
    w = open(saved_answer,'a+')
    write_string = 'MACRS Applicable Percentage: ' + str(applicable_percentage) + '%' + '\n'
    w.write(write_string)
    write_string = 'MACRS ANNUAL Depreciation: ' + str(macrs_depr) + '\n'
    w.write(write_string)
    w.close()
    string = 'Your answers are saved at: ' + saved_answer
    green(string)

    main()
    return

def find_macrs_depr(calc_selected):


    if calc_selected == "MACRS-Personalty":
        mid_quarter_cutoff_date = 'October 1st'
        yellow('The Mid-Quarter Cutoff Date is last 1/4 of year, or if using regular annual years, October 1st')
        mq_question = str(raw_input(cyan('Is your property on or after October 1st?: ')))
        if mq_question == "y":
            # percentage_assets_question = str(raw_input(cyan('How much of a percentage is placed in the last quarter?: ')))
            percentage_assets_question = float(raw_input(cyan('How much of a percentage is placed in the last quarter? No decimals or punctuation: ')))
            percentage_assets_question = percentage_assets_question / 100

            if percentage_assets_question > 0.4:
                convention = 'Mid-Quarter'
            else:
                convention = 'Half-Year'
        elif mq_question == "n":
            convention = 'Half-Year'
        else:
            red('You have entered a invalid option')
            find_macrs_depr()

        if convention == "Mid-Quarter":
            calc_macrs_mid_quarter()
        elif convention == "Half-Year":
            calc_macrs_half_year()
    elif calc_selected == "MACRS-Realty":
        depreciation_method = 'Straight-Line'
        convention = 'Mid-Month'
        print """
        # 1. Residential rental real-estate placed in service after December 31, 1986
        # 2. Non-residential real property placed in services between December 31, 1986 and before May 13, 1993
        # 3. Non-residential real property placed in service after May 12, 1993
        """
        realty_property_question = str(raw_input("What type of property is it?: "))
        if realty_property_question == "1":
            macrs_table = '5.6_top'
        elif realty_property_question == "2":
            macrs_table = '5.6_middle'
        elif realty_property_question == "3":
            macrs_table = '5.6_bottom'
        else:
            red('You have entered a invalid option')
            find_macrs_depr()

        if macrs_table == '5.6_top':
            calc_macrs_realty_top()
        elif macrs_table == '5.6_middle':
            calc_macrs_realty_middle()
        elif macrs_table == '5.6_bottom':
            calc_macrs_realty_bottom()
    elif calc_selected == "S179_Additional_Depr_MACRS":
            s179_addi_macrs_calc()

    return

def find_macrs_straight_line_half_year():

    timestr = time.strftime("%Y%m%d-%H%M%S")
    type_property = float(raw_input(cyan('Enter the MACRS Year-Class: ')).replace(',',''))
    acquisition_cost = float(raw_input(cyan('Enter the acquisition cost of the property: ')).replace(',',''))
    recovery_year = float(raw_input(cyan('Enter the RECOVERY YEAR: ')).replace(',',''))
    if type_property == 3:
        macrs_dict = {
            1: 16.67,
            2: 33.33,
            3: 33.33,
            4: 16.67
        }
        saved_answer = './solutions/macrs_straight_line_solution' + timestr + '.csv'
        w = open(saved_answer,'a+')

        applicable_percentage = macrs_dict[recovery_year]
        applicable_percentage = applicable_percentage / 100
        macrs_depr = acquisition_cost * applicable_percentage

    elif type_property == 5:
        macrs_dict = {
            1: 10,
            2: 20,
            3: 20,
            4: 20,
            5: 20,
            6: 10
        }
        saved_answer = './solutions/macrs_straight_line_solution' + timestr + '.csv'
        w = open(saved_answer,'a+')

        applicable_percentage = macrs_dict[recovery_year]
        applicable_percentage = applicable_percentage / 100
        macrs_depr = acquisition_cost * applicable_percentage

    elif type_property == 7:
        macrs_dict = {
            1: 7.14,
            2: 14.29,
            3: 14.29,
            4: 14.29,
            5: 14.29,
            6: 14.29,
            7: 14.29,
            8: 7.14
        }
        saved_answer = './solutions/macrs_straight_line_solution' + timestr + '.csv'
        w = open(saved_answer,'a+')

        applicable_percentage = macrs_dict[recovery_year]
        applicable_percentage = applicable_percentage / 100
        macrs_depr = acquisition_cost * applicable_percentage

    elif type_property == 10:
        macrs_dict = {
            1: 5,
            2: 10,
            3: 10,
            4: 10,
            5: 10,
            6: 10,
            7: 10,
            8: 10,
            9: 10,
            10: 10,
            11: 5
        }
        saved_answer = './solutions/macrs_straight_line_solution' + timestr + '.csv'
        w = open(saved_answer,'a+')

        applicable_percentage = macrs_dict[recovery_year]
        applicable_percentage = applicable_percentage / 100
        macrs_depr = acquisition_cost * applicable_percentage

    elif type_property == 15:
        macrs_dict = {
            1: 3.33,
            2: 6.67,
            3: 6.67,
            4: 6.67,
            5: 6.67,
            6: 6.67,
            7: 6.67,
            8: 6.67,
            9: 6.67,
            10: 6.67,
            11: 6.67,
            12: 6.67,
            13: 6.67,
            14: 6.67,
            15: 6.67,
            16: 3.33
        }
        saved_answer = './solutions/macrs_straight_line_solution' + timestr + '.csv'
        w = open(saved_answer,'a+')

        applicable_percentage = macrs_dict[recovery_year]
        applicable_percentage = applicable_percentage / 100
        macrs_depr = acquisition_cost * applicable_percentage

    elif type_property == 20:
        macrs_dict = {
            1: 2.5,
            2: 5,
            3: 5,
            4: 5,
            5: 5,
            6: 5,
            7: 5,
            8: 5,
            9: 5,
            10: 5,
            11: 5,
            12: 5,
            13: 5,
            14: 5,
            15: 5,
            16: 5,
            17: 5,
            18: 5,
            19: 5,
            20: 5,
            21: 2.5
        }
        saved_answer = './solutions/macrs_straight_line_solution' + timestr + '.csv'
        w = open(saved_answer,'a+')

        applicable_percentage = macrs_dict[recovery_year]
        applicable_percentage = applicable_percentage / 100
        macrs_depr = acquisition_cost * applicable_percentage

    else:
        red('You have entered a invalid option')
        find_macrs_straight_line_half_year()

    string = 'Your MACRS Depreciation is: ' + str(macrs_depr)
    green(string)
    w.write(string + '\n')
    remaining_basis = acquisition_cost - macrs_depr
    string = 'Your remaining BASIS is: ' + str(remaining_basis)
    yellow(string)
    w.write(string + '\n')
    w.close()

    string = 'Your solution is located at: ' + saved_answer

    yellow(string)
    main()
    return

def find_ADS_alternative_minimum_tax():
    return


def find_s179_calc():
    timestr = time.strftime("%Y%m%d-%H%M%S")

    basis = float(raw_input(cyan('Enter the amount of S179 Property that has been placed into service for this year: ')).replace(',',''))

    if basis >= 2540000: # meaning that al dollar for dollar deductions are complete consumed
        s179_deduction = 0
        red('NO S-179 DEDUCTION ALLOWED: Too much S179 assets, exceeds $2,030,000 + 510,000')
        main()
    elif basis <= 2030000: # if its at or under $2,030,000
        s179_deduction = 510000
    else: # in the event that it egins to exceed $2,030,000
        s179_deduction = 510000 - (basis - 2030000)
    basis = basis - s179_deduction

    saved_answer = './solutions/s179_single_problem_solution' + timestr + '.csv'
    w = open(saved_answer,'a+')

    string = 'SECTION 179 DEDUCTION: ' + str(s179_deduction)
    green(string)
    w.write(string + '\n')

    string = 'NEW BASIS AFTER DEDUCTION: ' + str(basis)
    yellow(string)
    w.write(string + '\n')

    saved_answer = './solutions/s179_solution' + timestr + '.csv'
    w.close()
    main()
    return
def s179_addi_macrs_calc():
    # print """
    # What kind of property are you calculating deductions for?
    #
    # # 1. MACRS Personalty
    # # 2. MACRS Reality
    #
    # """
    #
    # opt_choice = str(raw_input(cyan('Enter a OPTION: ')))
    #
    # if opt_choice == '1':
    #     calc_selected = 'MACRS-Personalty'
    #
    # # elif opt_choice == '2':
    # #     calc_selected = "MACRS-Realty"
    #
    # else:
    #     red('You have entered a invalid option')
    #     s179_addi_macrs_calc()

    basis = float(raw_input(cyan('Enter the amount of S179 Property that has been placed into service for this year: ')).replace(',',''))

    if basis >= 2540000: # meaning that al dollar for dollar deductions are complete consumed
        s179_deduction = 0
        red('NO S-179 DEDUCTION ALLOWED: Too much S179 assets, exceeds $2,030,000 by twice the amount')
        main()
    elif basis <= 2030000: # if its at or under $2,030,000
        s179_deduction = 510000
    else: # in the event that it egins to exceed $2,030,000
        s179_deduction = 510000 - (basis - 2030000)
    basis = basis - s179_deduction
    # additional 50% Depr
    # basis = basis - (basis * 0.5)
    additional_fifty_depr = basis * 0.5
    basis = basis - additional_fifty_depr
    # MACRS depr

    # new_basis = basis - s179_deduction - additional_fifty_depr - macrs_depr
    timestr = time.strftime("%Y%m%d-%H%M%S")
    # Open a new *.csv file to save answer
    saved_answer = './solutions/comprehensive_question_solution_s179_macrs_additionalbonus' + timestr + '.csv'
    w = open(saved_answer,'a+')
    string = 'SECTION 179 DEDUCTION TAKEN: ' + str(s179_deduction)
    green(string)
    w.write(string + '\n')
    string = 'ADDITIONAL 50% BONUS DEDUCTION TAKEN: ' + str(additional_fifty_depr)
    green(string)
    w.write(string + '\n')
    string = 'REMAINING BASIS: ' + str(basis)
    red(string)
    w.write(string + '\n')
    # find the final macrs deprciation
    # macrs_depr = find_macrs_depr(calc_selected)
    macrs_depr = float(raw_input(yellow('Please enter the separately calculated MACRS Depreciation because Stack Overflow cant answer shit for a question on returning values properly: ')).replace(',',''))
    basis = basis - macrs_depr
    string = 'FINAL BASIS AFTER DEDUCTIONS: ' + str(basis)
    green(string)
    w.write(string + '\n')
    string = 'SECTION 179 DEDUCTION TAKEN: ' + str(s179_deduction)
    yellow(string)
    w.write(string + '\n')
    string = 'ADDITIONAL 50% BONUS DEDUCTION TAKEN: ' + str(additional_fifty_depr)
    yellow(string)
    w.write(string + '\n')

    string = 'MACRS DEPRECIATION TAKEN: ' + str(macrs_depr)
    yellow(string)
    w.write(string + '\n')
    total_depreciation_current_year = s179_deduction + additional_fifty_depr + macrs_depr
    string = 'TOTAL DEPRECIATION TAKEN: ' + str(total_depreciation_current_year)
    yellow(string)
    w.write(string + '\n')
    w.close()
    string = '\nYour solution is located here: ' + saved_answer
    green(string)
    main()
    return macrs_depr
def main():
    print """
    #0. Return to Main MENU
    #1. MACRS-Personalty
    #2. MACRS-Realty
    #3. Section 179 + Additional Depr + MACRS Calculator
    #4. Section 179 Calculator
    #5. Additional Bonus Depr Calculator
    #6. MACRS Straight-Line Half-Year
    #7. Alternative Minimum Tax Tax Calculator
    """

    opt_choice = str(raw_input("Enter a OPTION: "))

    if opt_choice == "0":
        go_back_main_menu_module()
    elif opt_choice == "1":
        calc_selected = 'MACRS-Personalty'
        cyan(calc_selected)
        find_macrs_depr(calc_selected)
    elif opt_choice == "2":
        calc_selected = "MACRS-Realty"
        cyan(calc_selected)
        find_macrs_depr(calc_selected)
    elif opt_choice == "3":
        calc_selected = "S179_Additional_Depr_MACRS"
        cyan(calc_selected)
        find_macrs_depr(calc_selected)
    elif opt_choice == "4":
        find_s179_calc()
    elif opt_choice == "6":
        find_macrs_straight_line_half_year()
    else:
        red('You have entered a invalid option')
        main()
    return
main()
