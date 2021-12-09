import numpy as np

def input():
    with open("input.txt") as f:
        lines = f.readlines()
    return lines

def bingo():
    lines = input()
    numeros = lines[0].split(',')
    liste_grilles = []
    cpt = 0
    for i in range(6,len(lines),6):
        l1,l2,l3,l4,l5 = [],[],[],[],[]
        for j in lines[i-4].split(' '):
            if j != '':
                l1.append(int(j))
        for k in lines[i-3].split(' '):
            if k != '':
                l2.append(int(k))
        for l in lines[i-2].split(' '):
            if l != '':
                l3.append(int(l))
        for m in lines[i-1].split(' '):
            if m != '':
                l4.append(int(m))
        for n in lines[i].split(' '):
            if n != '':
                l5.append(int(n))
        liste_grilles.append([l1,l2,l3,l4,l5])
    
    for a in numeros:
        for i in range(len(liste_grilles)):
            for j in range(len(liste_grilles[i])):
                for k in range(len(liste_grilles[i][j])):
                    if liste_grilles[i][j][k] == int(a):
                        liste_grilles[i][j][k] = 0
        
        for g in liste_grilles:
            if column(g) or line(g) :
                for i in g:
                    for j in i:
                       cpt += j
                
                return cpt*int(a)
    return False        
    
        
        
def column(grille):
    a,b,c,d,e = 0,0,0,0,0
    for i in grille:
        a += i[0]
        b += i[1]
        c += i[2]
        d += i[3]
        e += i[4]
    if (a == 0) or (b == 0) or (c == 0) or (d == 0) or (e == 0):
        return True
    return False

def line(grille):
    for i in grille:
        if i == [0,0,0,0,0]:
            return True
    return False

def bingo2():
    lines = input()
    numeros = lines[0].split(',')
    liste_grilles = []
    cpt = 0
    for i in range(6,len(lines),6):
        l1,l2,l3,l4,l5 = [],[],[],[],[]
        for j in lines[i-4].split(' '):
            if j != '':
                l1.append(int(j))
        for k in lines[i-3].split(' '):
            if k != '':
                l2.append(int(k))
        for l in lines[i-2].split(' '):
            if l != '':
                l3.append(int(l))
        for m in lines[i-1].split(' '):
            if m != '':
                l4.append(int(m))
        for n in lines[i].split(' '):
            if n != '':
                l5.append(int(n))
        liste_grilles.append([l1,l2,l3,l4,l5])
    
    for a in numeros:
        for i in range(len(liste_grilles)):
            for j in range(len(liste_grilles[i])):
                for k in range(len(liste_grilles[i][j])):
                    if liste_grilles[i][j][k] == int(a):
                        liste_grilles[i][j][k] = 0
        
        for g in liste_grilles:
            if (column(g) or line(g)) and len(liste_grilles) == 1:
                for i in g:
                    for j in i:
                       cpt += j
                return cpt*int(a)
            elif column(g) or line(g):
                liste_grilles.remove(g)


if __name__=="__main__":
    print(bingo())
    print(bingo2())
