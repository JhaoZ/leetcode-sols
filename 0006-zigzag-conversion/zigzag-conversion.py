class Solution:
    def convert(self, s: str, numRows: int) -> str:
        row_data = [[] for i in range(numRows)] 

        i = 0
        down = True
        while i < len(s):
            if down:
                for j in range(min(numRows, len(s) - i)):
                    row_data[j].append(s[i])
                    i += 1
            else:
                for j in range(min(numRows - 2, len(s) - i)):
                    row_data[numRows - 2 - j].append(s[i])
                    i += 1

            down = not down
        fin_str = ''
        for i in range(numRows):
            fin_str += ''.join(row_data[i])
        return fin_str