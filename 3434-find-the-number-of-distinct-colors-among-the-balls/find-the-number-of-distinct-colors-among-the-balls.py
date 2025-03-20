class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ball = {}
        color = {}
        ans = []
        for b, c in queries:
            if b in ball:
                curr_color = ball[b]
                color[curr_color] -= 1
                if color[curr_color] == 0:
                    del color[curr_color]

                ball[b] = c
                if c not in color:
                    color[c] = 0
                color[c] += 1
            else:
                ball[b] = c
                if c not in color:
                    color[c] = 0
                color[c] += 1
            ans.append(len(color.keys()))
        return ans
