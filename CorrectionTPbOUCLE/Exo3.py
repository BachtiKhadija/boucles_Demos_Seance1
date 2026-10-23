"""
var n , i,P:Entier
var rep :chaine
Debut 
tantQue True faire
  lire n 
  
  //calculer sigma(i) pour i allant de 1 jusqu'a n
  P)1
  pour i =1 : n faire 
      P=P*i
  FinPour
  ecrire " le fact est : ",P
  ecrire '*'*10
  ecrire "voulez vous calculer un autre produit ?o/n "
  lire rep
  si rep!="o" alors
      quitter //break en python
   FinSi
FinTantQue   
"""
while True:
    while True:
      n=input("saisir un entier : ") 
      if n.isdigit()==True:
          n=int(n)
          break
    #calculer sigma(i) pour i allant de 1 jusqu'a n
    P=1
    for i in range(1,n+1): 
        P*=i #P*P*i
    print(f" le factoriel  est : {P}")
    print('*'*60)
    rep=input("voulez vous calculer un autre produit?o/n : ") 
    if rep!="o":
        break
