from collections import defaultdict


class Solution:
    def findPairs(self, nums: list[int], k: int) -> int:
        d = defaultdict(int)
        for n in nums:
            d[n] += 1

        ans = 0
        if k == 0:
            for (k, v) in d.items():
                if v > 1:
                    ans += 1
        else:
            for key in d.keys():
                if key + k in d:
                    ans += 1
        return ans
