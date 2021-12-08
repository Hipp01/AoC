def separer_texte():
    f = open("input5.txt","r")
    a = f.read().split('\n')
    f.close()
    return a


def rangee(l):
    nb_bin = ''
    for i in l:
        if i == 'F':
            nb_bin += '0'
        elif i == 'B':
            nb_bin += '1'
    nb_bin = int(nb_bin,2)
    return nb_bin


def colonne(l):
    nb = ''
    if l[7] == 'R':
        nb += '1'
    elif l[7] == 'L':
        nb += '0'

    if l[8] == 'R':
        nb += '1'
    elif l[8] == 'L':
        nb += '0'

    if l[9] == 'R':
        nb += '1'
    elif l[9] == 'L':
        nb += '0'
    nb = int(nb,2)
    return nb


def ID(l):
    id = 0
    col = colonne(l)
    ran = rangee(l)
    id = ran * 8 + col
    return id


def main_v1():
    sup = 0
    a = separer_texte()
    for i in a :
        if ID(i) > sup:
            sup = ID(i)
    print(sup)
    return sup

main_v1()


def main_v2():
    a = separer_texte()
    l = list(range(0,1024))
    cpt = 0
    l2 = []
    for i in a:
        if ID(i) in l:
            l.remove(ID(i))
    for j in l:
        if j != cpt + 1:
            l2.append(j)
        cpt = j
    l2.remove(min(l2))
    l2.remove(max(l2))
    print(l2[0])
    return(l2[0])

main_v2()