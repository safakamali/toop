from Resources import *
from termcolor import colored
from colorama import init as color_init, Fore
from os import system
from pyfiglet import figlet_format
import configure

color_init()


system(configure.ScreenClear_command)

def Header():
    print(Fore.GREEN+figlet_format("Toop", "speed"))


Header()

while True:
    prefix_text = f"{Fore.LIGHTBLUE_EX + 'Toop'}: {Fore.LIGHTYELLOW_EX + 'CMD' + Fore.LIGHTWHITE_EX} ~$ "
    input_command = input_C(prefix_text)
    command_args = input_command.split(" ")
    command =  command_args.pop(0).lower()

    if not input_command == "":
        if IsPythonFilename(input_command):
            system(f'python {input_command}')
        else:
            try:
                CommandsConfig[command]['func'](command_args)
            except KeyError:
                print(Fore.RED + "Unknown command!")
            except Exit:
                break
            except:
                print(Fore.RED + f"Error in this command ({command})")