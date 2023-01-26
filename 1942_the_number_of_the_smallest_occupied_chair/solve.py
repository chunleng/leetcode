from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        event_times = []
        for friend, time in enumerate(times):
            event_times.append((time[0], 1, friend))  # enter
            event_times.append((time[1], 0, friend))  # leave

        heapify(event_times)

        total_seats = 0
        seats = {}
        empty_seats = []
        while event_times:
            _, evt, friend = heappop(event_times)
            if evt == 1:  # enter
                if empty_seats:
                    seats[friend] = heappop(empty_seats)
                else:
                    seats[friend] = total_seats
                    total_seats += 1

                if friend == targetFriend:
                    return seats[friend]
            else:
                heappush(empty_seats, seats[friend])
