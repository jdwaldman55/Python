class Student:
    def __init__(self):
        self._fname = 'Jordan'
        self.__lname = 'Waldman'

    def getfname(self):
        print(self.__lname)

    def setlname(self,private):
        self.__lname = private

obj = Student()
obj._fname = 'Jordan'
obj.getfname()
print(obj._fname)

        

