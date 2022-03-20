class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        ans = ""
        for i in range(numRows):
            ans += getRow(s, i, numRows)

        return ans

def getRow(s, i, numRows):
    x = i
    row = ""
    isVertical = True        # Is next character appearing on the vertical stroke
    jump = (numRows - 1) * 2 # Value difference between vertical stroke
    jump1 = jump - (2 * i)   # Calculation for diagonal numbers (first increase)
    jump2 = jump - jump1     # Calculation for diagonal numbers (second increase)

    while x < len(s):
        row += s[x]

        if i > 0 and i < numRows - 1:
            if isVertical:
                x += jump1
            else:
                x += jump2
            isVertical = not isVertical
        else:
            x += jump

    return row

if __name__ == '__main__':
    print(Solution().convert("abcdefghijklmnopqrstuvwxyz", 3))
