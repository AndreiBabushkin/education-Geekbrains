import time
class TrafficLight:
    def __init__(self):
        __color = 0
    def running (self):
            self.__color = 'красный'
            print(self.__color)
            time.sleep(7)
            self.__color = 'желтый'
            print(self.__color)
            time.sleep(2)
            self.__color = 'зеленый'
            print(self.__color)
            time.sleep(5)
t = TrafficLight()
while True:
    t.running()

