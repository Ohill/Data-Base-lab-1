class Groups (object):
    def __init__(self):
        self.lst = []
    def __str__(self):
        return ("\n".join(str(x) for x in self.lst))

    def add (self, group):
        tmp = True
        for x in self.lst :
            if (x.number ==  group.number) and (x.facultet == group.facultet) and  (x.universitet == group.universitet):
                tmp = False
        if tmp==True:
            self.lst.append(group)
        return tmp
