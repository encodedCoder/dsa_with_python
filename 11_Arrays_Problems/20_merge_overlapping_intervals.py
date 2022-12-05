def merge(intervals):
        start_i = intervals[0][0]
        end_i   = intervals[0][1]

        merged_intervals = []
        i = 0
        while i < len(intervals)-1:
            if end_i >= intervals[i+1][0]:
                start_i = min(start_i, intervals[i+1][0])
                end_i   = max(end_i, intervals[i+1][1])
            else:
                merged_intervals.append([start_i, end_i])
                start_i = intervals[i+1][0]
                end_i   = intervals[i+1][1]
            i += 1
        merged_intervals.append([start_i, end_i])

        return merged_intervals



intervals = [[1,3],[2,6],[8,10],[15,18]]
intervals = [[1,4],[4,5]]
intervals = [[1,4],[0,4]]
intervals = [[1,4],[0,1]]
intervals = [[1,4],[0,0]]
print(merge(intervals))