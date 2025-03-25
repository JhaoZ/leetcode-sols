class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        x_intervals = []
        y_intervals = []
        
        for start_x, start_y, end_x, end_y in rectangles:
            x_intervals.append([start_x, end_x])
            y_intervals.append([start_y, end_y])
        
        x_intervals.sort(key = lambda x : x[0])
        y_intervals.sort(key = lambda x : x[0])

        def merge_intervals(arr):
            output = []
            for i in range(len(arr)):
                if not output:
                    output.append(arr[i])
                else:
                    if arr[i][0] < output[-1][1]:
                        output[-1][1] = max(output[-1][1], arr[i][1])
                    else:
                        output.append(arr[i])
            return output

        merged_x = merge_intervals(x_intervals)
        merged_y = merge_intervals(y_intervals)

        return len(merged_x) >= 3 or len(merged_y) >= 3