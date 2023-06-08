print('Welcome to BetterLife BMI System')
bmi_set = {}


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
        return f"{self.name}, bmi={self.bmi}"


class Group:
    def __init__(self):
        self.pList = []

    def addPeope(self, p):
        self.pList.append(p)

    def getData():
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
            bmi = round(w/(h**2), 1)
            bmi_set[n] = bmi
            print('{} with {}kg, {}m and BMI {} is added'.format(n, w, h, bmi))
            return bmi_set

    def __str__(self):
        s = 'The name of the group: '
        peopleStr = [str(p) for p in self.pList]
        s += ', '.join(peopleStr)
        return s

# set 100 random people


def setVirtualData():
    import random as r
    group = Group()
    for i in range(10):
        n = 'p' + str(i)
        h = r.randint(150, 170)/100
        w = r.randint(50, 100)
        p = People(n, h, w)
        print(p)
        group.addPeope(p)
    print(group)


def main():
    print('-------------------------------')
    print('   Better Life Health Report   ')
    print('-------------------------------')
    setVirtualData()


# 程式的入口點
if __name__ == "__main__":
    main()
