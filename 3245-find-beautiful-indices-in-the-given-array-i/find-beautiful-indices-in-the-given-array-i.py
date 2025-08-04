class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        a_idx = [i for i in range(len(s) - len(a) + 1) if s[i:i+len(a)] == a]
        b_idx = [i for i in range(len(s) - len(b) + 1) if s[i:i+len(b)] == b]
        ans = []
        if not b_idx or not a_idx:
            return ans
        for idx in a_idx:
            b_itr = bisect.bisect_right(b_idx, idx)
           
            if b_itr == len(b_idx):
                if abs(b_idx[b_itr - 1] - idx) <= k:
                    ans.append(idx)
            else:
                if abs(b_idx[b_itr] - idx) <= k or abs(b_idx[b_itr - 1] - idx) <= k:
                    ans.append(idx)
        return ans