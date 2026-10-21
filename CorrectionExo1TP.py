# table de multiplication 
while True: 
    while True:
        n=input("saisir un entier ")
        if n.isdigit()==True:
            n=int(n)
            break #quitter la boucle
    #afficher la table de multiplication n 
    for i in range(1,11):
        print(f"{n} * {i} = {n*i}")
    rep=input("voulez vous afficher une autre table de mulyiplication ? o/n")
    if rep!='o':
        print("Fin programme !!!")
        break
        
"""
var n : entier
var rep : chaine
Debut 
tantQue True:
    Ecrire("saisir un entier ")
    lire n       
    //afficher la table de multiplication n 
    pour i de 1 : 10 faire
        ecrire(n,"*",i," = ",n*i)
    FinPour    
    ecrire("voulez vous afficher une autre table de mulyiplication ? o/n")
    lire rep
    si rep!='o' alors
        Ecrire("Fin programme !!!")
        Quitter
FinTantQue



"""













"""   



