class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        if len(nums) < 3:
            return []

        nums_cnt = {}

        # Get the count for each number that appeared
        for i in range(len(nums)):
            if nums[i] in nums_cnt:
                nums_cnt[nums[i]] += 1
            else:
                nums_cnt[nums[i]] = 1

        nums_cnt_keys = sorted(list(nums_cnt.keys()))
        ret = []

        for i in range(len(nums_cnt_keys)):
            # if there's no duplicate of num i, we cannot use it again
            # therefore, we make a combination with the next digit
            num1 = nums_cnt_keys[i]
            loop_start = i + 1 if nums_cnt[nums_cnt_keys[i]] == 1 else i

            for j in range(loop_start, len(nums_cnt_keys)):
                num2 = nums_cnt_keys[j]
                num3 = 0 - num1 - num2

                if num3 in nums_cnt:
                    # we check the cases where num3 is equal or bigger than num2
                    # if it is bigger, we have likely used it before, since nums_cnt_keys is sorted
                    if num3 > num2:
                        ret.append([num1, num2, num3])
                    elif num2 == num3:
                        # We have to see if we can use the number by seeing the number of times we have already used it
                        use_cnt = 0
                        if num1 == num3:
                            use_cnt += 1
                        if num2 == num3:
                            use_cnt += 1
                        if nums_cnt[num3] > use_cnt:
                            ret.append([num1, num2, num3])

        return ret
