class MyCircularQueue:

    def __init__(self, k):
        self.q = [0] * k
        self.k = k
        self.front = 0
        self.size = 0

    def enQueue(self, value):
        if self.isFull():
            return False

        i = (self.front + self.size) % self.k
        self.q[i] = value
        self.size += 1
        return True

    def deQueue(self):
        if self.isEmpty():
            return False

        self.front = (self.front + 1) % self.k
        self.size -= 1
        return True

    def Front(self):
        if self.isEmpty():
            return -1
        return self.q[self.front]

    def Rear(self):
        if self.isEmpty():
            return -1
        return self.q[(self.front + self.size - 1) % self.k]

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.k