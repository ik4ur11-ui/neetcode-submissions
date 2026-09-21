class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        
        box = [["."] * 9 for _ in range (0,9)]
        transposed = [["."] * 9 for _ in range (0,9)]
        c_idx = 0

        for idx, row in enumerate(board):
            if idx % 3 == 0:
                box[c_idx] = board[idx][0:3] + board[idx+1][0:3] + board[idx+2][0:3]
                box[c_idx+1] = board[idx][3:6] + board[idx+1][3:6] + board[idx+2][3:6]
                box[c_idx+2] = board[idx][6:9] + board[idx+1][6:9] + board[idx+2][6:9]
                c_idx += 3
            for i in range (0,9):
                if board[idx][i] != "." and board[idx][i] not in ["1","2","3","4","5","6","7","8","9"]:
                    print("!")
                    return False
                transposed[idx][i] = board[i][idx]

        print(transposed)
        print(box)

        for i in range(9):
            
            row = [x for x in board[i] if x != "."]
            current_box = [x for x in box[i] if x != "."]
            column = [x for x in transposed[i] if x != "."]

            if len(set(row)) != len(row):
                return False

            elif len(set(current_box)) != len(current_box):
                return False

            elif len(set(column)) != len(column):
                return False
        
        return True

        