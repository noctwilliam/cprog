// Merge Intervals:
// Problem : Given a collection of intervals, merge overlapping intervals.Solution : Sort the intervals based on their start times and then iterate through the sorted intervals, merging any overlapping intervals and storing the merged intervals in a new list.

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Interval{
    int start;
    int end;
};

bool compareIntervals(const Interval &a, const Interval &b){
    return a.start < b.start;
}

vector<Interval> mergeIntervals(vector<Interval> &intervals){
    if (intervals.empty()){
        return intervals;
    }

    sort(intervals.begin(), intervals.end(), compareIntervals);

    vector<Interval> mergedIntervals;
    mergedIntervals.push_back(intervals[0]);

    for (int i = 1; i < intervals.size(); ++i){
        Interval &currentInterval = intervals[i];
        Interval &lastMergedInterval = mergedIntervals.back();

        if (currentInterval.start <= lastMergedInterval.end) {
            lastMergedInterval.end = max(currentInterval.end, lastMergedInterval.end);
        }
        else{
            mergedIntervals.push_back(currentInterval);
        }
    }

    return mergedIntervals;
}

void printIntervals(const vector<Interval> &intervals){
    for (const Interval &interval : intervals){
        cout << "[" << interval.start << ", " << interval.end << "] ";
    }
    cout << endl;
}

int main(){
    vector<Interval> intervals = {{1, 4}, {3, 6}, {8, 10}, {15, 18}};

    cout << "Original intervals: ";
    printIntervals(intervals);

    vector<Interval> mergedIntervals = mergeIntervals(intervals);

    cout << "Merged intervals: ";
    printIntervals(mergedIntervals);

    return 0;
}

