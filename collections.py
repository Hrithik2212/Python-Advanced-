from collections import Counter
from collections import namedtuple
from collections import OrderedDict
from collections import deque
a="aaaaaabbcccc"
my_counter=Counter(a)
## prints the elements frequency preseng in the container and returns a dict 
## returns a dict
print(my_counter)

print(my_counter.values())##returns a list of frequencies

### most common element 
## takes int as arg and returns a list of tuples
print(my_counter.most_common(2))

print("\n\n")
""" ===Named Tuple==== """

Point = namedtuple('Point','x,y')
## Creates a class Point
pt = Point(1,-4)
print(pt.x,pt.y)

""" ===OrderedDict=== """
## Its like regular Dict but the order of the elements are remembered
ordered_dict=OrderedDict()
ordered_dict['a']=1
ordered_dict['b']=2
ordered_dict['c']=3
ordered_dict['d']=4
print(ordered_dict)
## After python 3.7 normal dict work same as OrderedDict

""" ===Deque=== """
d=deque()
d.append(1)
d.append(2)
d.appendleft(3)
d.pop()
print(d)
d.popleft()
print(d)
d.clear()
print(d)
d.append(1)
d.append(2)
d.appendleft(3)
d.extendleft([4,5,6])
print(d)
d.rotate(1)
print(d)