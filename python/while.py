import random

random = random.randint(1,100)

print(random)
print("Entrer un nombre compris entre 10 et 20")
number = int(input())
while (number != random):
    if(number < random):
        print("Plus Grand !")
    if(number > random):
        print("Plus Petit !")
    number = int(input())
print("Nombre correct")