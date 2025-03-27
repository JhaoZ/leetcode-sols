class MyCircularQueue:

    def __init__(self, k: int):
        self.insert_ptr = 0
        self.remove_ptr = 0
        self.size = 0
        self.data = [None] * k
        

    def enQueue(self, value: int) -> bool:
        if self.data[self.insert_ptr] == None:
            self.data[self.insert_ptr] = value
            self.insert_ptr += 1
            self.insert_ptr %= len(self.data)
            self.size += 1
            return True
        else:
            return False
        

    def deQueue(self) -> bool:
        if self.data[self.remove_ptr] != None:
            self.data[self.remove_ptr] = None
            self.size -= 1
            self.remove_ptr += 1
            self.remove_ptr %= len(self.data)
            return True
        else:
            return False
        
        

    def Rear(self) -> int:
        rear_ptr = self.insert_ptr - 1
        if rear_ptr < 0:
            rear_ptr = len(self.data) - 1
        return self.data[rear_ptr] if self.data[rear_ptr] != None else -1
        

    def Front(self) -> int:
        return self.data[self.remove_ptr] if self.data[self.remove_ptr] != None else -1
        

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == len(self.data)
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()