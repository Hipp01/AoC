import string

def separe_text():
    f = open("input.txt","r")
    a = f.read().split('\n\n')
    f.close()
    return a


def reponse_groupe(g):
    liste = list(string.ascii_lowercase)
    dico = {}
    groupe = g.split('\n')
    total_groupe = 0
    for i in liste :
        dico[str(i)] = 0
    for j in groupe :
        for k in j:
            dico[k] += 1
    for h in dico.values():
        if h != 0:
            total_groupe += 1  
    return total_groupe


def main_v1():
    a = separe_text()
    cpt = 0
    for i in a :
        cpt += reponse_groupe(i)
    return cpt

# print(main_v1())


def reponse_groupe_entier(g):
    liste = list(string.ascii_lowercase)
    dico = {}
    groupe = g.split('\n')
    total_groupe_entier = 0
    for i in liste :
        dico[str(i)] = 0
    for j in groupe :
        for k in j:
            dico[k] += 1
    for h in dico.values():
        if h == len(groupe):
            total_groupe_entier += 1
    return total_groupe_entier

def main_v2():
    a = separe_text()
    cpt2 = 0
    for i in a :
        cpt2 += reponse_groupe_entier(i)
    return cpt2

print(main_v2())
