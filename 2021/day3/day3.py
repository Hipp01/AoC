def input():
    with open("input.txt") as f:
        lines = f.readlines()
    return lines


def electrique():
    lines = input()
    gamma = ''
    epsilon = ''
    liste_e = (len(lines[0])-1)*[0]
    for ligne in lines:
        for i in range(len(ligne)) :
            if ligne[i] == '0':
                liste_e[i] -= 1
            elif ligne[i] == '1':
                liste_e[i] += 1

    for j in liste_e:
        if j > 0:
            bit = 1
        elif j < 0:
            bit = 0

        gamma += str(bit)
        epsilon += str(1-bit)

    gamma = int(gamma,2)
    epsilon = int(epsilon,2)
    
    return gamma * epsilon


def oxygene():
    lines = input()
    lines2 = lines.copy()

    oxy = ''
    for i in range(len(lines2)):
        lines2[i] = lines2[i][:-1]
    lines = lines2.copy()
    while len(lines) > 0 and len(lines[0]) > 0:
        lines2 = lines.copy()
        nb_zero = 0
        nb_un = 0

        for ligne in lines2 :
            if ligne[0] == '0':
                nb_zero += 1
            elif ligne[0] == '1':
                nb_un += 1

        for ligne in lines2:
                
            if (ligne[0] == '1') and nb_zero > nb_un :
                lines.remove(ligne)

            elif (ligne[0] == '0') and nb_un >= nb_zero :
                lines.remove(ligne)


        for ligne in range(len(lines)):
            lines[ligne] = lines[ligne][1:]

        if len(lines) == 0:
            oxy += lines2[0]
            return int(oxy,2)

        if nb_zero <= nb_un:
            oxy += '1'
        else:
            oxy += '0'

    return int(oxy,2) 



def co2():
    lines = input()
    lines2 = lines.copy()

    co = ''
    for i in range(len(lines2)):
        lines2[i] = lines2[i][:-1]
    lines = lines2.copy()
    while len(lines) > 0 and len(lines[0]) > 0:
        lines2 = lines.copy()
        nb_zero = 0
        nb_un = 0

        for ligne in lines2 :
            if ligne[0] == '0':
                nb_zero += 1
            elif ligne[0] == '1':
                nb_un += 1

        for ligne in lines2:
                
            if (ligne[0] == '1') and nb_un >= nb_zero :
                lines.remove(ligne)

            elif (ligne[0] == '0') and nb_zero > nb_un :
                lines.remove(ligne)


        for ligne in range(len(lines)):
            lines[ligne] = lines[ligne][1:]

        if len(lines) == 0:
            co += lines2[0]
            return int(co,2)

        if nb_zero <= nb_un:
            co += '0'
        else:
            co += '1'
        

    return int(co,2) 





if __name__=="__main__":
    print(electrique())
    print(oxygene())
    print(co2())
    print(oxygene()*co2())
