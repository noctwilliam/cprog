'''
Merge Intervals:
Problem : Given a collection of intervals, merge overlapping intervals.
Solution : Sort the intervals based on their start times and then iterate through the sorted intervals, merging any overlapping intervals and storing the merged intervals in a new list.
Set of Intervals: {1,4}, {2,5}, {7,9}
Intervals (obj) are to be stored in a list
'''

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __lt__(self, other):
        return self.start < other.start

def merge_intervals(intervals):
    if not intervals:
        return intervals

    intervals.sort()

    merged = []
    merged.append(intervals[0]) #append the first interval to the list

    for i in range(1, len(intervals)):
        current_interval = intervals[i] #current interval is the second interval in the list
        last_merged_interval = merged[-1] 

        if current_interval.start <= last_merged_interval.end:
            last_merged_interval.end = max(current_interval.end, last_merged_interval.end)
        else:
            merged.append(current_interval)

    return merged

def print_intervals(intervals):
    for interval in intervals:
        print('[', interval.start, ',', interval.end, '] ', sep='', end='')

def main():
    intervals = [Interval(1, 4), Interval(3, 6), Interval(8, 10), Interval(15, 18)]

    print('Original intervals: ')
    print_intervals(intervals)
    merged_intervals = merge_intervals(intervals)

    print('\nMerged intervals: ')
    print_intervals(merged_intervals)

if __name__ == '__main__':
    main()