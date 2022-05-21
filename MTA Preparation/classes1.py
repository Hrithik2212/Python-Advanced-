"""Intro"""

class flight:
    def __init__(self,number):
        if not number[:2].isalpha():
            raise ValueError(f"No airline code in number")
        self._number = number
    def number(self):
        return self._number


f = flight("SN606")
print(f.number())