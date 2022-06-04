class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        return self.traverse("", 0, 0, n)

    def traverse(self, s: str, open: int, close: int, n: int) -> list[str]:
        if close == n:
            return [s]

        l = []

        if open < n:
            l += self.traverse(s+"(", open+1, close, n)
        if open > close:
            l += self.traverse(s+")", open, close+1, n)

        return l
