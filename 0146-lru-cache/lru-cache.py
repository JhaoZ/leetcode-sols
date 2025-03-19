class LRUCache:

    def __init__(self, capacity: int):
        self.dict = OrderedDict()
        self.cap = capacity
        

    def get(self, key: int) -> int:
        if key in self.dict:
            value = self.dict[key]
            self.dict.move_to_end(key)
            return value
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.dict[key] = value
            self.dict.move_to_end(key)
        else:
            self.dict[key] = value
            
            if len(self.dict) > self.cap:
                self.cap -= 1
                self.dict.popitem(last = False)

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)