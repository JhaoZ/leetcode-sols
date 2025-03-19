class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:

        row, col = len(isWater), len(isWater[0])
        queue = deque()
        seen = set()

        for i in range(row):
            for j in range(col):
                if isWater[i][j] == 1:
                    queue.append(((i, j), 0))
        
        dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        while queue:
            curr_cord, curr_height = queue.popleft()
            curr_x, curr_y = curr_cord

            if (curr_x, curr_y) in seen:
                continue

            if (curr_x, curr_y) not in seen:
                isWater[curr_x][curr_y] = curr_height
                seen.add((curr_x, curr_y))

            for x, y in dirs:
                new_x = curr_x + x
                new_y = curr_y + y

                if not (0 <= new_x < row and 0 <= new_y < col):
                    continue

                if (new_x, new_y) in seen:
                    continue
                
                queue.append(((new_x, new_y), curr_height + 1))
        return isWater

            
        
        
        