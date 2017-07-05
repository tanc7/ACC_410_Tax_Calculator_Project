from termcolor import colored
import os
import sys
import socket
import StringIO
import time
import operator
# os.chdir('/root/Documents/ACC_410_Exam_Calculator_Project')
os.chdir('/root/Documents/ACC_410_Exam_Calculator_Project/Chapter_14_15/')
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

def homework_problems():
    os.system("python /root/Documents/ACC_410_Exam_Calculator_Project/Chapter_14_15/homework_problems.py")
    return

def chapter_14_15_calculators():
    return
def main():
    print cyan("Chapters 6 and 7, Exam #2")
    print """
    # 1. Homework Problems
    # 2. Calculators
    """

    opt_choice = float(raw_input(yellow("Enter a OPTION: ")).replace(',',''))

    if opt_choice == 1:
        os.system('clear')
        homework_problems()
        main()
    elif opt_choice == 2:
        os.system('clear')
        chapter_14_15_calculators()
        main()
    elif opt_choice == 0:
        os.system('clear')
        go_back_main_menu_module()
    else:
        print red("You have entered a invalid option")
        main()
    return
main()
