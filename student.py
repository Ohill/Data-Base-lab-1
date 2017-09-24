class Student (object):
    def __init__(self, name,universitet, group, age ):
        self.name = name
        self.group = group
        self.age = age
        self.universitet = universitet
    def __str__(self):
        return "Name: %s Universitet: %s Group: %s Age: %s " %(self.name,self.universitet ,self.group, self.age)
