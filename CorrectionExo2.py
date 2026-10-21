"""
 var n,s,i:entier
 var rep : chaine
 
 Debut 
 
   tant Que 1==1 : 
        lire n 
        S=0
        pour i de 1:n faire 
                S+=i
        FinPour
        
        ecrire "la somme est : ",S
        ecrire "voulez vous calculer une autre somme ?"
        lire rep
        si rep!='o' alors 
           quitter
        FinSi
    FinTantQue
    """
while 1==1 : 
    while True:
        n=input("saisir un entier ")
        if n.isdigit()==True:
            n=int(n);break
    S=0
    for i in range(1,n+1):
        S+=i
    print("la somme est : ",S)
    rep=input( "voulez vous calculer une autre somme ?")
    if rep!='o': 
        break


   