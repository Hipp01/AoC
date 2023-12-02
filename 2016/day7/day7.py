import re


def input():
    with open("input.txt") as f:
        lines = f.readlines()
    return lines


def extract_elements(sentence):
    elements_inside_brackets = '   '.join(re.findall(r'\[([^\]]*)\]', sentence))
    elements_outside_brackets = '   '.join(re.split(r'\[[^\]]*\]', sentence))
    return elements_outside_brackets, elements_inside_brackets


def is_abba(letters):
    for i in range(1, len(letters) - 2):
        if letters[i - 1] != letters[i] and letters[i] == letters[i + 1] and letters[i - 1] == letters[i + 2]:
            return True
    return False


def set_abas(letters):
    abas = set()
    for i in range(0, len(letters) - 2):
        if letters[i] == letters[i + 2] and letters[i] != letters[i + 1]:
            aba = str(letters[i]) + str(letters[i + 1]) + str(letters[i + 2])
            abas.add(aba)
    return abas


def main():
    lines = input()
    cpt_abbas = 0
    cpt_abas = 0
    for line in lines:
        elts = extract_elements(line)
        if is_abba(elts[0]) and not is_abba(elts[1]):
            cpt_abbas += 1

        abas = set_abas(elts[0])
        babs = set_abas(elts[1])
        line_is_aba = False

        for aba in abas:
            bab = aba[1] + aba[0] + aba[1]
            if bab in babs and not line_is_aba:
                cpt_abas += 1
                line_is_aba = True

    print(cpt_abbas)
    print(cpt_abas)


if __name__ == "__main__":
    main()
