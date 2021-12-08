def separe_text():
    f = open("input.txt","r")
    a = f.read().split('\n')
    f.close()
    return a

def main_v1():
    addition = []
    a = separe_text()
    for j in range(len(a)) :
        a[j] = int(a[j])
    for i in range(25,len(a)+1) :
        preambule = a[(i-25):(i)]
        for b in preambule :
            for c in preambule :
                if b != c :
                    addition.append(b+c)
        if a[i] not in addition :
            return a[i]

print(main_v1())

def main_v2():
    a = separe_text()
    b = main_v1()
    final = 0
    cpt = 0
    for j in range(len(a)) :
        a[j] = int(a[j])

    while cpt != len(a) :
        l = []
        i = cpt
        while sum(l) <= b :
            if sum(l) == b:
                final = min(l) + max(l)
                return final
            l.append(a[i])
            i += 1 
        cpt += 1  
    return 0

print(main_v2())