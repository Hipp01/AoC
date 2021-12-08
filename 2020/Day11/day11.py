def separe_text():
    f = open("test.txt","r")
    a = f.read().split('\n')
    f.close()
    return a

def main_v1():
    a = separe_text()
    for i in range(len(a)) :
        for j in range(len(a[i])) :
            if a[i][j] == 'L' and (a[i][j-1] == ('#' or '.') and (a[i][j+1] == ('#' or '.'):
                a[i][j] = '#'
            


def change_l(l):
    l.split('.')
    for i in l :
        for j in i:
            pass
        





# l = LLLLLLLL.LLLL.LLLLL.LLLLLLLLLLLLLL.LLLLLLLLLLLLLL.LLLLL.LLLLLLLLLLLLLL.LLLLLLL.LLLLLL.LLLLLLLLLL.L
