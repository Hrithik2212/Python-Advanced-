""" Tuple"""

# Tuples are immutabe sequence of arbitary objects
 
a = ("Norway",1,3)
print(type(a))


''' Tuple Unpacking '''
# Returning Multiple values from a function 
def min_max(items):
    return min(items),max(items)

mini,maxi=min_max([4,35,23,22,11,54,61])
print(mini," ",maxi)

(a,(b,(c,d)))=(1,("Hrithik",("hey",[1,2,3])))
print(a)
print(b)
print(c)
print(d)

''' Swapping Elements'''
a = 1
b = 2
a,b = b,a
print(f'a = {a}  ,b {b}')
