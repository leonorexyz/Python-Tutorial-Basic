def addSet(*args):
    result = 0
    for data in args:
        result += data
    return result

def multiplySet(*args):
    result = 1
    for data in args:
        result *= data
    return result

def power(n:int):
    return lambda x: x ** n