import os
import time

#\033[1;30m Branco
#\033[1;31m Vermelho
#\033[1;32m Verde
#\033[1;33m Amarelo
#\033[1;34m Azul
#\033[1;35m Roxo
#\033[1;36m Ciano
#\033[1;37m Cinza Claro

os.system("clear")
os.system("pkg install figlet")
os.system("clear")
print("\033[1;36m")
os.system("figlet Cyber-Punk")
print("""\033[1;34m
卐=======================卐
\033[1;35m
l    [1] install pip      l
l    [2] install perl     l
l    [3] install curl     l
l    [4] install gh       l
l    [5] install git      l
l    [6] install python   l
l    [7] install python2  l
l    [8] install python3  l
l    [9] 4devs            l
l    [10] install php     l
l    [11] Exit            l
\033[1;34m
卐=======================卐
""")
op = input("/Digite a opção:/ ")

if op == "1":
    os.system("clear")
    os.system("pip install requests")
    os.system("python3 Cyber.py")
elif op == "2":
    os.system("clear")
    os.system("pkg install perl")
    os.system("python3 Cyber.py")
elif op == "3":
    os.system("clear")
    os.system("pkg install curl")
    os.system("python3 Cyber.py")
elif op == "4":
    os.system("clear")
    os.system("pkg install gh")
    os.system("python3 Cyber.py")
elif op == "5":
    os.system("clear")
    os.system("pkg install git")
    os.system("python3 Cyber.py")
elif op == "6":
    os.system("clear")
    os.system("pkg install python")
    os.system("python3 Cyber.py")
elif op == "7":
    os.system("clear")
    os.system("pkg install python2")
    os.system("python3 Cyber.py")
elif op == "8":
    os.system("clear")
    os.system("pkg install python3")
    os.system("python3 Cyber.py")
elif op == "9":
    os.system("clear")
    os.system("xdg-open www.4devs.com.br")
    os.system("python3 Cyber.py")
elif op == "10":
    os.system("clear")
    os.system("pkg install php")
    os.system("python3 Cyber.py")
elif op == "11":
    os.system("clear")
    print("Finalizando....")
    time.sleep(4)
    exit()
else:
    os.system("python3 Cyber.py")
    