def increase_1():
    increase = 0
    with open("input.txt") as f:
        lines = f.readlines()
    for i in range(len(lines)-1) :
        depth = int(lines[i])
        depth_plus_un = int(lines[i+1])
        if depth_plus_un > depth :
            increase += 1
    return increase

def increase_2():
    increase = 0
    with open("input.txt") as f:
        lines = f.readlines()

    for i in range(len(lines)-3) :
        depth = int(lines[i])
        depth_plus_un = int(lines[i+1])
        depth_plus_deux = int(lines[i+2])
        depth_plus_trois = int(lines[i+3])
        fenetre_un = depth + depth_plus_un + depth_plus_deux
        fenetre_deux = depth_plus_un + depth_plus_deux + depth_plus_trois
        if fenetre_deux > fenetre_un:
            increase += 1
    return increase
            


if __name__ == "__main__":
    print(increase_1())
    print(increase_2())