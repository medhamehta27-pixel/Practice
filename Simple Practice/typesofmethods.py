#Types of Methods Static, Class , Instance

class Student:
    school = 'Test school name' # Class variable

    def __init__(self, m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self): #instance method since we are passing self mutators changing value
        return (self.m1 + self.m2 + self.m3)/3

    def get_m1(self): #instance method since we are passing self accessors
        return self.m1

    @classmethod
    def getSchool(cls):
        return cls.school

    @staticmethod
    def info():
        print('this is Student class..... in abc module')

s1 = Student(12,13,18)
s2 = Student(19,10,18)

print(s1.avg())
print(s2.avg())

print(Student.getSchool())

Student.info()