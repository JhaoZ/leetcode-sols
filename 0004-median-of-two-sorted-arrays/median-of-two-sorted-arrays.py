class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a, b = nums1, nums2
        if len(b) < len(a):
            a, b = b, a
        
        total = len(a) + len(b)
        half = total // 2 
        l = 0
        r = len(a) - 1
        while True:
            i = (l + r) // 2
            j = half - i - 2
        
            left_a = a[i] if i >= 0 else float("-infinity")
            left_b = b[j] if j >= 0 else float("-infinity")
            right_a = a[i + 1] if i + 1 < len(a) else float("infinity")
            right_b = b[j + 1] if j + 1 < len(b) else float("infinity")

            if left_a <= right_b and left_b <= right_a:
                if total % 2 == 1:
                    return min(right_a, right_b)
                else:
                    return (max(left_a, left_b) + min(right_a, right_b)) / 2
            elif left_a > right_b:
                r = i - 1
            else:
                l = i + 1
        return -1