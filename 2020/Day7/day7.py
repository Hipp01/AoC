import networkx as nx
import matplotlib.pyplot as plt


def separe_text():
    f = open("input.txt","r")
    a = f.read().split('\n')
    f.close()
    return a


def separe_bagage(ligne):
    l = []
    ligne = ligne.replace(' bags','')
    ligne = ligne.replace(' bag','')
    ligne = ligne.replace('.','')
    l += ligne.split(' contain ')
    l[1] = l[1].split(', ')
    for i in range(len(l[1])) :
        l[1][i] = l[1][i][2:]

    return l

def dictionnaire_couleur():
    liste = []
    a = separe_text()
    dico = {}
    for i in a :
        liste.append(separe_bagage(i))
    for j in liste :
        dico[j[0]] = set()
        for h in j[1] :
            dico[j[0]].add(h)
    return dico



def main_v1():
    d = dictionnaire_couleur()
    cles = d.keys()
    g = nx.Graph()
    g.add_nodes_from(cles)
    cpt = 0
    for i in list(g.nodes) :
        for j in d[i] :
                g.add_edge(i,j) 
    print(g.degree['shiny gold'])
    nx.draw_networkx(g, with_labels=True)
    plt.show()


main_v1() 



# shiny gold

    
    

# main_v1()




# print(separe_bagage('bright gray bags contain 2 bright gold bags, 5 dull lavender bags.'))
# print(separe_bagage('plaid blue bags contain 1 dull indigo bag, 4 wavy black bags, 4 clear red bags.'))




# 'bright gray bags contain 2 bright gold bags, 5 dull lavender bags.'