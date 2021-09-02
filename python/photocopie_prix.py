print("Merci d'entrer le nombre de photocopies que vous souhaiter effectuer")
number = int(input())
if(number >= 1 and number <= 30):
    tarif = (number * 50)
    print("Vous devez payez", tarif, "Francs")
if(number >= 31 and number <= 60):
    tarif = (number * 30)
    print("Vous devez payez", tarif, "Francs")
if(number >= 61 and number <= 100):
    tarif = (number * 20)
    print("Vous devez payez", tarif, "Francs")
if(number > 100):
    tarif = (number * 15)
    print("Vous devez payez", tarif, "Francs")