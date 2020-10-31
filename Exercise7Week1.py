import math
def get_circle_perimeter(radius):
    perimeter = 2 * math.pi * radius
    return perimeter
def get_circle_area(radius):
    area = math.pi * radius**2
    return area
## Example of concatenation.
def print_name():
    first_name = input('Whats you first name? ')
    last_name = input('Whats you last name? ')
    print(type(first_name))
    #type casting
    print(last_name+', '+first_name)
##  print(last_name+', '+first_name)
    print()
def print_circle_perandarea(radius):
    print(get_circle_perimeter(radius))
    print(get_circle_area(radius))
