print("Merci d'indiquer l'année que vous souhaiter verifier :")
anne = int(input())
if((anne % 4) == 0 and (anne % 100) != 0):
	print("L'an" ,anne, "est une année bisextile")
else:
	print("L'an" ,anne, "n'est pas une année bisextile")
