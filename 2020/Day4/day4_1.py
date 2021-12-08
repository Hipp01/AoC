def reecriture():
    l = []
    a = ''
    f = open("input.txt","r")
    f2 = open("ecriture.txt","w")
    for i in f:
        l += i.replace('\n',' & ')
    for j in l:
        f2.write(j)

    f.close()
    f2.close()


def day4_2():
    f = open("ecriture.txt","r")
    l = []
    l2 = []
    invalide = 0
    valide = 0
    cpt = 0
    for i in f:
        l += i.split(' & & ')
    for j in l:
        l2.append(j.split(' '))
    for k in l2:
        cpt += 1
        if is_valide(k):
            valide += 1
    print(cpt)
    print(valide)
    return 0



def is_valide(k):
    a = []
    if len(k) == 8:
        return True
    elif len(k) == 7:
        for i in k:
            a += i.split(':')
        for j in a:
            if j == 'cid':
                return False
        return True
    else :
        return False




def invalidite(k):
    a = []
    if len(k) == 8 :
        return False
    if len(k) < 7 :
        return True
    else :
        for i in k:
            a += i.split(':')
        for j in a:
            if j == 'cid':
                return True
    return False

    



# ['ecl:gry', 'pid:860033327', 'eyr:2020', 'hcl:#fffffd', 'byr:1937', 'iyr:2017', 'cid:147', 'hgt:183cm']   bon

# ['hcl:#ae17e1', 'iyr:2013', 'eyr:2024', 'ecl:brn', 'pid:760753108', 'byr:1931', 'hgt:179cm']              bon a 7

reecriture()

day4_2()

