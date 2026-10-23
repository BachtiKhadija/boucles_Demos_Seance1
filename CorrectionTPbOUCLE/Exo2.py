"""
var n , i,S:Entier
var rep :chaine
Debut 
tantQue True faire
  lire n 
  
  //calculer sigma(i) pour i allant de 1 jusqu'a n
  S=0
  pour i =1 : n faire 
      S=S+i
  FinPour
  ecrire " la somme est : ",S
  ecrire '*'*10
  ecrire "voulez vous calculer une autre somme?o/n"
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
    S=0
    for i in range(1,n+1): 
        S+=i
    print(f" la somme est : {S}")
    print('*'*60)
    rep=input("voulez vous calculer une autre somme?o/n : ") 
    if rep!="o":
        break
