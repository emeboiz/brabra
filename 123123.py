import colorama
from colorama import Fore
import time
import pyfiglet
import os
from pynput.mouse import Controller
from pynput import keyboard
#THIS IS OPEN SOURCE ITS NOT A RAT CMON GUYS
mouse = Controller()

colorama.init()
keyboard_controller = keyboard.Controller()
mouse = Controller()

title = Fore.RED + """
██╗░░██╗██╗░░░██╗██████╗░░█████╗░
██║░██╔╝██║░░░██║██╔══██╗██╔══██╗
█████═╝░██║░░░██║██████╔╝██║░░██║
██╔═██╗░██║░░░██║██╔══██╗██║░░██║
██║░╚██╗╚██████╔╝██║░░██║╚█████╔╝
╚═╝░░╚═╝░╚═════╝░╚═╝░░╚═╝░╚════╝░ 
 
                                                  """ + Fore.LIGHTMAGENTA_EX + " KURO? " + Fore.CYAN + " KURO? " + Fore.RED + " python rác " + Fore.RESET
os.system("cls")
print(Fore.GREEN+"EXE VERSION!!"+Fore.RESET)
kst = input(Fore.YELLOW+"Enter cái keybind của bạn: ").lower()

key_to_hold = kst

holding_key = False


def on_press(key):
    global holding_key
    try:
        if key.char == key_to_hold:
            holding_key = True
            print_status()
    except AttributeError:
        pass


def on_release(key):
    global holding_key
    try:
        if key.char == key_to_hold:
            holding_key = False
            print_status()
    except AttributeError:
        pass


def print_status():
    os.system("cls")
    print(f"Giữ {key_to_hold} để sài macro")
    print(title)
    print("------------------------------------------")
    if holding_key:
        print(Fore.GREEN + "KURCO STARTED" + Fore.RESET)
    else:
        print(Fore.RED + "KURCO STOPPED" + Fore.RESET)


def run_macro():
    mouse.scroll(0, 1)
    time.sleep(0.01)

    mouse.scroll(0, -1)
    time.sleep(0.01)


def main():
    print_status()

    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        while True:
            if holding_key:
                run_macro()
            time.sleep(0.01)


if __name__ == "__main__":
    main()

input()