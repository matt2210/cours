import time
import os
end = 0
while(end != 'n'):
    print("Jouer 1 :")
    joueur_1 = input()
    resultat_joueur_1 = 0
    print("Jouer 2 :")
    joueur_2 = input()
    resultat_joueur_2 = 0
    print("Lancer ? (Y/N)")
    start = input()
    if (start == 'Y'):
        for i in range(3):
            import random
            random = random.randint(1, 6)
            if (random == 1):
                resultat_lancer = 100
            if (random == 2):
                resultat_lancer = 2
            if (random == 3):
                resultat_lancer = 3
            if (random == 4):
                resultat_lancer = 4
            if (random == 5):
                resultat_lancer = 5
            if (random == 6):
                resultat_lancer = 60
            resultat_joueur_1 = resultat_joueur_1 + resultat_lancer
        print("Résultat de", joueur_1, resultat_joueur_1, "Pts")
        for i in range(3):
            import random
            random = random.randint(1, 6)
            if (random == 1):
                resultat_lancer = 100
            if (random == 2):
                resultat_lancer = 2
            if (random == 3):
                resultat_lancer = 3
            if (random == 4):
                resultat_lancer = 4
            if (random == 5):
                resultat_lancer = 5
            if (random == 6):
                resultat_lancer = 60
            resultat_joueur_2 = resultat_joueur_2 + resultat_lancer
        print("Résultat de", joueur_2, resultat_joueur_2, "Pts")
        if (resultat_joueur_1 > resultat_joueur_2):
            print("Le gagnant est :", joueur_1)
        else:
            print("Le gagnant est :", joueur_2)
    print("Voulez-Vous re lancer une partie ? (Y/n)")
    end = str(input())
    os.system('cls')


