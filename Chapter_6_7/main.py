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

def bad_debts():
    os.system('python /root/Documents/ACC_410_Exam_Calculator_Project/Chapter_6_7/bad_debts.py')
    return

def casualty_and_theft():
    os.system('python /root/Documents/ACC_410_Exam_Calculator_Project/Chapter_6_7/casualty_and_theft.py')
    return

def net_operating_losses():
    os.system('python /root/Documents/ACC_410_Exam_Calculator_Project/Chapter_6_7/nol.py')
    return

def at_risk_losses():
    os.system('python /root/Documents/ACC_410_Exam_Calculator_Project/Chapter_6_7/at_risk.py')
    return

def passive_activity_losses():
    os.system('python /root/Documents/ACC_410_Exam_Calculator_Project/Chapter_6_7/passive_activity_losses.py')
    return

def main():
    print cyan("Chapters 6 and 7, Exam #2")
    print """
    # 1. Bad Debts
    # 2. Casualty and Theft Losses
    # 3. Net Operating Losses
    # 4. At-Risk Losses
    # 5. Passive Activity Losses
    # 0. Return to Main Menu
    """

    opt_choice = float(raw_input(yellow("Enter a OPTION: ")).replace(',',''))

    if opt_choice == 1:
        os.system('clear')
        bad_debts()
        main()
    elif opt_choice == 2:
        os.system('clear')
        casualty_and_theft()
        main()
    elif opt_choice == 3:
        os.system('clear')
        net_operating_losses()
        main()
    elif opt_choice == 4:
        os.system('clear')
        at_risk_losses()
        main()
    elif opt_choice == 5:
        os.system('clear')
        passive_activity_losses()
        main()
    elif opt_choice == 0:
        os.system('clear')
        go_back_main_menu_module()
    else:
        print red("You have entered a invalid option")
        main()
    return
main()
