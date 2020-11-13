from flask import Flask, request

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
            return "Яркость всех точек ниже порога"
        else:
            xadd = xadd / counter
            yadd = yadd / counter
            return "Среднее значение координат по икс {}, а по игрек {}".format(xadd, yadd)


# Чтобы протестировать программу нужно ввести
# http://127.0.0.1:5000/start?max_value=6

if __name__ == '__main__':

    app = Flask(__name__)

    @app.route('/start')
    def start_robot():
        max_value = request.args.get('max_value')

        if (max_value == None):
            max_value = 0
        else:
            max_value = int(max_value)
        
        img = Image(7)
        result = img.get_middlepoint(max_value)

        return result
    

    app.run(debug=True)

