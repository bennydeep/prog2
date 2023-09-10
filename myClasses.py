class DateofBirthException (Exception):
    pass

class numException (Exception):
    pass

class ugyfelIDException (Exception):
    pass

class tartozikazugyfelException(Exception):
    pass

class MissingDataException(Exception):
    def __init__(self,value):
        self.__value = value

    def __str__(self):
        return "A " + self.__value + " mező üres. Tölts ki mindent, majd próbáld újra"


class Customer:
    def __init__(self, name, id, date, num, balance):
        self.__name = name
        self.__id = id
        self.__date = date
        self.__num = num
        self.__balance = balance


    def getName(self):
        return self.__name

    def setName(self, p):
        self.__name = p

    def getID(self):
        return self.__id

    def getDate(self):
        return self.__date

    def setDate(self, p):
        self.__date = p

    def getNum(self):
        return self.__num

    def setNum(self, p):
        self.__num = p

    def getBalance(self):
        return self.__balance

    def setBalance(self, p):
        self.__balance = p

    def __str__(self):
        return self.__name + ' (ID: ' + str(self.__id) + ') (Egyenleg: ' + str(self.__balance) + ' Ft)'  # ilyen formátumba fogja beletölteni a listába

    def __le__(self, other):
        if self.getName() == other.getName():
            return self.getDate() < other.getDate()
        else:
            return self.getName() < other.getName()

    def __gt__(self, other):
        if self.getName() == other.getName():
            return self.getDate() > other.getDate()
        else:
            return self.getName() > other.getName()

    def __eq__(self, other):
        return self.getID() == other.getID()