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


