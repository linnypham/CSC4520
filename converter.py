def toBinary(number):
    binary = []
    while number > 0:
        remainder = number % 2
        number//=2
        binary.append(remainder)
    return binary[::-1]

def toHex(number):
    hex = []
    dictionary = {10:'A', 11:'B',12:'C',13:'D',14:'E',15:'F'}
    while number > 0:
        remainder = number % 16
        number//=16
        if remainder in range(0,10):
            hex.append(remainder)
        else:
            hex.append(dictionary[remainder])
    return hex[::-1]