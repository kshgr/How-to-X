import colorama
from colorama import Fore, Back, Style

#Initialize colorama
colorama.init(autoreset=True)

#Print text using background and font colors
print(Back.GREEN + Fore.BLUE + " Welcome to KSHGR Tech ")
#Add newline
print()
#Print text using background color
print(Back.YELLOW + " Programming made easy ")