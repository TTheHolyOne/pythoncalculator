import pyfiglet
import pprint
import colorama
import sys
import time
from colorama import init
from colorama import Fore, Back, Style
init()
def quitornot():
    quitornot = input('\n\nWould you like to quit? (Y/N) \n')
    if quitornot.lower() == 'y':
        print('Shutting down...')
        sys.exit()
    elif quitornot.lower() == 'n':
        calculator()
def clear_screen():
  print("\n"*100) # just prints empty lines to move everything else up
ascii_banner = pyfiglet.figlet_format("TTheHolyOne")
ascii_banner1 = pyfiglet.figlet_format("github.com/ttheholyone", font = 'short')
print(Fore.RED + ascii_banner.lower())
print(Fore.BLUE + ascii_banner1.lower())
print(Fore.YELLOW + 'This program is a advance calculator that allows you to perform calculations using two numbers and a character that indicates which math operation to perform. \n\n\n\nMade By ' + Fore.RED + 'TTheHolyOne#1642' + Fore.GREEN)
time.sleep(1)
input('Press enter key to proceed\n')
def calculator():
    opers = {
      '+': lambda a, b: a + b,
      '-': lambda a, b: a - b,
      '/': lambda a, b: a / b,
      '*': lambda a, b: a * b,
      '**': lambda a, b: a ** b
    }
    operspretty = {
    '+': 'Addition',
    '-': 'Subtraction',
    '*': 'Multiply',
    '/': 'Divide',
    '**': 'Pow'
    }
    def operschoice(operspretty):
        print("\n\nOperators to choose from:\n\n\n")
        for item, amount in operspretty.items():
            print("{} ({})".format(item, amount))
    clear_screen()
    while True:
            try:
                num1 = int(input('Please choose a number: \n'))
                num2 = int(input('\n\nPlease choose another number: \n'))
                break
            except:
                print('Please enter a valid number')
    operschoice(operspretty)
    choice = input('\n\n\nPlease choose from the choices above\n')
    clear_screen()
    if choice in opers:
        print('\n\nCalculating...')
        time.sleep(1)
        print(f"\n\nAnswer: \n{opers[choice](num1,num2)}")
        quitornot()
    else:
         print("Given operator not found") #checks if the read value is in the opers dictionairy
calculator()
time.sleep(1)
print('shutting down...')
