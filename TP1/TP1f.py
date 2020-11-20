#Première partie : Calendrier

def pri():
    print("Bonjour")

def bissextile (annee):
    rep = False
    test400 = annee%400
    test4 = annee%4
    test100 = annee%100
    if test400 == 0 :
        rep = True
    elif test4 == 0 and test100 != 0 :
        rep = True
    return rep

def nb_jour_mois(mois,annee) :
    Nb = 0
    mois30 = [4,6,9,11]
    mois31 = [1,3,5,7,8,10,12]
    if mois < 1 or mois > 12 :
        print("le mois n'est pas pris en compte")
        return False
    else :
        if (mois in mois30) == True :
            Nb = 30
        if (mois in mois31) == True :
            Nb = 31
        if mois == 2 :
            if bissextile(annee) == True :
                Nb = 29
            else :
                Nb = 28
    return Nb

def date_valide(jour,mois,annee) :
    if jour <= nb_jour_mois(mois,annee) :
        return True
    else :
        return False

#Deuxième partie : Impôts

def mesImpots(revenu) :
    rep = 0
    Tranche = [9964,27519,73779,156244]
    if revenu > Tranche[0] and revenu < Tranche[1] :
        rep += (revenu - Tranche[0])*0.14
    if revenu > Tranche[1] and revenu < Tranche[2] :
        rep += (revenu - Tranche[1])*0.30
        rep += (Tranche [1] - Tranche[0])*0.14
    if revenu > Tranche[2] and revenu < Tranche[3] :
        rep += (revenu - Tranche[2])*0.41
        rep += (Tranche [2] - Tranche[1])*0.30
        rep += (Tranche [1] - Tranche[0])*0.14
    if revenu > Tranche[3] :
        rep += (revenu - Tranche[3])*0.45
        rep += (Tranche [3] - Tranche[2])*0.41
        rep += (Tranche [2] - Tranche[1])*0.30
        rep += (Tranche [1] - Tranche[0])*0.14
    return rep  

#Troisième partie : Matrice


    


