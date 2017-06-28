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
def calculate_theft_complete_casualty():
    adjusted_basis = float(raw_input(yellow("Enter the ADJUSTED BASIS of the stolen or completely lost asset: ")).replace(',','').replace('$',''))
    insurance_proceeds = float(raw_input(yellow("Enter the INSURANCE PROCEEDS RECEIVED for the asset: ")).replace(',','').replace('$',''))
    deduction = adjusted_basis - insurance_proceeds
    str_solution = "DEDUCTION: %s from %s - %s" % (
        str(deduction),
        str(adjusted_basis),
        str(insurance_proceeds)
        )
    print green(str_solution)
    save_solution('theft_complete_casualty_deduction',str_solution)
    return

def calculate_partial_casualty():

    FMV_begin = float(raw_input(yellow("Enter the FMV BEFORE the casualty event for the asset (or enter the decline in value here and a '0' in the next question): ")).replace(',','').replace('$',''))
    FMV_end = float(raw_input(yellow("Enter the FMV AFTER the casualty eventy for the asset: ")).replace(',','').replace('$',''))
    insurance_proceeds = float(raw_input(yellow("Enter the INSURANCE PROCEEDS RECEIVED for the asset: ")).replace(',','').replace('$',''))

    decline_val = FMV_begin - FMV_end

    # find the lesser of....
    if decline_val < adjusted_basis:
        subtract_from = decline_val
    elif adjusted_basis > decline_val:
        subtract_from = adjusted_basis

    deduction = subtract_from - insurance_proceeds
    str_solution = "DEDUCTION: %s from %s - %s" % (
        str(deduction),
        str(subtract_from),
        str(insurance_proceeds)
        )
    print green(str_solution)
    save_solution('partial_casualty_deduction',str_solution)
    return

def main():
    print """
    Is this casualty event a...
    1. Theft or Complete Casualty Loss?
    2. Partial Casualty Loss?
    """

    opt_choice = float(raw_input(yellow("Enter a OPTION: ")).replace(',','').replace('$',''))

    if opt_choice == 1:
        os.system('clear')
        calculate_theft_complete_casualty()
        main()
    elif opt_choice == 2:
        os.system('clear')
        calculate_partial_casualty()
        main()
    else:
        print red("You have entered a invalid option")
        main()
    return
main()
