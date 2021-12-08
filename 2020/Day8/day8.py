def separe_text():
    f = open("test.txt","r")
    a = f.read().split('\n')
    f.close()
    return a

def instruction(l,i,cpt):
    l = l.split(' ')
    if l[0] == 'acc' :
        cpt += int(l[1])
        i += 1
    elif l[0] == 'jmp' :
        i += int(l[1])
    else :
        i += 1
    return i,cpt

def main_v1():
    a = separe_text()
    cpt = 0
    deja_vu = []
    i = 0
    while i not in deja_vu :
        deja_vu.append(i)
        i,cpt = instruction(a[i],i,cpt)
    return cpt

print(main_v1())


def main_v2():
    i = 0
    while i != len(separe_text())-1:
        a = separe_text()
        cpt = 0
        deja_vu = []
        i = 0
        while i not in deja_vu :
            deja_vu.append(i)
            i,cpt = instruction(a[i],i,cpt)
            if i in deja_vu :
                j = 0 
                cpt2 = 0
                deja_vu2 = []
                a[i-1] = a[i-1].replace('jmp','nop')
                while j not in deja_vu2 :                    
                    deja_vu2.append(j)
                    j,cpt2 = instruction(a[j],j,cpt2)
                    print('ferbvi')
                i = j

    return cpt

#print(main_v2())