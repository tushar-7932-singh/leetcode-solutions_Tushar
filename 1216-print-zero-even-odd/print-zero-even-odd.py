from threading import Semaphore

class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.z = Semaphore(1)
        self.o = Semaphore(0)
        self.e = Semaphore(0)

    def zero(self, printNumber):
        for i in range(1, self.n + 1):
            self.z.acquire()
            printNumber(0)

            if i % 2:
                self.o.release()
            else:
                self.e.release()

    def even(self, printNumber):
        for i in range(2, self.n + 1, 2):
            self.e.acquire()
            printNumber(i)
            self.z.release()

    def odd(self, printNumber):
        for i in range(1, self.n + 1, 2):
            self.o.acquire()
            printNumber(i)
            self.z.release()