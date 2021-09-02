print("Merci d'entrer votre note")
note = float(input())
if(note < 8):
    print("Votre note est insuffisante vous êtes donc ajourné")
if(note > 8 and note < 10):
    print("Votre note est accepter pour le rattrapage ")
if(note >= 10):
    print("Bravo vous êtes reçus")
