def immeuble():
    etage = 0
    with open("input.txt") as f:
        lines = f.read()
    for i in lines :
        if i == '(':
            etage += 1
        elif i == ')':
            etage -= 1
    return etage



def sous_sol():
    etage = 0
    with open("input.txt") as f:
        lines = f.read()
    for i in range(len(lines)) :
        if lines[i] == '(':
            etage += 1
        elif lines[i] == ')':
            etage -= 1
        if etage == -1:
            return i+1

if __name__ == "__main__":
    print(immeuble())
    print(sous_sol())