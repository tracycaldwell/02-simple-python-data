def calculate_rectangle_area(height, width):    
    ## Todo: update `None` to contain the formula for `rectangle_area`
    height = float(input("Enter the height"))
    width = float(input("Enter the width"))
    rectangle_area = height * width
    return rectangle_area
    print ("The rectangle area is:", rectangle_area)

def calculate_area_of_square(side):
    ## Todo: update `None` to contain the formula for `squre_area`
    side = float(input("Enter the side length"))
    square_area = (side)**2
    return square_area
   print ("The square area is:", square_area)

def calculate_total_plus_tip_per_person(total_bill, tip_percent, number_of_people):
    ## Todo: update `None` to contain the formula for `total_plus_tip_` and `total_plus_tip_per_person`.
    total_bill= float(input("Enter the total bill value"))
    tip_percent= float(input("Enter the tip percentage as a decimal))
    number_of_people = int(input("Enter the number of people"))
    total_plus_tip = total_bill + (total_bill * tip_percent)
    total_plus_tip_per_person = total_plus_tip / number_of_people
    return total_plus_tip_per_person
    print("The total per person is:", total_plus_tip_per_person)

def fahrenheit_to_celcius(degrees):
    ## Todo: update `None` to contain the formula for `degrees_in_celcius`
    ## use the formula (F - 32) × 5/9 = C
    degrees = float(input("Degrees in Fahrenheit"))
    degrees_in_celcius = (degrees - 32) * (5/9)
    return degrees_in_celcius
    print("The degrees in Celcius is:", degrees_in_celcius)

def calculate_the_remainder(num1, num2):
    ## Todo: update `None` to contain the formula for `remainder`
    num1 = float(input("Enter number 1"))
    num2 = float(input("Enter number 2"))
    remainder = num1 % num2
    return remainder
    print("The remainder is:", remainder)
