class StockPrice:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
        self.time = {}
        self.current_price = None
        self.maxTimeStamp = -1

    def update(self, timestamp: int, price: int) -> None:
        if timestamp >= self.maxTimeStamp:
            self.current_price = price
            self.maxTimeStamp = timestamp
        self.time[timestamp] = price
        heapq.heappush(self.minHeap, (price, timestamp))
        heapq.heappush(self.maxHeap, (-price, timestamp))
        

    def current(self) -> int:
        return self.current_price
        

    def maximum(self) -> int:
        while -self.maxHeap[0][0] != self.time[self.maxHeap[0][1]]:
            heapq.heappop(self.maxHeap)
        return -self.maxHeap[0][0]

    def minimum(self) -> int:
        while self.minHeap[0][0] != self.time[self.minHeap[0][1]]:
            heapq.heappop(self.minHeap)
        return self.minHeap[0][0]
        


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()