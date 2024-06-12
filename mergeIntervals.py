import numpy as np
import random

class Solution:
    def __init__(self, intervals):
        self.__intervals = intervals

    def getIntervals(self):
        return self.__intervals

    def mergeIntervals(self):
        # Helpful in two things:
        #       For A,B in intervals: A[0] < B[0]
        #       For the overlap rule: A[1] > B[0] --> Overlap exists
        #       If not sorted, then not only A to B but B to A checking would have been necessary.
        self.getIntervals().sort(key = lambda x: x[0])
        print("Sorted Input Random Interval list:", self.getIntervals())
        merged = []
        for interval in self.getIntervals():
            #################### SMALL_NOTE_NOT_SO_SMALL ####################################
            # `not merged` == True --> merged is empty, right.
            # Although I knew this, it took long time to focus on it because
            # I was obsessed with second operand being false --> there exists an overlap.
            # In the if-block we'll see that we only append intervals in intervals which
            # are not overlapped with any other.
            #####################################################################
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
                # merged.append([interval[0], merged[-1][1]]): No need this obv.
        return merged

def generate_random_intervals(n, low, high, interval_range):
    """
    This function creates intervals from random numbers between `low` and `high`, where `n`
    is the length of the `intervals` list and `interval_range` is the max range of each random intervals
    in the list.
    """
        intervals = []
        for _ in range(n):
            start = random.randint(low, high - interval_range)
            end = random.randint(start + 1, start + interval_range)
            intervals.append([start, end])
        return intervals




intervals = generate_random_intervals(6,0,30,5)
print("Unmerged random intervals", intervals)
s = Solution(intervals)
print("overlap merged random intervals", s.mergeIntervals())
