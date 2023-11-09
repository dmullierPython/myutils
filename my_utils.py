import math
def average(values):
    """ Calculates the average of the given list. """
    total = 0;
    for n in values:        	# total the given values
        total += float(n)
    return total/len(values)	# return calculated average

def area_rectangle(width, length):
    area = width * length
    return area

def area_square(length):
    area = area_rectangle(length, length)
    return area

def area_circle(radius):
    area = math.pi*(radius ** 2)
    return area

def area_triangle(base, height):
    area = area_rectangle(base, height)/2
    return area

if __name__ == '__main__':
    print("Area module")
    print("area of a circle with radius of 10 ", area_circle(10))
    print("area of a rectangle of 10,10 ", area_rectangle(10, 10))
    print("area of a square 10 ", area_square(10))
    print("area of a triangle 10,10 ", area_triangle(10, 10))