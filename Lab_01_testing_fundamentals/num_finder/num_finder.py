class NumFinder:
    def __init__(self):
        self.smallest = float('inf')
        self.largest = float('-inf')

    def find(self, nums):
        for n in nums:
            if n < self.smallest:
                self.smallest = n
            if n > self.largest:
                self.largest = n