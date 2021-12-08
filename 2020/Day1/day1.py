def day():
    liste = []
    f = open("input.txt","r")
    a = 0
    for ligne in f:
        liste.append(ligne)

    for j in liste:
        for h in liste:
            for k in liste : 
                if int(j) + int(h) + int(k) == 2020:
                    a = int(j) * int(h) * int(k)
    
    print(a)
    return a 


day()