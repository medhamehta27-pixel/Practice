# method Overloding

class Student:

    def __init__(self, m1,m2):
        self.m1 = m1
        self.m2 = m2

    def add(self, m1=None ,m2 = None, m3= None):

        if m1 != None and m2 != None and m3 != None:
            return m1+m2+m3
        
        elif m1 != None and m2 != None:
            return m1+m2
        else:
            return m1

s1= Student(12,13)
print(s1.add(5,10,3))

