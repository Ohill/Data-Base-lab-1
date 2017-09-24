class Students (object):
    def __init__(self):
        self.lst = []
    def __str__(self):
        return ("\n".join(str(x) for x in self.lst))

    def add (self, student):
        self.lst.append(student)