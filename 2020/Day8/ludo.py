import os
import re


class Program:

    INSTRUCTION = r'(acc|jmp|nop) ([+-]\d+)'

    def __init__(self, instructions):
        self.instructions = instructions
        self.num_of_instr = len(instructions)
        self.acc = 0
        self.index = 0
        self.executed = set()

    def __next(self):
        if self.index == self.num_of_instr:
            return False
        if self.index in self.executed:
            return True

        self.executed.add(self.index)
        instruction = self.instructions[self.index]
        op, amount = re.search(self.INSTRUCTION, instruction).groups()
        amount = int(amount)

        if op == 'acc':
            self.acc += amount

        self.index += 1 if op != 'jmp' else amount

        return self.__next()

    def execute(self):
        return self.__next()

    @classmethod
    def solve(cls, instructions):
        replace = {'jmp': 'nop', 'nop': 'jmp'}

        for i, instr in enumerate(instructions):
            op, amount = re.search(cls.INSTRUCTION, instr).groups()

            if op == 'acc':
                continue

            new_op = replace[op]

            new_instr = list(instructions)
            new_instr[i] = instr.replace(op, new_op)

            p = cls(new_instr)
            loop = p.execute()

            if not loop:
                return p.acc


def main():
    with open(os.getcwd() + '/input.txt') as f:
        instructions = f.read().splitlines()

    print(Program.solve(instructions))


if __name__ == "__main__":
    main()