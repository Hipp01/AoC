def cadeau():
    with open("input.txt") as f:
        lines = f.readlines()
    total = 0
    for i in lines :
        dimensions = i.split('x')
        l = int(dimensions[0])
        w = int(dimensions[1])
        h = int(dimensions[2])
        papier_cadeau = 2*l*w + 2*w*h + 2*h*l + min(l*w,w*h,h*l)
        total += papier_cadeau
    return total

def ruban():
    with open("input.txt") as f:
        lines = f.readlines()
    total = 0
    for i in lines :
        dimensions = i.split('x')
        l = int(dimensions[0])
        w = int(dimensions[1])
        h = int(dimensions[2])
        liste_dimensions = [l,w,h]
        min_1 = min(liste_dimensions)
        liste_dimensions.remove(min_1)
        min_2 = min(liste_dimensions)
        ruban = 2*min_1 + 2*min_2 + l*w*h
        total += ruban

    return total


if __name__ == "__main__":
    print(cadeau())
    print(ruban())
