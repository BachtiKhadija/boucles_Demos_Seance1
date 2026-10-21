#on utilise for si on veut répéter des lignes de code n fois
"""
syntaxe de for en algo  
for en algo Pour 

pour varIncr de bottom to top faire
    code source 
FinFpour


exemple en algo
*************
pour i de a to b faire    // de a à b tel que b-30+1= 10
   ecrire "Bonjour"         // i => variable compteur de la boucle 
Fin pour
#traduire en python 
****************

for i in range(a,b+1):    // de a à b tel que b-30+1= 10
   print("Bonjour")

Exemple2 : 
récupérer les multiples de 3 <=20 

algo
**** 
var i : entier
Debut 

    pour i de 1 to  20 faire
        si i%3==0 alors 
           ecrire i," est multiple de 3"
        finsi
    FinPour
Fin


for i in range(1,20):
    if i%3==0 : 
        print(i," est multiple de 3")
        

n=20
c1,c2,c3=0,0,0 
for i in range(4,10):
    x=int(input("saisir le nombre "))
    if x%2==0:
        c1+=1  #a=a+b  => a+=b
    
    if x%3==0:
        c2+=1 
    if x%2 and x%3 :
        c3+=1
print("le nombre de multiple de 2 est {}\nle nombre de multiple de 3 est {}\nle nombre de multiples de e et 3 est {}".format(c1,c2,c3))
""" 
#Boucle TantQue  => pilotée par une condition =>tourne tant que la condition est vraie et s'arrête une fois la condition est fausse    
#                => on l utilise s on connais pas d'avance d'itérations de la boucle
# Exemple : algo demande plusieurs valeur , la saisie s'arrête une fois on entre la valeur zero 

"""n=int(input("saisir la premiere valeur : "))
while(n>0):
    print(f"{n}",end=" ")
    n=int(input("\nsaisir la premiere valeur : "))
print("Fin Tant Que")"""
    
        