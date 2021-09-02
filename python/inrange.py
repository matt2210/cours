print("Combien de fois voulez vous repeter le mot ? : ")
n = int(input())
for i in range (n):
    n = n+(1+n)
print(n)