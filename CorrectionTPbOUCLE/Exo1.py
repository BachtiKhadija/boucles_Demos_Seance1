"""
pour i in [1,10] repeter n*i = {n*i}
Remarque 
var n,i
Debut
  lire n
  pour  i=1 : 10  faire
     ecrire "n*",i,"=",(n*i)
  Fin Pour
"""
#**********************Contrôle de saisie*********************
while True:
    while True:
        n=input("saisir une valeur : ")
        if n.isdigit()==True:
            n=int(n)
            break

    #**********************Contrôle de saisie*********************
    for  i in range(1,11):
        print(n,"*",i,"=",(n*i))
    print("*"*50)
    rep=input("voulez afficher la TM d'un autre entier ? o/n")
    if rep!="o":
        break
print("*************************************Fin Programme***************************************************")
    

















