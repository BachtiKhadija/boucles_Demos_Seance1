while True: 
    note=input("saisir la note : ")
    while note.isidigit()==False:
        note=input("saisir une noe valide : ")
    note=int(note)
    """if note>=10:
        print("admis !!!")
    else:
        print("non admis")"""
    print("admis") if note>=10 else print("non admis")
    
    rep=input("voulez vous tester une autre note ? o/n")
    if rep!='o':
        break # quitter la boucle 
print("Fin Programme!!!")
    