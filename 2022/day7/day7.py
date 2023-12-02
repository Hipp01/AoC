def input():
    with open("input2.txt") as f:
        lines = f.read()
    return lines


def tree_files(lines):
    tree = {}
    lines = lines.split("\n")
    # print(lines)
    for i in range(len(lines)):
        lines[i] = lines[i].split(" ")
        lines[i] = [x for x in lines[i] if len(x) > 0 and x[0].isnumeric()]
        print(lines[i])
        
        
        # for j in range(len(lines[i])):
        #     if j == 0:
        #         tree[lines[i][j]] = []
        #     else:
        #         tree[lines[i][0]].append(lines[i][j])

    return tree

    # for i in range(len(lines)):
    #     lines[i] = lines[i].split("\n")
    #     lines[i] = [x for x in lines[i] if len(x) >0 and x[0].isnumeric()]
    #     # print(lines[i])
    #     for j in range(len(lines[i])):
    #         if j == 0:
    #             tree[lines[i][j]] = []
    #         else:
    #             tree[lines[i][0]].append(lines[i][j])

    # return tree






def main():
    lines = input()
    print(tree_files(lines))


if __name__ == "__main__":
    main()
