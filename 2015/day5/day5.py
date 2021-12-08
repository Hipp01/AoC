def valid():
    with open("input.txt") as f:
            lines = f.readlines()
    
    nombre_valides = 0
    for ligne in lines:
        valid_voyelles = False
        valid_double = False
        valid_chaine = True

        if ('ab' in ligne) or ('cd' in ligne) or ('pq'in ligne) or ('xy' in ligne) :
            valid_chaine = False

        voyelles = {'a', 'e', 'i', 'o', 'u'}
        nombre_voyelles = 0

        for i in range(len(ligne)) :
            if ligne[i] in voyelles :
                nombre_voyelles += 1
            if nombre_voyelles >= 3:
                valid_voyelles = True

            if (ligne[i-1] == ligne[i]) and (i != 0):
                valid_double = True
        
        if valid_voyelles and valid_double and valid_chaine :
            nombre_valides += 1
    
    return nombre_valides

                    

            

def valid2():
    with open("input.txt") as f:
            lines = f.readlines()
    nombre_valide = 0
    for ligne in lines:
        deux_fois = False
        split_by_letter = False
        for i in range(len(ligne)) :
            if ligne[i-1]+ligne[i] in ligne[i+1:]:
                deux_fois = True

            if ligne[i-2] == ligne[i] and (i != 0) and (i != 1) :
                split_by_letter = True


        if deux_fois and split_by_letter:
            nombre_valide += 1
    return nombre_valide









if __name__ == "__main__":
    print(valid())
    print(valid2())