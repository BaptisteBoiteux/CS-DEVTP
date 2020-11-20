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



