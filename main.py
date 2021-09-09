'''
@Author: Rakesh Yadav
@Date: 07/09/21
'''

rows = 8  # rows = int(input())
cols = 8  # cols = int(input())
given = [[0 for i in range(cols)] for j in range(rows)]
# inactive positions within the grids are as marked with -1
given[3][0] = -1
given[0][2] = -1
given[7][0] = -1
given[6][2] = -1
given[3][4] = -1
given[7][6] = -1
given[1][7] = -1


class Solution:
    # function for Bishop's move within the grids
    def bishopMove(self, cr1, cc1):
        if self.ans is None:
            if cr1 < 0 or cc1 < 0 or cr1 >= self.rows or cc1 >= self.cols or self.given[cr1][cc1] == -1 or \
                    self.mat[cr1][cc1] == 2:
                return
            self.mat[cr1][cc1] += 2
            if self.mat[cr1][cc1] == 3:
                self.ans = str(cr1) + ',' + str(cc1)
                return
            self.bishopMove(cr1 + 1, cc1 + 1)
            self.bishopMove(cr1 + 1, cc1 - 1)
            self.bishopMove(cr1 - 1, cc1 + 1)
            self.bishopMove(cr1 - 1, cc1 - 1)

            self.mat[cr1][cc1] -= 2

    # function for Horse's move within the grids
    def horseMove(self, cr1, cc1, cr2, cc2):
        if self.ans is None:
            if cr2 < 0 or cc2 < 0 or cr2 >= self.rows or cc2 >= self.cols or self.mat[cr2][cc2] == 1 or self.given[cr2][
                cc2] == -1:
                return
            self.mat[cr2][cc2] += 1

            self.bishopMove(cr1, cc1)

            self.horseMove(cr1, cc1, cr2 - 2, cc2 - 1)
            self.horseMove(cr1, cc1, cr2 - 2, cc2 + 1)

            self.horseMove(cr1, cc1, cr2 + 2, cc2 - 1)
            self.horseMove(cr1, cc1, cr2 + 2, cc2 + 1)

            self.horseMove(cr1, cc1, cr2 - 1, cc2 - 2)
            self.horseMove(cr1, cc1, cr2 - 1, cc2 + 2)

            self.horseMove(cr1, cc1, cr2 + 1, cc2 - 2)
            self.horseMove(cr1, cc1, cr2 + 1, cc2 + 2)

            self.mat[cr2][cc2] -= 1

    # solve(<matrix of N,M>,<(x,y)-Bishop's position>, <(x,y)-Horse's position>)
    def solve(self, given, cr1, cc1, cr2, cc2):
        self.given = given
        self.rows = len(given)
        self.cols = len(given[0])
        self.ans = None
        self.mat = self.given.copy()
        # initial Bishop position will be fixed for each step taken by horse;
        # 1 coordinates for Bishop and 2 coordinates for Horse
        # CC = current column, cr = current row
        self.horseMove(cr1, cc1, cr2, cc2)

        return self.ans


print(Solution().solve(given, 3, 2, 6, 6))
