class Image(object):    
    def __init__(self, value):
        self.mas = []

        for i in range(256):
            self.mas.append([])

            for j in range(256):
                self.mas[i].append(value)

    def get_middlepoint(self, max_value):
        xadd = 0
        yadd = 0
        counter = 0
        
        for i in range(256):
            for j in range(256):
                if (self.mas[i][j] > max_value):
                    counter = counter + 1
                    xadd = xadd + i
                    yadd = yadd + j

        if (counter == 0):
            print("Яркость всех точек ниже порога")
        else:
            xadd = xadd / counter
            yadd = yadd / counter
            print("Среднее значение координат по икс {}, а по игрек {}".format(xadd, yadd))



if __name__ == '__main__':
    max_value = int( input('Введите порог яркости: ') )

    img = Image(7)
    img.get_middlepoint(max_value)


