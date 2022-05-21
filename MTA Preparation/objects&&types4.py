""" Python's Type Stream """

## Python has a dynamic and strong type system

def add(a,b):
    return a+b

# This shows the strong dynamism of python 
print(add(5,7))
print(add('Hi',' Hrithik'))
print(add(4.5,3.2))
print(add([1,2,3],[4,5,6]))

'''Conclusion 
    Python will not generally perform implicit conversions
    between types
   Exception to this Rule:
        Convertng to Bool in if statment and while loop '''