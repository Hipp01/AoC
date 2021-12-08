def day2():
    liste2liste = []
    cpt = 0
    f = open("input.txt","r")
    for i in f:
        liste2liste.append(i.split(" "))
    for j in liste2liste:
        nombres = j[0].split('-')
        lettre = j[1].replace(':','')
        mdp = j[2]
        if (mdp.count(lettre) >= int(nombres[0]) and mdp.count(lettre) <= int(nombres[1])):
            cpt += 1
    print(cpt)
    return cpt
        
    
day2()


def day2_2():
    liste2liste = []
    cpt = 0
    f = open("input.txt","r")
    for i in f:
        liste2liste.append(i.split(" "))
    for j in liste2liste:
        nombres = j[0].split('-')
        lettre = j[1].replace(':','')
        mdp = j[2]
        if((mdp[int(nombres[0])-1] == lettre) ^ (mdp[int(nombres[1])-1] == lettre)) :
            cpt += 1
    print(cpt)
    return cpt

day2_2()