"""Passing Arguments and return Values"""

m = [1,12,34]
def modify(k):
    k.append(20)
    print('k = ',k)
modify(m)
print(m)