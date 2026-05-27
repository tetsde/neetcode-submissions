class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]

        square = {}

        for r in range(3):
            for c in range(3):
                square[(r,c)] = set()
            
      

        for r in range(9):
            for c in range(9):
                val = board[r][c]

                if val == ".":
                    continue

                box_toado = (r//3,c//3)
                    
                if (val in rows[r] or
                        val in cols[c] or 
                        val in square[box_toado]): 
                        return False

                rows[r].add(val)
                cols[c].add(val)
                square[box_toado].add(val)

        return True

                    

                
