"""Lists"""

'''Slicing '''
# List[start:Stop]

a = "Hi da Saketh, this is Hrithik da talking to you".split()
print(a)
print(a.index("Saketh,"))
# Returns the index 

print(a.count('da'))

del a[1]
print(a)

a.remove('da')
print(a)

a.insert(2,'poriki')
print(a)

a.reverse()
print(a)

m = [21,33,45,12,32,98,44,3]
m.sort()
print(m)
m.sort(reverse=True)
print(m)

# Use sorted and reversed function to get a new list 
