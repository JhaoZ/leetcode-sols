class Solution:
    def maxDiff(self, num: int) -> int:
        rep = [str(ch) for ch in str(num)]

        find_replacement = 0
        for i in range(len(rep)):
            if rep[i] != '9':
                find_replacement = i
                break
        
        max_rep = rep.copy()
        for i in range(len(max_rep)):
            if max_rep[i] == rep[find_replacement]:
                max_rep[i] = '9'
        
        max_num = int(''.join(max_rep))

        find_replacement = 0
        for i in range(len(rep)):
            if rep[i] != '1' and rep[i] != '0':
                find_replacement = i
                break
        
        min_rep = rep.copy()
        for i in range(len(min_rep)):
            if min_rep[i] == rep[find_replacement]:
                if find_replacement != 0:
                    min_rep[i] = '0'
                else:
                    min_rep[i] = '1'
        min_num = int(''.join(min_rep))
        return max_num - min_num
