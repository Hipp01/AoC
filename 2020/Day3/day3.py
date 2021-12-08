def day3_x_1(x):
    f = open("input.txt", "r")
    current = 0
    arbre = 0
    l=[]
    nombre = 0
    for i in f : 
        l.append(i)
    nombre = len(l[1]) - 2
    for j in l:
        if current > nombre : 
            current = current % 31
        if j[current] == "#":
            arbre += 1
        current += x
    
    print(arbre)
    return arbre


def day3_1_2():
    f = open("input.txt", "r")
    current = 0
    arbre = 0
    l=[]
    l2 = []
    nombre = 0
    for i in f : 
        l.append(i)
    for e in l:
        if l.index(e) % 2 == 0 :
            l2.append(e)
    nombre = len(l[1]) - 2
    for j in l2:
        if current > nombre : 
            current = current % 31
        if j[current] == "#":
            arbre += 1
        current += 1
    
    print(arbre)
    return arbre



def final():
    a = day3_x_1(1) * day3_x_1(3) * day3_x_1(5) * day3_x_1(7) * day3_1_2()
    print(a)
    return a


# 2138320800

final()
