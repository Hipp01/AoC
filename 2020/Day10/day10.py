def separe_text():
    f = open("test.txt","r")
    a = f.read().split('\n')
    f.close()
    return a


def main_v1():
    a = separe_text()
    cpt1 = 1
    cpt3 = 1
    for i in range(len(a)) :
        a[i] = int(a[i])
    a = sorted(a)
    for j in range(len(a)) :
        if a[j-1] == a[j] - 1 :
            cpt1 += 1
        elif a[j-1] == a[j] - 3 :
            cpt3 += 1


    cpt = cpt1 * cpt3
    return cpt1, cpt3 , cpt


print(main_v1())