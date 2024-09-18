from mathFunction import areaCircle

def pricePizzaRatio(diameter,price):
    area = areaCircle(diameter/2)
    return area/price
