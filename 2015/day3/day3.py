def houses():
    x = 0
    y = 0
    with open("input.txt") as f:
        lines = f.read()
    ensemble = set()
    for i in lines :
        if i == '^':
            y += 1
        elif i == 'v':
            y -= 1
        elif i == '<':
            x -= 1
        elif i == '>':
            x += 1
        ensemble.add(str((x,y)))
    return len(ensemble)

def houses_robot():
    x_santa, x_robot = 0, 0
    y_santa, y_robot = 0, 0
    ensemble_maisons = set()
    ensemble_maisons.add((0,0))
    with open("input.txt") as f:
        lines = f.read()

    for i in range(0,len(lines),2) :
        if lines[i] == '^':
            y_santa += 1
        elif lines[i] == 'v':
            y_santa -= 1
        elif lines[i] == '<':
            x_santa -= 1
        elif lines[i] == '>':
            x_santa += 1
        ensemble_maisons.add((x_santa,y_santa))

    for i in range(1,len(lines)+1,2) :
        if lines[i] == '^':
            y_robot += 1
        elif lines[i] == 'v':
            y_robot -= 1
        elif lines[i] == '<':
            x_robot -= 1
        elif lines[i] == '>':
            x_robot += 1
        ensemble_maisons.add((x_robot,y_robot))
        
    return len(ensemble_maisons)



if __name__ == "__main__":
    print(houses())
    print(houses_robot())