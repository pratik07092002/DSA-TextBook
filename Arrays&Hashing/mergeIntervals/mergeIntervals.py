from typing import List


def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # first I Sort intervals by start
    intervals.sort(key=lambda x: x[0])

    merged = []
    for interval in intervals:
        # then If merged is empty OR no overlap I add interval
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
        # else I merge by extending the end
            merged[-1][1] = max(merged[-1][1], interval[1])
    return merged  
