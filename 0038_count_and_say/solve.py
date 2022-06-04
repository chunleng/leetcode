class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        s = self.countAndSay(n-1)

        c = s[0]
        p = 1
        acc = 1
        res = ""

        while p < len(s):
            if s[p] == c:
                acc += 1
            else:
                res += str(acc) + c
                c = s[p]
                acc = 1
            p += 1

        return res + str(acc) + c
