class TicTacToe:

    def __init__(self, n: int):
        self.rows = [0] * n
        self.cols = [0] * n
        self.downDiag = 0
        self.upDiag = 0
        self.n = n
        

    def move(self, row: int, col: int, player: int) -> int:
        place = 1 if player == 1 else -1
        self.rows[row] += place
        if abs(self.rows[row]) == self.n:
            return 1 if self.rows[row] > 0 else 2
        
        self.cols[col] += place
        if abs(self.cols[col]) == self.n:
            return 1 if self.cols[col] > 0 else 2
        
        if row == col:
            self.downDiag += place
            if abs(self.downDiag) == self.n:
                return 1 if self.downDiag > 0 else 2
        if self.n - row - 1 == col:
            self.upDiag += place
            if abs(self.upDiag) == self.n:
                return 1 if self.upDiag > 0 else 2
        return 0

        
        
            
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)