class Solution:
    def isValid(self, s: str) -> bool:
        paren_stack = []
        for c in s:
            if c in ('(','{','['):
                paren_stack.append(c)
            else:
                if len(paren_stack) == 0:
                    return False
                c_open = paren_stack.pop()
                match c_open:
                    case '(':
                        matching_paren = ')'
                    case '{':
                        matching_paren = '}'
                    case '[':
                        matching_paren = ']'
                    case _:
                        return False
                if c != matching_paren:
                    return False
        return len(paren_stack) == 0
