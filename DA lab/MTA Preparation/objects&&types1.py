## Everything is an object 

""" IMMUTABLE OBJECTS """
# 1)Assining an Variable 

x = 500
# Python creates int as 1000 and object reference x and x points to 1000 
# Now python creates a new integer object assigning x to point to 500,Now the 1000 cant be reached after this 
# ints are immutable and this lost 1000 will be recollected by python garbage collector after some time 
print(id(x))
x=1000
print(id(x))
'''END CONCLUSION 
 When a new value is assigned to the variable the object reference points to another 
 value strored in some other Address'''

# Checking ID of two variables pointing the same int 
a = 35
b = 46
print(id(a),'  ',id(b))
a = b
print(id(a)==id(b))
'''CONCLUSION
    When two variable are aassigned as eqaul both of them points to the same reference'''
'''Tryout'''
a = 4
b = 4
print(id(a)==id(b))

'''Augmented Asssignment'''
t = 5
print(id(t))
t += 2
print(id(t))

""" MUTABLE OJECTS """
s = [1,3,7]
r = s
r[1]=17
print(s)
'''Result 
    Lists are mutable as , here both r and s points to the same object and when r[1] is changed it affects the list s
    as both points to the same addresss and when values are changed they don't point to a new address but change the 
    values in the existing address '''

p = [1,2,3]
q = [1,2,3]
print(p==q) # Eqaulity 
print(p is q) # Identy Equivalence 

print("\n")
print("---END OF PROGRAM---")