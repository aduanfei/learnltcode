class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.encoding=encoding
        self.count=[x for i,x in enumerate(encoding) if i%2==0]
        self.ind=0

    def next(self, n: int) -> int:
        for i in range(n):
            while (self.count[self.ind]==0):
                self.ind=self.ind+1
                if self.ind>=len(self.count):
                    return -1
            self.count[self.ind]= self.count[self.ind]-1
        return  self.encoding[self.ind*2+1]


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)