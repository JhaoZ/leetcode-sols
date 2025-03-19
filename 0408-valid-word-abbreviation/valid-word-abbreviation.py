class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        p1 = 0
        p2 = 0
        while p1 < len(abbr):
            if p2 >= len(word):
                break
            if abbr[p1].isdigit():
                if abbr[p1] == '0':
                    return False
                curr = 0
                while p1 < len(abbr) and abbr[p1].isdigit():
                    curr = curr * 10 + int(abbr[p1])
                    p1 += 1
                p2 += curr
                if p2 >= len(word):
                    break
            else:
                if word[p2] != abbr[p1]:
                    return False
                p2 += 1
                p1 += 1
        return p1 == len(abbr) and p2 == len(word)
        