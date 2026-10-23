"""
var max,n ,k,pos: entier
Debut
  lire n
  max=n
  pos=1
  pour k =2 : 10 faire
        lire n
        si max<n alors 
            max=n
            pos=k
        finsi
  Fin Pour 
  Ecrire "Le maximum est : ",max,", sa position est : ",pos
Fin  
"""
while True:
    n=input("saisir un entier")
    if n.isdigit():
        n=int(n)
        break
max=n
pos=1
for k in range(2,11):
    while True:
        n=input("saisir un entier")
        if n.isdigit()==True:
            n=int(n)
            break
    if max<n: 
        max=n
        pos=k
    
print( "Le maximum est : ",max,", sa position est : ",pos)
