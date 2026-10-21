pt=input("saisir le prix ToTAL : ")  

while pt.isdigit()==False:
    pt=input("saisir le prix ToTAL : ")  
tauxR=input("saisir le taux de remise : ")
while tauxR.isdigit()==False:
    tauxR=input("saisir une valeur numérique : ")  
remise=int(pt)*int(tauxR)
print("remise = ",remise)