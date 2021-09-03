import time
import os
end = 0
while(end != 'n'):
    tentative = 0
    import random
    print("Choix du niveau [1-2-3]")
    level = int(input())
    if(level == 1):
        random = random.randint(1, 100)
        print(random)
        print("Entrer un nombre compris entre 1 et 100")
        max_tentative = 6
    if(level == 2):
        random = random.randint(1, 1000)
        print(random)
        print("Entrer un nombre compris entre 1 et 1000")
        max_tentative = 12
    if(level == 3):
        random = random.randint(1, 10000)
        print(random)
        print("Entrer un nombre compris entre 1 et 10000")
        max_tentative = 18
    number = 0
    while (number != random and  tentative != max_tentative):
        number = int(input())
        tentative = tentative + 1
        if (number < random):
            restant = max_tentative - tentative
            print("Plus Grand !")
            print("Tentative numero", tentative, "Il vous en reste ", restant)
        if (number > random):
            restant = max_tentative - tentative
            print("Plus Petit !")
            print("Tentative numero", tentative, "Il vous en reste ", restant)
    print("Partie Fini")
    time.sleep(1)
    print("Voulez-Vous re lancer une partie ? (Y/n)")
    end = str(input())
    os.system('cls')

