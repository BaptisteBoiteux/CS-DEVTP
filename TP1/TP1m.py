import TP1f as f

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
