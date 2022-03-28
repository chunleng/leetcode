class Solution:
    INT_MAX = 2147483647
    INT_MIN = -2147483648
    def reverse(self, x: int) -> int:
        ans = 0
        is_negative = False
        if x < 0:
            is_negative = True
        x = abs(x)

        while (x != 0):
            pop = x % 10
            x //= 10

            if (not is_negative and
                (ans > self.INT_MAX // 10 or
                (ans == self.INT_MAX // 10 and pop > 7))):
                return 0
            if (is_negative and
                (ans > abs(self.INT_MIN // 10 + 1) or
                (ans == abs(self.INT_MIN // 10 + 1) and pop > 8))):
                return 0
            ans = ans * 10 + pop

        return -ans if is_negative else ans
