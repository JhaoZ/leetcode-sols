class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        n, m = len(board), len(board[0])

        def crush(i, j):
            add = []
            if board[i][j] == 0:
                return add
            curr = board[i][j]
            # vertical 
            v_counter = 0
            for a in range(i, n):
                if board[a][j] == curr:
                    v_counter += 1
                else:
                    break
            # horizontal
            h_counter = 0            
            for a in range(j, m):
                if board[i][a] == curr:
                    h_counter += 1
                else:
                    break

            if v_counter >= 3:
                for a in range(v_counter):
                    add.append((i+a,j))
            
            if h_counter >= 3:
                for a in range(h_counter):
                    add.append((i,j+a))
            

            return add
        
        def drop():
            for i in reversed(range(n)):
                for j in range(m):
                    if board[i][j] == 0:
                        # look up
                        counter = 0
                        for a in reversed(range(0, i)):
                            if board[a][j] != 0:
                                board[i][j] = board[a][j]
                                board[a][j] = 0
                                break




        while True:
            to_remove = []
            for i in range(n):
                for j in range(m):
                    to_remove.extend(crush(i, j))

            if len(to_remove) == 0:
                break
            
            for a, b in to_remove:
                board[a][b] = 0

            # drop
            drop()

        return board
                