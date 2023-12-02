# import numpy as np

def input():
    with open("input2.txt") as f:
        lines = f.read()
    return lines


def set_grid():
    grid = 


def main():
    lines = input()
    



if __name__ == "__main__":
    main()







def old():
    return 0
    # def number_edges(lines):
    #     lines = lines.split("\n")
    #     width = len(lines[0])
    #     height = len(lines)
    #     edges = width*2 + height*2 - 4
    #     return edges


    # def visible(lines):
    #     # tree_visible = number_edges(lines)
    #     tree_visible = 0
    #     a = np.array([list(x) for x in lines.split("\n")])
    #     b = np.zeros((len(a), len(a[0])))
    #     # print(b)
    #     # for i in range(1,len(a)-1):
    #     #     for j in range(1,len(a[i])-1):
    #     #         print(a[i][j], a[i][j-1])
    #     #         if (int(a[i][j]) > int(a[i][j-1])) or (int(a[i][j]) > int(a[i][j+1])) or (int(a[i][j]) > int(a[i-1][j])) or (int(a[i][j]) > int(a[i+1][j])):
    #     #             tree_visible += 1
    #     #             b.itemset((i,j), 1)
    #     # print(b)
    #     for i in range(0,len(a)):
    #         b.itemset((i,0), 1)
    #         b.itemset((i,len(a[i])-1), 1)
    #     for i in range(0,len(a[0])):
    #         b.itemset((0,i), 1)
    #         b.itemset((len(a)-1,i), 1)
    #     for i in range(1,len(a)-1):
    #         for j in range(1,len(a[i])-1):
    #             high_range = int(a[i][j-1])
    #             if int(a[i][j]) > high_range:
    #                 high_range = int(a[i][j-1])
    #                 b.itemset((i,j), 1)

    #     for i in range(len(a)-1, 1, -1):
    #         for j in range(len(a[i])-1, 1, -1):
    #             high_range = int(a[i][j-1])
    #             if int(a[i][j]) > high_range:
    #                 high_range = int(a[i][j])
    #                 b.itemset((i,j), 1)
        
    #     print(b)                
    #     return tree_visible
        
        

    # def main():
    #     lines = input()
    #     # print(number_edges(lines))
    #     print(visible(lines))


    # if __name__ == "__main__":
    #     main()