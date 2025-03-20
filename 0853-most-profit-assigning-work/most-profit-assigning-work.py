class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        arr = [(difficulty[i], profit[i]) for i in range(len(difficulty))]
        arr.sort(key = lambda x : (x[0], x[1]))
        money = 0
        
        start = 0
        current_max = 0
        end = 0
        worker_pt = 0
        worker.sort()
        while worker_pt < len(worker):
            work = worker[worker_pt]
            temp = current_max
            while end < len(arr) and arr[end][0] <= work:
                if arr[end][1] > temp:
                    start = end
                    current_max = arr[start][1]
                    temp = arr[end][1]
                end += 1
            money += current_max
            worker_pt += 1
        return money
        