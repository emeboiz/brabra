import colorama
from colorama import Fore
import time
import pyfiglet
import os
from pynput.mouse import Controller
from pynput import keyboard

mouse = Controller()

colorama.init()
keyboard_controller = keyboard.Controller()
mouse = Controller()

# kbc=kb.c()
# call kb_c for in-game movements

title = Fore.RED + """ 
██╗░░██╗██╗░░░██╗██████╗░░█████╗░
██║░██╔╝██║░░░██║██╔══██╗██╔══██╗
█████═╝░██║░░░██║██████╔╝██║░░██║
██╔═██╗░██║░░░██║██╔══██╗██║░░██║
██║░╚██╗╚██████╔╝██║░░██║╚█████╔╝
╚═╝░░╚═╝░╚═════╝░╚═╝░░╚═╝░╚════╝░ 
                                                  
""" + Fore.LIGHTMAGENTA_EX + "KURO??" + Fore.CYAN + "KURO??" + Fore.RED + "PYTHON 12A13" + Fore.RESET
os.system("cls")
print(Fore.GREEN+"EXE VERSION!!"+Fore.RESET)
key_to_toggle = input(Fore.YELLOW+"nhập cái key của bạn để toggle: ").lower()

toggle_enabled = False


def on_press(key):
    global toggle_enabled
    try:
        if key.char == key_to_toggle:
            toggle_enabled = not toggle_enabled
            print_status()
    except AttributeError:
        pass


def print_status():
    os.system("cls")
    print("Press " + key_to_toggle + " to toggle the macro.")
    print(title)
    print("------------------------------------------")
    if toggle_enabled:
        print(Fore.GREEN + "KURCO STARTED" + Fore.RESET)
    else:
        print(Fore.RED + "KURCO STOPPED" + Fore.RESET)


def run_macro():
    mouse.scroll(0, 1)
    time.sleep(0.01)

    mouse.scroll(0, -1)
    time.sleep(0.01)


def main():
    print(f"Bấm {key_to_toggle} để dùng toggle.")
    print(title)

    with keyboard.Listener(on_press=on_press) as listener:
        while True:
            if toggle_enabled:
                run_macro()
            time.sleep(0.01)


if __name__ == "__main__":
    main()

input()
