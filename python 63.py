from colorama import Fore
import pyfiglet
font=pyfiglet.figlet_format('Eid Mubarak')
print(Fore.RED+font)


print('------')
a=dir(Fore)
for i in a:
    print(i)
print('------')
b=dir(pyfiglet)
for i in b:
    print(i)

