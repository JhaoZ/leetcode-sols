class NumArray:

    def merge(self, a, b):
        return a + b

    def build(self, nums, idx, lo, hi):
        if lo == hi:
            self.segtree[idx] = nums[lo]
        else:
            mid = (lo + hi) // 2
            self.build(nums, idx * 2, lo, mid)
            self.build(nums, idx * 2 + 1, mid + 1, hi)
            self.segtree[idx] = self.merge(self.segtree[idx * 2], self.segtree[idx * 2 + 1])

    def query(self, idx, query_lo, query_hi, lo, hi):
        if query_lo > query_hi:
            return 0
        if lo == query_lo and hi == query_hi:
            return self.segtree[idx]
        mid = (lo + hi) // 2
        return self.merge(self.query(idx * 2, query_lo, min(mid, query_hi), lo, mid), self.query(idx * 2 + 1, max(query_lo, mid + 1), query_hi, mid + 1, hi))
    
    def update_tree(self, idx, lo, hi, pos, new_ele):
        if lo == hi:
            self.segtree[idx] = new_ele
        else:
            mid = (lo + hi) // 2
            if pos <= mid:
                self.update_tree(idx * 2, lo, mid, pos, new_ele)
            else:
                self.update_tree(idx * 2 + 1, mid + 1, hi, pos, new_ele)
            
            self.segtree[idx] = self.merge(self.segtree[idx * 2], self.segtree[idx * 2 + 1])


    def __init__(self, nums: List[int]):
        max_n = len(nums) * 4 
        self.n = len(nums)
        self.segtree = [0] * max_n
        self.build(nums, 1, 0, len(nums) - 1)
        

    def update(self, index: int, val: int) -> None:
        self.update_tree(1, 0, self.n - 1, index, val)

    def sumRange(self, left: int, right: int) -> int:
        return self.query(1, left, right, 0, self.n - 1)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)