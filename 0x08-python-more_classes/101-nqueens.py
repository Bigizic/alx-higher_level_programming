#!/usr/bin/python3
"""A module for solving the N queen problem
"""
import sys


class NQueensSolver:
    def __init__(self, n):
        self.n = n
        self.solutions = []
        self.pos = None

    def get_input(self):
        if len(sys.argv) != 2:
            print('Usage: nqueens N')
            sys.exit(1)
        try:
            self.n = int(sys.argv[1])
        except Exception:
            print('N must be a number')
            sys.exit(1)
        if self.n < 4:
            print('N must be at least 4')
            sys.exit(1)

    def is_attacking(self, pos0, pos1):
        if (pos0[0] == pos1[0]) or (pos0[1] == pos1[1]):
            return True
        return abs(pos0[0] - pos1[0]) == abs(pos0[1] - pos1[1])

    def group_exists(self, group):
        for stn in self.solutions:
            i = 0
            for stn_pos in stn:
                for grp_pos in group:
                    if stn_pos[0] == grp_pos[0] and stn_pos[1] == grp_pos[1]:
                        i += 1
            if i == self.n:
                return True
        return False

    def build_solution(self, row, group):
        if row == self.n:
            tmp0 = group.copy()
            if not self.group_exists(tmp0):
                self.solutions.append(tmp0)
        else:
            for col in range(self.n):
                a = (row * self.n) + col
                matches = zip(list([self.pos[a]]) * len(group), group)
                used_positions = map(
                        lambda x: self.is_attacking(x[0], x[1]),
                        matches
                    )
                group.append(self.pos[a].copy())
                if not any(used_positions):
                    self.build_solution(row + 1, group)
                group.pop(len(group) - 1)

    def get_solutions(self):
        self.pos = list(map(
            lambda x: [x // self.n, x % self.n], range(self.n ** 2))
        )
        a = 0
        group = []
        self.build_solution(a, group)


solver = NQueensSolver(0)
solver.get_input()
solver.get_solutions()

for solution in solver.solutions:
    print(solution)
