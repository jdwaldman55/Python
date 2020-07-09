class Car:
    manufacturer = 'Unknown'
    color = 'Unknown'
    cost = 0

    def Recipt(self):
        msg = 'Congratulations on buying your brand new {} {}. Your card will be charged ${}'.format(self.color, self.manufacturer, self.cost)
        return msg
    
class Sedan(Car):
    manufacturer = 'Ford'
    color = 'Blue'
    cost = 25000
    top_speed = 120
    speed_to_60mph = '5 seconds'

    def Recipt(self):
        msg = 'Congratulations on buying your brand new {} {}. Your card will be charged ${}'.format(self.color, self.manufacturer, self.cost)
        return msg


class Convertable(Car):
    manufacturer = 'Ferrari'
    color = 'Red'
    cost = 175000
    top_speed = 195
    speed_to_60mph = '2.3 seconds'

    def Recipt(self):
        msg = 'Congratulations on buying your brand new {} {}. Your card will be charged ${}'.format(self.color, self.manufacturer, self.cost)
        return msg

if __name__ == '__main__':
    sedan = Sedan()
    print(sedan.Recipt())

    convertable = Convertable()
    print(convertable.Recipt())
    
    

    
