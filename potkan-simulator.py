import random
import time
import os

# JAZYKY + MAIN LOBBY

def svk():
    print("####################################################")
    print("#          🐀 SIMULÁCIA ŽIVOTA POTKANA 🐀         #")
    print("#                                                  #")
    print("#                                                  #")
    print("#        🐀 STLAČ [A] PRE SPUSTENIE HRY 🐀        #")
    print("#        🐀 STLAČ [X] PRE SKONČENIE HRY 🐀        #")
    print("#        🐀 STLAČ [L] PRE ZMENU JAZYKA  🐀        #")
    print("#                                                  #")
    print("#                                                  #")
    print("####################################################")
    choose_svk = input("              Vyber si odpoveď:        ")
    if choose_svk == "A":
        os.system("clear")
        #hra_svk()
    if choose_svk == "X":
        os.system("exit")
    if choose_svk == "L":
        os.system("clear")
        LANG()



def eng():
    print("####################################################")
    print("#            🐀 POTKAN LIFE SIMULATOR 🐀          #")
    print("#                                                  #")
    print("#                                                  #")
    print("#              🐀 PRESS [A] TO PLAY 🐀            #")
    print("#              🐀 PRESS [X] TO EXIT 🐀            #")
    print("#        🐀 PRESS [L] TO CHANGE LANGUAGE🐀        #")
    print("#                                                  #")
    print("#                                                  #")
    print("####################################################")
    choose_eng = input("              Choose your answer:        ")
    if choose_eng == "A":
        os.system("clear")
        # hra_eng()
    if choose_eng == "X":
        os.system("exit")
    if choose_eng == "L":
        os.system("clear")
        LANG()

def rus():
    print("####################################################")
    print("#          🐀 СИМУЛЯТОР КРЫСИНОЙ ЖИЗНИ 🐀         #")
    print("#                                                  #")
    print("#                                                  #")
    print("#       🐀 НАЖМИ [A], ЧТОБЫ НАЧАТЬ ИГРУ 🐀        #")
    print("#          🐀 НАЖМИ [X], ЧТОБЫ ВЫЙТИ 🐀           #")
    print("#       🐀 НАЖМИ [L], ЧТОБЫ ИЗМЕНИТЬ ЯЗЫК 🐀      #")
    print("#                                                  #")
    print("#                                                  #")
    print("####################################################")
    choose_rus = input("                   Oтвечaй:        ")
    if choose_rus == "A":
        os.system("clear")
        # hra_rus()
    if choose_rus == "X":
        os.system("exit")
    if choose_rus == "L":
        os.system("clear")
        LANG()


def hun():
    print("####################################################")
    print("#          🐀 PÁTKÁNY ÉLET SZIMULÁTOR  🐀         #")
    print("#                                                  #")
    print("#                                                  #")
    print("# 🐀 NYOMJA MEG AZ [A], A JÁTÉK ELINDíTÁSÁHOZ 🐀  #")
    print("#   🐀 NYOMJA MEG AZ [X] GOMBOT A KILÉPÉSHEZ 🐀   #")
    print("#         🐀 NYOMJA MEG AZ [L] GOMBOT 🐀          #")
    print("#        🐀 A NYELV MEGVÁLTOZTATÁSÁHOZ 🐀         #")
    print("#                                                  #")
    print("####################################################")
    choose_hun = input("                     Válsz:        ")
    if choose_hun == "A":
        os.system("clear")
        # hra_hun
    if choose_hun == "X":
        os.system("exit")
    if choose_hun == "L":
        os.system("clear")
        LANG()

def ar():
    print("####################################################")
    print("#           🐀 محاكاة حياة الفئران  🐀          #")
    print("#                                                  #")
    print("#                                                  #")
    print("#            🐀 اضغط [A] لبدء اللعبة🐀           #")
    print("#               🐀 اضغط [X] للخروج 🐀            #")
    print("#           🐀 Nاضغط [L] لتغيير اللغة 🐀         #")
    print("#                                                  #")
    print("####################################################")
    choose_ar = input("                      أَجِبْ:        ")

    if choose_ar == "A":
        os.system("clear")
        # hra_ar
    if choose_ar == "X":
        os.system("exit")
    if choose_ar == "L":
        os.system("clear")
        LANG()


# INITIAL LANG SETUP
def LANG():
    os.system("clear")
    print("####################################################")
    print("#            🐀 POTKAN LIFE SIMULATOR 🐀          #")
    print("#                                                  #")
    print("#                                                  #")
    print("#              🐀  [1] SLOVAK    🐀               #")
    print("#              🐀  [2] ENGLISH   🐀               #")
    print("#              🐀  [3] RUSSIAN   🐀               #")
    print("#              🐀  [4] HUNGARIAN 🐀               #")
    print("#              🐀  [5] ARABIC    🐀               #")
    print("#                                                  #")
    print("#                                                  #")
    print("####################################################")

    choose = int(input("              Choose your language:        "))
    if choose == 1:
        os.system("clear")
        svk()
    elif choose == 2:
        os.system("clear")
        eng()
    elif choose == 3:
        os.system("clear")
        rus()
    elif choose == 4:
        os.system("clear")
        hun()
    elif choose == 5:
        os.system("clear")
        ar()

