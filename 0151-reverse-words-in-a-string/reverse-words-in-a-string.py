class Solution:
    def reverseWords(self, s: str) -> str:
        arr = []
        curr = ''
        for ch in s:
            if ch != ' ':
                curr += ch
            else:
                if curr != '':
                    arr.append(curr)
                    curr = ''
        if curr != '':
            arr.append(curr)
        return ' '.join(arr[::-1])
        