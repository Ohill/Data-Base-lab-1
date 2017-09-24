class Group(object):
    def __init__(self, number, facultet, universitet):
        self.number = number
        self.facultet = facultet
        self.universitet = universitet
    def __str__(self):
        return  "University: %s Facultet: %s Number: %s  "  %( self.universitet,self.facultet,self.number)