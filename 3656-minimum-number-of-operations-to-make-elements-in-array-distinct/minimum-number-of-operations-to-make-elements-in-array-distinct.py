class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        freq = Counter(nums)


        if len(nums) <= 3:
            return 1 if len(set(nums)) != len(nums) else 0 

        def isdistinct():
            for key, val in freq.items():
                if val > 1:
                    return False
            return True


        ptr = 0
        o = 0
        while True:

            if isdistinct():
                break

            if len(nums) - ptr < 3:
                o += 1
                break

            
            o += 1

            freq[nums[ptr]] -= 1
            freq[nums[ptr + 1]] -= 1
            freq[nums[ptr + 2]] -= 1
            ptr += 3

            


        
        return o

        