print("Merci de rentrer le nombre de photocopies voulus")
number = int(input())
if (number <= 50):
    price = (number * 50)
    print("Vous devez payez", price, "Francs")
if(number >= 50 ):
    reduc = number - 50
    total = (50 * 50)+(25*reduc)
    print("Vous devez payez", total, "Francs")
