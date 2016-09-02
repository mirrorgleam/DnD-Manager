import random

victims = []

def rollDice(n,s):
    if s == 100:
        for i in range(n):
            pres = random.randrange(10,100,10)
            print(pres)
        selectDice()

    else:    
        for i in range(n):
            res = random.randint(1,s)
            print(res)
        selectDice()

def selectDice():
    s = input("\nPlease select the die you will be throwing:\nD4=\t4\nD6=\t6\nD8=\t8\nD10=\t10\nD12=\t12\nD20=\t20\nD10%=\t100\nExit\tExit\nDM Main=\tDM\nSelection: ")
    if s.lower() == "dm":
        DmMain()
    elif s.lower() == "exit":
        exit()
    elif s != "4" and s != "6" and s != "8" and s != "10" and s != "12" and s != "20" and s != "100":
        print("\nyour dice are broken... \nCheck the number of sides and try again")
        selectDice()
    n = int(input("\nAnd how many die will be thrown: "))
    if int(n) > 10:
        print("\nRed flag!\nToo many dice on the table")
        selectDice()
    elif int(n) < 1:
        print("\nWhat happened!?\nWhere did your dice go?")
        selectDice()
    
    rollDice(int(n),int(s))

def getWho():
    who = input("\nWelcome Traveler\nAre you the DM or Player?\n(DM or P)")
    if who.lower() == "dm":
        DmMain()
    elif who.lower() == "p":
        selectDice()
    else:
        print("\nNope... Try again")
        getWho()

def DmMain():
    global victims
    
    try:
        with open('victims.txt','r') as v:
            victims = v.read().splitlines()
        if victims == []:
            getVics()

    except FileNotFoundError:
        if victims == []:
            getVics()
        else:
            chekVics()

    print("\nWelcome DM")

    print("\nVictims List:\n{}".format(victims[:]))

    print("\nMake your move")
    
    dmSel = input("\nMonster Select\t1\nVictim Select\t2\nRoll Dice\t3\nNew Victims\t8\nExit\t\tExit\nSelection: ")

    if dmSel.lower() == "exit":
        exit()

    elif dmSel == "1":

        while True:

            try:
                mon = input("\nHow many monsters are there? ")
                mon = int(mon)
                print("\nMonster :: {} :: was selected".format(random.randint(1,mon)))
                DmMain()

            except ValueError:
                print("\n{} is not a valid option".format(mon))
                continue

    elif dmSel == "2":
            print("\nYour victim this time is {}".format(random.choice(victims).upper()))
            DmMain()
    
    elif dmSel == "3":
        selectDice()
    
    elif dmSel == "8":
        getVics()

    else:
        print("\n{} is not a valid option\nAre you trying to break me?".format(dmSel))
        DmMain()

def getVics():
    open("victims.txt","w").close()
    global victims
    victims = []
    vic = input("\nGimme a player's name: ")
    while vic.lower() != 'done':
        print("\nType 'done' to finish")
        victims.append(vic)
        vic = input("\nAnother name? ")
    chekVics()

def chekVics():
    open("victims.txt","w").close()
    global victims
    with open('victims.txt','r+') as v:
        v.write("\n".join(victims))
    print("\nYour victims are:\n{}\nCorrect?".format(victims[:]))
    sel = input("\nY or N: ")
    if sel.lower() == "y":
        DmMain()
    elif sel.lower() == "n":
        getVics()
    else:
        print("\nI didn't understand your response")
        chekVics()


getWho()
