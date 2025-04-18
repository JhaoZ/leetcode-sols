class Solution:
    @cache
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        seq = self.countAndSay(n - 1)
        s = ""
        counter = 0
        curr = ""
        for ch in seq:
            if curr == "":
                curr = ch
                counter += 1
            elif curr != ch:
                s += str(counter) + curr
                counter = 1
                curr = ch
            else:
                counter += 1
        if counter > 0:
            s += str(counter) + curr
        return s