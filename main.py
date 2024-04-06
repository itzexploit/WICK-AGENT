from fake_useragent import UserAgent
from time import sleep
from pystyle import Colors , Colorate
from threading import Thread as thr
from colorama import init , Fore
from os import system , name

red = Fore.LIGHTRED_EX; green = Fore.LIGHTGREEN_EX; blue = Fore.LIGHTBLUE_EX; yellow = Fore.LIGHTYELLOW_EX; cyan = Fore.LIGHTCYAN_EX; white = Fore.LIGHTWHITE_EX; magenta = Fore.LIGHTMAGENTA_EX;
init()
ua = UserAgent()

system('cls' if name == 'nt' else 'clear')

banner = '''
            _     _  ___   _______  ___   _         _______  _______  _______  __    _  _______ 
            | | _ | ||   | |       ||   | | |       |   _   ||       ||       ||  |  | ||       |
            | || || ||   | |       ||   |_| | ____  |  |_|  ||    ___||    ___||   |_| ||_     _|
            |       ||   | |       ||      _||____| |       ||   | __ |   |___ |       |  |   |  
            |       ||   | |      _||     |_        |       ||   ||  ||    ___||  _    |  |   |  
            |   _   ||   | |     |_ |    _  |       |   _   ||   |_| ||   |___ | | |   |  |   |  
            |__| |__||___| |_______||___| |_|       |__| |__||_______||_______||_|  |__|  |___|  
'''

print(Colorate.Horizontal(Colors.red_to_blue,banner,2))
print(Colorate.Horizontal(Colors.red_to_yellow,'\n                          Welcome To WICK AGENT, Created By John Wick',2))
print(Colorate.Horizontal(Colors.red_to_white,'                                     Team Pytho Learn',2))

num = int(input(f'\n  {red}[{yellow}+{red}]{green} Number Of User-Agents {red}:{white} '))

def main():
    file =  open('user-agent-wick.txt', 'w')
    for _ in range(num):
        ua2 = ua.random
        print(Colorate.Horizontal(Colors.green_to_cyan,ua2,2))
        file.write(ua2 + '\n')
    print(Colorate.Horizontal(Colors.purple_to_blue,'\n   OPEN [ user-agent-wick.txt ] FILE xD',2))

thr(target=main).start()
