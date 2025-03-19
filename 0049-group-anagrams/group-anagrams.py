class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            can = ''.join(sorted(s))
            groups[can].append(s)
        return list(groups.values())
