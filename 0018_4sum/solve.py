class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        if len(nums) < 4:
            return []

        nums.sort()
        ans = []
        for i in range(len(nums) - 3):
            if i > 0 and nums[i-1] == nums[i]:
                continue # Since we have covered this case
            for j in range(i+1, len(nums)-2):
                if j > i + 1 and nums[j-1] == nums[j]:
                    continue # Since we have covered this case

                l, r = j+1, len(nums)-1
                while l < r:
                    s = nums[i] + nums[j] + nums[l] + nums[r]
                    if s > target:
                        r -= 1
                        while l < r and nums[r] == nums[r+1]:
                            r -= 1
                    elif s < target:
                        l += 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                    else:
                        ans.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                        while l < r and nums[r] == nums[r+1]:
                            r -= 1

        return ans
