from typing import List


class Solution:
    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        # Run the first completed task as late as possible to optimise overlap

        tasks = sorted(tasks, key=lambda x: x[1])

        used_time = [0 for _ in range(tasks[-1][1])]

        for s, e, d in tasks:
            # The current tasks might be able to use the "on" time from the previous tasks
            # Therefore we need to calculate the time needed by the current process
            needed_time = d - sum(used_time[s - 1 : e])
            i = e
            while i >= s and needed_time > 0:
                if used_time[i - 1] == 0:
                    needed_time -= 1
                    used_time[i - 1] = 1
                i -= 1

        return sum(used_time)
