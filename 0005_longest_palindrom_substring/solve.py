class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        ans = s[0]
        i = 0 # Center start index
        j = 1 # Center end index

        while j < len(s):
            for x in range(min(i+1, len(s)-j)): # check palindrome from center
                if s[i-x] != s[j+x]:
                    # not possible to find longer palindrome from this center
                    break

                l_palindrome = x * 2 + j - i + 1
                if l_palindrome > len(ans):
                    ans = s[i-x:j+x+1]

            if j - i == 0: # step through all possible center
                j += 1
            else:
                i += 1

        return ans

if __name__ == '__main__':
    print(Solution().longestPalindrome("aabbccb"))
