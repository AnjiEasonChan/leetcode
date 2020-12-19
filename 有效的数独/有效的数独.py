class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [{} for _ in range(9)]
        col = [{} for _ in range(9)]
        grid = [[{} for _ in range(3)] for _ in range(3)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    tmp = int(board[i][j])
                    row[i][tmp] = row[i].get(tmp, 0) + 1
                    col[j][tmp] = col[j].get(tmp, 0) + 1
                    grid[i//3][j//3][tmp] = grid[i//3][j//3].get(tmp, 0) + 1
                    if row[i].get(tmp) > 1 or col[j].get(tmp) > 1 or grid[i//3][j//3].get(tmp) > 1:
                        return False
        return True
