class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if s == "" and p == "":
            return True
        if p == "":
            return False

        # optimize pattern
        # a*.* -> .*
        # .*a* -> .*
        # a*a* -> a*
        i = 0
        while i < len(p) - 3:
            if p[i+1] == '*' and p[i+3] == '*':
                if p[i] == '.' or p[i+2] == '.':
                    p = p[:i] + ".*" + p[i+4:]
                    i = max(i-2,0)
                elif p[i] == p[i+2]:
                    p = p[:i+2] + p[i+4:]
                    i = max(i-2, 0)
                else:
                    i += 1
            else:
                i += 1
        return self.traverse(s, p)

    def traverse(self, s, p) -> bool:
        if s == "":
            # return True if all the remaining pattern are optional
            if len(p) % 2 == 1:
                return False
            for i in range(1,len(p),2):
                if p[i] != "*":
                    return False
            return True
        if p == "":
            return False

        # Cases
        # a == a  -> s[1:], p[1:]               (match and next)
        # a == a* -> s, p[2:] || s[1:], p       (dont' match || match and continue)
        # a == b  -> False                      (fail to match)
        # a == b* -> s, p[2:]                   (fail to match and continue)

        if p[0] == "." or s[0] == p[0]:
            if len(p) > 1 and p[1] == "*":
                return self.traverse(s[1:], p) or self.traverse(s,p[2:])
            return self.traverse(s[1:], p[1:])

        if len(p) > 1 and p[1] == "*":
            return self.traverse(s, p[2:])

        return False
