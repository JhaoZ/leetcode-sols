class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:

        if numerator == 0:
            return str(0)

        neg = 0
        if numerator < 0:
            neg += 1
            numerator = abs(numerator)
        if denominator < 0:
            neg += 1
            denominator = abs(denominator)

        ans = str(numerator // denominator)
        if numerator % denominator == 0:
            if neg == 1:
                return "-" + ans
            return ans
        ans += "."

        n, d = str(numerator % denominator), denominator

        past = ""
        curr = numerator % denominator
        idx = 1
        seen = {curr: 0}
        dup = False
        while curr != 0:
            curr =  curr * 10 
            print(curr)
            if curr in seen:
                dup = True
                break
            seen[curr] = idx

            div = curr // d
            past += str(div)
            curr -= div * d
            
            
            idx += 1

        if dup:
            idx = seen[curr]
            past = past[:idx - 1] + "(" + past[idx - 1:] + ")"
        
        return ans + past if neg != 1 else "-" + ans + past