"""
WRITE A FUNCTION 'indices23' as described below. 
You can use any libraries as you see fit. 
(Test your solution before answering here. Write only the function and no additional code.)
"""

def indices23(lst:list):
    copy = lst.copy()
    copy.sort(reverse=True)
    return [lst.index(copy[1]),lst.index(copy[2])]

class MultiplyAdd():
    def __init__(self,m=5,c=5):
        self.m = m
        self.c = c
    
    def run(self,x):
        self.x =x 
        self.y = self.m * self.x +self.c
        return self.y

mult_add = MultiplyAdd(m=3,c=4)

assert mult_add.run(0) == 4
assert indices23(list(range(25))) == [23,22]