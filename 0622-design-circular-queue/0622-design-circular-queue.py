class MyCircularQueue:

    def __init__(self, k):
        self.c = 0
        self.k = k
        self.q = [0 for _ in range(k)]
        self.f = self.r = -1
        
    def enQueue(self, value):
        if self.c == self.k: 
            return False
        else:
            if self.r == -1:
                self.r = self.f = 0
            else:
                self.r += 1
                if self.r == self.k:
                    self.r = 0
            self.q[self.r] = value
            self.c += 1
            return True
        
    def deQueue(self):
        if self.c == 0: 
            return False
        if self.f == self.r:
            self.f = self.r = -1
        else:
            self.f += 1
            if self.f == self.k:
                self.f = 0
        self.c -= 1
        return True
        

    def Front(self):
        if self.c == 0: 
            return -1
        
        return self.q[self.f]

    def Rear(self):
        if self.c == 0:
            return -1
        
        return self.q[self.r]

    def isEmpty(self):
        return self.c == 0

    def isFull(self):
        return self.c == self.k