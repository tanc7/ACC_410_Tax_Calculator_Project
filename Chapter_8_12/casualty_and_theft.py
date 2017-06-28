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

def opt_1():
    os.system('python /root/Documents/ACC_410_Exam_Calculator_Project/Chapter_8_12/insurance_and_c_and_t.py')
    return

def opt_2():
    os.system('python /root/Documents/ACC_410_Exam_Calculator_Project/Chapter_8_12/c_and_t_deduction_calc.py')
    return

def opt_3():
    os.system('python /root/Documents/ACC_410_Exam_Calculator_Project/Chapter_8_12/c_and_t_gain_loss_calc.py')
    return


def main():
    print cyan("CASUALTY & THEFT LOSSES")

    print """
    # 1. Factoring Insurance into C & T Losses Calculator
    # 2. C & T Deduction Calculator
    # 3. C & T Gains/Losses Calculator
    # 0. Return to Main Menu
    """

    opt_choice == float(raw_input(yellow("Enter a OPTION: ")).replace(',',''))

    if opt_choice == 1:
        os.system('clear')
        opt_1()
        main()
    elif opt_choice == 2:
        os.system('clear')
        opt_2()
        main()
    elif opt_choice == 3:
        os.system('clear')
        opt_3()
        main()
    elif opt_choice == 0:
        os.system('clear')
        go_back_main_menu_module()
    else:
        print red("You have entered a invalid option")
        main()
    return
main()
