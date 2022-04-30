from typing import Optional


class Solution():
    def three_sum_closest(self, nums: list[int], target: int) -> Optional[int]:
        if len(nums) < 3:
            return None

        nums = sorted(nums)
        ans = nums[0] + nums[1] + nums[2]

        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1,len(nums)):
                    s = nums[i] + nums[j] + nums[k]
                    if abs(s - target) < abs(ans - target):
                        ans = s
                    if s > target:
                        break

        return ans

if __name__ == '__main__':
    sol = Solution()
    print(sol.three_sum_closest([0,0,0], 2))
    print(sol.three_sum_closest([-1,2,1,-4], 1))
    print(sol.three_sum_closest([-4,-3,-1,2,3], 0))
