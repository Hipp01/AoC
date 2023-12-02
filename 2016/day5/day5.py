import hashlib


def input():
    with open("input.txt") as f:
        lines = f.read()
    return lines


def five_zeros(code, index_min):
    hashage = ''
    while hashage[:5] != '00000':
        index_min += 1
        to_hash = code + str(index_min)
        hashage = hashlib.md5(to_hash.encode()).hexdigest()
    return index_min, hashage[5], hashage[6]


def main():
    lines = input()
    final_code_1 = ''
    final_code_2 = [''] * 8
    index_min = 0
    for i in range(8):
        tour = five_zeros(lines[:-1], index_min)
        index_min = tour[0]
        final_code_1 += tour[1]
        if tour[1].isdigit() and int(tour[1]) >= 0 and int(tour[1]) <= 7 and final_code_2[int(tour[1])] == '':
            final_code_2[int(tour[1])] = tour[2]
    while '' in final_code_2:
        tour = five_zeros(lines[:-1], index_min)
        index_min = tour[0]
        if tour[1].isdigit() and int(tour[1]) >= 0 and int(tour[1]) <= 7 and final_code_2[int(tour[1])] == '':
            final_code_2[int(tour[1])] = tour[2]
    print(final_code_1)
    print(''.join(final_code_2))


if __name__ == "__main__":
    main()
