class Solution:
    def maxArea(self, height: list[int]) -> int:
        if len(height) < 2:
            return 0
        start, end = 0, len(height) - 1
        current_max = self.calculate_height(height,start,end)

        while start < end:
            if height[start] < height[end]:
                start += 1
            elif height[end] < height[start]:
                end -= 1
            else:
                start += 1
                end -= 1
            current_max = max(current_max, self.calculate_height(height, start, end))

        return current_max

    def calculate_height(self, height: list[int], start, end) -> int:
        return min(height[start], height[end]) * (end-start)
