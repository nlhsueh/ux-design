from abc import ABC, abstractmethod
import sys


def bmi(h, w):
    bmi = round(w/(h**2), 1)
    return bmi


class People:
    def __init__(self, name, h, w):
        self.name = name
        self.h = h
        self.w = w
        self.bmi = bmi(self.h, self.w)

    def getBMI(self):
        return bmi

    def __str__(self):
        return f"({self.name},bmi:{self.bmi}), {self.getHealthLevel()}"

    @abstractmethod
    def getHealthLevel(self):
        pass


class GeneralStudent(People):
    def __init__(self, name, h, w):
        super().__init__(name, h, w)

    def getHealthLevel(self):
        if self.bmi >= 24:
            self.hLevel = '太重'
        elif self.bmi < 18:
            self.hLevel = '太輕'
        else:
            self.hLevel = '標準'
        return self.hLevel


class AthleteStudent(People):
    def __init__(self, name, h, w):
        super().__init__(name, h, w)

    def getHealthLevel(self):
        if self.bmi >= 23:
            self.hLevel = '太重'
        elif self.bmi < 19:
            self.hLevel = '太輕'
        else:
            self.hLevel = '標準'
        return self.hLevel


class Group:
    def __init__(self, gName):
        self.pList = []
        self.name = gName

    def addPeople(self, p):
        self.pList.append(p)

    def inputData(self):
        while True:
            go = input('Press G/g to continue input; X/x to stop ')
            if (go == 'X' or go == 'x'):
                break
            elif (go not in ['G', 'g']):
                continue
            n = str(input('Please input the name '))
            while True:
                try:
                    w = float(input('Please input the weight (kg) '))
                except ValueError:
                    print('Input should be a value, please re-input ')
                    continue
                if (w > 500 or w < 10):
                    print('Weight should be in the range (10, 500), please re-input ')
                    continue
                break
            while True:
                try:
                    h = float(input('Please input the height (m) '))
                except ValueError:
                    print('Input should be a value, please re-input ')
                    continue
                if (h > 2.2 or h < 1):
                    print('Height should be in the range (1, 2.2), please re-input ')
                    continue
                break
            p = People(n, h, w)
            self.addPeople(p)
            print(f'{n} with {w}kg, {h}m is added')

    def avgHeight(self):
        h = 0
        for ph in self.pList:
            h += ph.h
        return round(h/len(self.pList), 1)

    def getName(self):
        return self.name

    def __str__(self):
        s = f'Group {self.name} has the people: '
        peopleStr = [str(p) for p in self.pList]
        s += ', '.join(peopleStr)
        return s


# set 100 random people
def setVirtualData(g):
    import random as r
    for i in range(10):
        n = 'p' + str(i)
        h = r.randint(150, 170)/100
        w = r.randint(50, 100)
        p = GeneralStudent(n, h, w)
        g.addPeople(p)


# set People data from console input


def main():
    print('-------------------------------')
    print('   Better Life Health Report   ')
    print('-------------------------------')
    g = Group('FCU')
    arg = sys.argv
    if len(arg) > 1 and arg[1] == 'v':  # v: virtual data input
        # set data from virtual
        setVirtualData(g)
    else:
        # set data from console input
        g.inputData()
    print(g)
    print(f"The average height of {g.getName()} is {g.avgHeight()}m")


# 程式的入口點
if __name__ == "__main__":
    main()
