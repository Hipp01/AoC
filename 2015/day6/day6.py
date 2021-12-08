import numpy as np

def nb_lights():
    with open("input.txt") as f:
        lines = f.readlines()
    lights = np.array(1000*[1000*[0]])  
    cpt = 0
    for ligne in lines :
        split = ligne.split(' ')
        cmd = 0
        if len(split) == 5:
            cmd = 1
        commande = split[0+cmd]
        begin = split[1+cmd].split(',')
        x_begin = int(begin[0])
        y_begin = int(begin[1])
        end = split[3+cmd].split(',')
        x_end = int(end[0])
        y_end = int(end[1])

        for i in range(y_begin,y_end+1):
            for j in range(x_begin,x_end+1):

                if commande == 'off':
                    lights[j][i] = 0
                elif commande == 'on':
                    lights[j][i] = 1
                elif commande == 'toggle':
                    lights[j][i] = 1-lights[j][i]
        
    for i in np.nditer(lights) :
        cpt += i
    return cpt


def nb_lights2():
    with open("input.txt") as f:
        lines = f.readlines()
    lights = np.array(1000*[1000*[0]])  
    cpt = 0
    for ligne in lines :
        split = ligne.split(' ')
        cmd = 0
        if len(split) == 5:
            cmd = 1
        commande = split[0+cmd]
        begin = split[1+cmd].split(',')
        x_begin = int(begin[0])
        y_begin = int(begin[1])
        end = split[3+cmd].split(',')
        x_end = int(end[0])
        y_end = int(end[1])

        for i in range(y_begin,y_end+1):
            for j in range(x_begin,x_end+1):

                if commande == 'off':
                    lights[j][i] -= 1
                    if lights[j][i] <= 0:
                        lights[j][i] = 0
                elif commande == 'on':
                    lights[j][i] += 1
                elif commande == 'toggle':
                    lights[j][i] += 2
        
    for i in np.nditer(lights) :
        cpt += i
    return cpt
  


if __name__ == "__main__":
    print(nb_lights2())