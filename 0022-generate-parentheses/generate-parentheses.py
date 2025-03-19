class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        ans = []
        def gen(temp, left_cnt, right_cnt):
            if len(temp) == 2 * n:
                ans.append(temp)
                return
            
            if left_cnt < n:
                gen(temp + '(', left_cnt + 1, right_cnt)
            
            if right_cnt < left_cnt:
                gen(temp + ')', left_cnt, right_cnt + 1)
        gen("", 0, 0)
        return ans