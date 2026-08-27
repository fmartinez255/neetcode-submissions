class DynamicArray:
    
    def __init__(self, capacity: int):
        self.arr = [0] * capacity
        self.capacity = capacity
        self.length = 0

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.length == self.capacity:
            self.resize()

        self.arr[self.length] = n
        self.length += 1

    def popback(self) -> int:
        pop = self.arr[self.length-1]
        self.length -= 1

        return pop

    def resize(self) -> None:
        self.capacity = 2 * self.capacity
        tempArr = [0] * self.capacity

        for i in range(self.length):
            tempArr[i] = self.arr[i]

        self.arr = tempArr

    def getSize(self) -> int:
        return self.length
    
    def getCapacity(self) -> int:
        return self.capacity
