from datetime import date
print("Quel est votre âge ?")
age = int(input())
b = int((date.today().year - age))
print("Vous êtes neé en : ")
print(b)

