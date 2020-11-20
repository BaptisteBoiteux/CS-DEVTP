import TP1f as f

'''

print("Bienvenue dans le Programme pour valider une date\n")
print("Veuillez rentrer le numero du jour :")
jour = int(input())
print("Veuillez rentrer le numero du mois :")
mois = int(input())
print("Veuillez rentrer l'année:")
annee = int(input())

rep = f.date_valide(jour,mois,annee)
if rep == True :
    print("date valide")
else:
    print("date non valide")

print("Bienvenue dans le Programme pour calculer vos impôts\n")
print("Veuillez rentrer votre salaire annuel:")
revenu = int(input())
rep = f.mesImpots(revenu)
print("Vous devez payer"+ str(rep) + "€ d'impôts cette année")

'''

B = [[1,2,3],[4,5,6],[0,0,0]]
C = [[5,6,7],[1,2,8],[4,5,6]]
matrice = f.multiplication(B,C)
print(matrice)


