from typing import Optional


class Solution():
    def threeSumClosest(self, nums: list[int], target: int) -> Optional[int]:
        if len(nums) < 3:
            return None

        nums.sort()
        ans = nums[0] + nums[1] + nums[2]
        diff = abs(ans - target)

        for i, n in enumerate(nums[:-2]):
            if i > 0 and n == nums[i - 1]:
                continue

            l,r = i + 1, len(nums) - 1

            while l < r:
                s = n + nums[l] + nums[r]
                d = abs(s - target)
                if d < diff:
                    ans = s
                    diff = d

                if s < target:
                    l += 1
                else:
                    r -= 1

        return ans
