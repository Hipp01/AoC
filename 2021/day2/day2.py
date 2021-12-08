def position():
    with open("input.txt") as f:
        lines = f.readlines()
    horizontal = 0
    profondeur = 0
    for i in lines :
        commande = i.split(' ')
        direction = commande[0]
        nombre = int(commande[1])

        if direction == 'forward' :
            horizontal += nombre

        elif direction == 'down' :
            profondeur += nombre
        
        elif direction == 'up' :
            profondeur -= nombre
    
    return horizontal*profondeur


def position2():
    with open("input.txt") as f:
        lines = f.readlines()
    horizontal = 0
    profondeur = 0
    objectif = 0
    for i in lines :
        commande = i.split(' ')
        direction = commande[0]
        nombre = int(commande[1])

        if direction == 'forward' :
            horizontal += nombre
            profondeur += objectif*nombre

        elif direction == 'down' :
            objectif += nombre
        
        elif direction == 'up' :
            objectif -= nombre

    return horizontal*profondeur



if __name__ == "__main__":
    print(position())
    print(position2())