class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        pals = set()  
        def gen(pos, curr):
            if pos >= (n + 1) // 2:
                if n % 2 == 1:
                    test = curr + curr[:-1][::-1]
                    if int(test) % k == 0:
                        pals.add(''.join(sorted(test)))
                else:
                    test = curr + curr[::-1]
                    if int(test) % k == 0:
                        pals.add(''.join(sorted(test)))
                return
            
            for i in range(0, 10):
                gen(pos + 1, curr + str(i))
        
        for i in range(1, 10):
            gen(1, str(i))

        count = 0

        print(pals)

        for pal in pals:
            freq = Counter(pal)
            denom = 1
            for key, val in freq.items():
                denom *= math.factorial(val)
            
            zero_cnt = 0
            if "0" in freq:
                zero_cnt = freq["0"]

            num = math.factorial((len(pal) - 1)) * (len(pal) - zero_cnt)

            count += num // denom
        
        return count

                

        