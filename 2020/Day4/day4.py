def separe_text():
    f = open("input.txt","r")
    a = f.read().split('\n\n')
    f.close()
    return a

def un_passeport(p):
    dico = {}
    a = p.replace('\n',' ')
    a = a.split((' '))
    for i in a :
        dico[i.split(':')[0]] = str(i.split(':')[1])
    return dico


def valide(p):
    dico = un_passeport(p)
    return ("byr" in dico.keys()) and ("iyr" in dico.keys()) and ("eyr" in dico.keys()) and ("hgt" in dico.keys()) and ("hcl" in dico.keys()) and ("ecl" in dico.keys()) and ("pid" in dico.keys())


def main_v1():
    a = separe_text()
    cpt = 0
    for i in a :
        if valide(i):
            cpt += 1
    return cpt


print(main_v1())



def byr(p):
    d = un_passeport(p)
    return valide(p) and (len(d['byr']) == 4) and (int(d['byr']) >= 1920) and (int(d['byr']) <= 2002)

def iyr(p):
    d = un_passeport(p)
    return valide(p) and (len(d['iyr']) == 4) and (int(d['iyr']) >= 2010) and (int(d['byr']) <= 2020)

def eyr(p):
    d = un_passeport(p)
    return valide(p) and (len(d['eyr']) == 4) and (int(d['eyr']) >= 2020) and (int(d['eyr']) <= 2030)

def hgt(p):
    high = 0
    d = un_passeport(p)
    if 'cm' in d['hgt']:
        if len(d['hgt']) == 5 :
            high = d['hgt'][0:3]
            if (int(high) >= 150) and (int(high) <= 193):
                return True
    elif 'in' in d['hgt']:
        if len(d['hgt']) == 4 :
            high = d['hgt'][0:2]
            if (int(high) >= 59) and (int(high) <= 76):
                return True
    else :
        return False

def hcl(p):
    d = un_passeport(p)
    e = '0123456789abcdef'
    if d['hcl'][0] == '#' and len(d['hcl']) == 7:
        for i in d['hcl'][1:]:
            if i not in e :
                return False
        return True
    return False
                
def ecl(p):
    d = un_passeport(p)
    l = ['amb' , 'blu' , 'brn' , 'gry' , 'grn' , 'hzl' , 'oth']
    return d['ecl'] in l

def pid(p):
    d = un_passeport(p)
    n = '0123456789'
    if len(d['pid']) != 9:
        return False
    for i in d['pid']:
        if i not in n :
            return False
    return True


def main_v2():
    a = separe_text()
    cpt = 0
    for i in a :
        if byr(i) and iyr(i) and eyr(i) and hgt(i) and hcl(i) and ecl(i) and pid(i) :
            cpt += 1
    return cpt

print(main_v2())