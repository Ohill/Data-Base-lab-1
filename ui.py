from student import Student
from group import Group
from  groups import Groups
from students import  Students
import pickle
class UI (object):
    def __init__(self):
        self.students = Students()
        self.groups = Groups()
    def choise (self):
        try:
            with open('data.pickle', 'rb') as file:
                self = pickle.load(file)
        except:
            print("Error file")
        while True:

            print ("Start menu:\n\n1.Show all data.\n2.Add student.\n"
                   "3.Change student data.\n4.Delete student.\n5.Add group.\n6.Change group data.\n7.Delete group.\n"
                   "8.Filter.\nQ: Quit of program.")
            chois = input("Enter your choise: ")
            if (chois=="q") or (chois=="Q"):
                with open("data.pickle", 'wb') as file:
                    pickle.dump(self, file)
                break
            elif (chois== "2"):
                self.add_stud()
            elif (chois=="1"):
                self.showall()
            elif (chois=="5"):
                self.add_group()
            elif (chois=="3"):
                self.chg_stud()
            elif (chois=="4"):
                self.del_stud()
            elif (chois=="6"):
                self.chg_grp()
            elif (chois=="7"):
                self.del_group()
            elif (chois == "8"):
                self.filtr()
            else: print("Error value. Try again\n")

    def showall(self):
        print("\nData Base:\n")
        for x in self.groups.lst:
            print(str(x)+":")
            for i in self.students.lst:
                if (x.number == i.group) and (x.universitet == i.universitet):
                    print(str(i))
        print("\nEnter anything for back or (q) for out of program:")
        if(str(input())=="q") :
            exit()
        else: return

    def add_stud (self):
        print("Enter name, universitet, group of student split ENTERS:\n")
        stud = Student(str(input()), str(input()), str(input()),str(input()))
        tmp = True
        for x in self.groups.lst:
            if (x.universitet == stud.universitet) and (x.number == stud.group):
                self.students.add(stud)
                tmp = False
                break
        if (tmp == True):
            print("\n\n---------------------------------\n"
                  "ERROR: You try add student in false group or univetsitet\n"
                  "---------------------------------")
            print("Try again? Y/N :")
            if (str(input())=="Y"):
                self.add_stud()
            else: return
    def add_group (self):
        print("Enter number, facultet and universitet of group split ENTERS:\n")
        group = Group(str(input()), str(input()), str(input()))
        self.groups.add(group)
    def chg_stud(self):
        print("Enter name, universitet, group of student split ENTERS:\n")
        stud = Student(str(input()), str(input()), str(input()),str(input()))
        boolean = True
        for x in self.students.lst:
            if (x.group == stud.group ) and (x.universitet == stud.universitet) and (stud.name == x.name) and (x.age == stud.age):
                boolean = False
                choise = str(input("What do you want to change:\n1.Name\n2.Group\n3.Univetsitet\n4.Age\n5.All\nEnter your choise: "))
                if (choise=="1"):
                    x.name = str(input("Enter new name: "))
                elif(choise=="2"):
                    tmp=True
                    group = str(input("Enter a real group: "))
                    for i in self.groups.lst:
                        if (group==i.number):
                            tmp = False
                            x.group=group
                            break
                    if (tmp == True):
                        print("\n\n---------------------------------\n"
                              "ERROR: This group not real\n"
                              "---------------------------------")
                elif (choise=="3"):
                    tmp = True
                    unvst = str(input("Enter a real Universitet: "))
                    for i in self.groups.lst:
                        if (unvst==i.universitet):
                            tmp = False
                            x.universitet = unvst
                            break
                        if (tmp==True):
                            print("\n\n---------------------------------\n"
                                  "ERROR: This Universitet not real\n"
                                  "---------------------------------")
                elif (choise=="5"):
                    self.students.lst.remove(x)
                    self.add_stud()
                elif (choise=="4"):
                    x.age = str(input("Enter new age: "))

        if (boolean==True):
            print("\n\n---------------------------------\n"
                                  "ERROR: This student was not found\n"
                                  "---------------------------------")

    def del_stud (self):
        print("Enter name, universitet, group of student split ENTERS:\n")
        stud = Student(str(input()), str(input()), str(input()), str(input()))
        for x in self.students.lst:
            if (x.group == stud.group) and (x.universitet == stud.universitet) and (stud.name == x.name) and (stud.age == x.age):
                self.students.lst.remove(x)
                return
        print("\n\n---------------------------------\n"
              "ERROR: This student was not found\n"
              "---------------------------------")
    def chg_grp (self):
        print("Enter number, facultet and universitet of group split ENTERS:\n")
        group = Group(str(input()), str(input()), str(input()))
        boolean = True
        for x in self.groups.lst:
            if (x.number == group.number) and (x.universitet == group.universitet) and (x.facultet == group.facultet):
                boolean = False
                choise = str(input("What do you want to change:\n1.Number\n2.Facultet\n3.Univetsitet\nEnter your choise: "))
                if (choise=="1"):
                    grp  = str(input("Enter new number: "))
                    for i in self.groups.lst:
                        if (grp == i.number) and (group.universitet == i.universitet):
                            print("\n\n---------------------------------\n"
                                  "ERROR: This group already exists\n"
                                  "---------------------------------")
                            return
                    x.number = grp
                    for k in self.students.lst:
                        if (k.universitet == group.universitet) and (k.group==group.number):
                            k.group= grp
                elif (choise == "2"):
                    x.facultet = str(input("Enter new facultet: "))
                elif (choise == "3"):
                    unvrst = str(input("Enter new Universitet: "))
                    for i in self.groups.lst:
                        if (unvrst == i.universitet) and (group.number == i.number):
                            print("\n\n---------------------------------\n"
                                  "ERROR: This group already exists\n"
                                  "---------------------------------")
                            return
                        x.universitet = unvrst
                        for k in self.students.lst:
                            if(k.universitet==group.universitet) and (k.group == group.number):
                                k.universitet = unvrst
                return
        print("\n\n---------------------------------\n"
              "ERROR: This group was not found\n"
              "---------------------------------")

    def del_group(self):
        print("Enter number, facultet and universitet of group split ENTERS:\n")
        group = Group(str(input()), str(input()), str(input()))
        boolean = True
        for x in self.groups.lst:
            if (x.number == group.number) and (x.universitet == group.universitet) and (x.facultet == group.facultet):
                self.groups.lst.remove(x)
                return
        print("\n\n---------------------------------\n"
              "ERROR: This group was not found\n"
              "---------------------------------")


    def filtr (self):
        studnts = []
        min_studnts = []

        for x in self.groups.lst:
            studnts.clear()
            for i in self.students.lst:
                if (i.group == x.number) and (i.universitet==x.universitet):
                    studnts.append(i)
            min = studnts[0]
            min_val = 0
            for k in studnts:
                if (k.age<=min.age):
                    min_val = k.age
            for k in studnts:
                if (k.age == min_val):
                    min_studnts.append(k)
        print("\n".join(str(z) for z in min_studnts) + "\n")





