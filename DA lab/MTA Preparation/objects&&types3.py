"""Function Arguments"""
def banner(message,border='-'):
    line = border * len(message)
    print(line)
    print(message)
    print(line)

    # When assing default arguments , the parameters should come after default arguments not before
a = banner("How are you")

from ast import Add
import time
from turtle import delay 

print(time.ctime())

def show_default(arg = time.ctime()):
    print(arg)

show_default()
time.sleep(1)
show_default()
# The time doesnt change 
'''Result 
    Usually immutable default arguments dont cause any problems but mutable default arguments cause confusing effects
    '''
# Another example 

def add_spam(lst = []):
    lst.append('spam')
    return lst

breakfast = ['eggs','bread']
add_spam(breakfast)
print(breakfast)

print(add_spam())
print(add_spam())
print(add_spam())
# Infinetely spam gets added on 

'''Solution 
    Always use Immutable object or use the none operator and check for none'''

def add_spam(arg=None):
    if arg == None:
        arg = []
    arg.append('spam')
    return arg

print('\n')
breakfast = ['eggs','bread']
add_spam(breakfast)
print(breakfast)

print(add_spam())
print(add_spam())
print(add_spam())