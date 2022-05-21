""" Dict Comprehesion"""

a = {'UK':"London",
    "India":'Delhi',
    "China":'Bejing',
    "USA":"Washington",
    "France":'Paris'}

b = {y:x for x,y in a.items()}

from pprint import pprint as pp
pp(b)