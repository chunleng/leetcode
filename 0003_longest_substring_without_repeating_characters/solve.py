class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == '':
            return 0

        ans = 1
        i = 0           # current check index start
        j = 0           # current check index end
        d = {} # dictionary with the latest index if each character, for checking repeats

        while j < len(s):
            if d.get(s[j], -1) >= i: # check dictionary for character in the search range
                i = d[s[j]] + 1
            else:
                d[s[j]] = j
                j += 1
                ans = max(ans, j-i)

        return ans

if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring("abcbcd"))
