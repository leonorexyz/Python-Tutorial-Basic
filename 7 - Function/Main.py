def persegi(s):
    area = s ** 2
    return area

def segitiga(s,t):
    area = 0.5*s*t
    return area

def lingkaran(s):
    if(s%7==0):
        area = s * 22/7
    else:
        area = 3.14 * (s**2)
    return area

print(segitiga(5,10))