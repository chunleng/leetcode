from typing import Final


class Solution:
    MIN: Final[int] = -2147483648
    MAX: Final[int] = 2147483647
    def myAtoi(self, s: str) -> int:
        negate = False
        ret = 0
        i = 0

        for i in range(len(s)):
            if s[i] != " ":
                break

        if i < len(s):
            if s[i] == "+":
                i += 1
            elif s[i] == "-":
                i += 1
                negate = True

        for i in range(i,len(s)):
            if s[i] == "0":
                ret *= 10
            elif s[i] == "1":
                ret = ret * 10 + 1
            elif s[i] == "2":
                ret = ret * 10 + 2
            elif s[i] == "3":
                ret = ret * 10 + 3
            elif s[i] == "4":
                ret = ret * 10 + 4
            elif s[i] == "5":
                ret = ret * 10 + 5
            elif s[i] == "6":
                ret = ret * 10 + 6
            elif s[i] == "7":
                ret = ret * 10 + 7
            elif s[i] == "8":
                ret = ret * 10 + 8
            elif s[i] == "9":
                ret = ret * 10 + 9
            else:
                break

        if negate:
            ret *= -1
            if ret < self.MIN:
                ret = self.MIN
        elif ret > self.MAX:
            ret = self.MAX

        return ret
