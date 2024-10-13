def mailing_adress(name, email):
    print(f'Mailing Adress\nName:{name} \nEmail:{email}')

#2. Hello
def user_greetings(user_name):
    print(f'Hello {user_name}'.title())

#3.Area of Room
def area_of_room(width, height):
    width = float(input('Enter width: '))
    length = float(input('Enter length: '))
    area = width * length
    print(f'There are {area} square feet in an area')

#Bottle Deposits    
def size_container():
    small_container =  int(input('Enter the size of small container: '))
    large_container = int(input('Enter the size of large container: '))
    
   
    total_refund = (small_container * 0.10) + (large_container * 0.25)
    
    print(f'The total refund is ${total_refund:.2f}')
   
    
#meal taxes
def meal_tax():
    meal_cost = int(input('Enter the meal cost: '))
    
    tip_amount = meal_cost * (18/100)
    meal_with_tax = meal_cost * (20/100)
    total_cost = meal_cost + tip_amount + meal_with_tax
    
    print(f'Total cost of the meal is {total_cost:.2f}')

#sum of first positive integars
def positive_integers(n):
    n = int(input('Enter the number: '))
    if n > 0:
        total_sum = (n(n+1)//2) 
        print(f'Total cost of the number is {total_sum:.2f}')
        
    else:
        print('Enter a positive integar')       
            
        
    
# Widgets and gizzos
def retail_seller():
    widget_no = int(input('Enter the number of widgets: '))
    gizmos_no = int(input('Enter the no of gizmos: '))
    
    total_weight = (gizmos_no * 112) + (widget_no * 75)
    
    print(f'total weight is {total_weight}')
    
#Interest Rate
def cinterest_rate():
    amount = int(input('Enter amount: '))
    interest = amount * (4/100)
    amount_with_interest = amount + interest
    print(f'Amount {amount_with_interest} after adding the interest rate')
   
#Arithmetic
def calculation(a, b):
    
    sum = a + b
    diference = b - a
    product = a * b
    
    print(f'sum: {sum}\ndifference: {diference}\nproduct: {product}')
    
    
#Fuel Efficiency
def fuel_efficiency():
    USA = float(input('Enter the Value: '))
    MPG = 235.215 / USA
    print(f'Afetr conversion into MPG {MPG:.2f} is value')
    
#Distance between two points on earth
# import math
# def points_dist(lat1, lat2, lon1, lon2):
#     t1 = math.radians(lat1)
#     t2 = math.radians(lat2)
#     g1 = math.radians(lon1)
#     g2 = math.radians(lon2)
#     distance = 6371.01 * math.acos(math.sin(t1) * math.sin(t2) + math.cos(t1) * math.cos(t2) * math.cos(g1 - g2))  
#     return distance
    
# lat1 = float(input('Enter Value of lat1: '))
# lat2 = float(input('Enter Value of lat2: '))
# lon1 = float(input('Enter Value of long1: '))
# lon2 = float(input('Enter Value of long2: '))
# distance = points_dist(lat1, lat2, lon1, lon2)
# print(f'{distance:.2f}')

def cash_measure():
    cash = float(input('Enter cash: '))
    cash_in_cents = int(cash * 100)
    
    one_dollar = {'quarters': 25,
        'dimes': 10,
        'nickels': 5,
        'pennies': 1}

    for key, value in one_dollar.items():
       count = cash_in_cents // value
       cash_in_cents %= value
       
       print(f'value in cents {count}')
    

            
#Height Units
def find_height():
    height_with = int(input('Enter the height: '))  
    inches = int(input('Enter the inches: '))
    
    height = height_with * inches * 2.54
    print(f'Height in inches {height}cm')
    
#Distance Units
def find_dist_units(feet):
    # feet = int(input('Enter the value in meters: '))
    miles = feet/5280
    
    meters = feet * 0.3048
    
    yards = feet / 3
    
    print(f'Value of feet in meters {meters:.2f}, in miles {miles:.3f} and in {yards:.2f}')
    
#Area and Volume
import math
def area_volume(radius):
    area = math.pi * radius ** 2
    volume = (4 / 3) * math.pi * radius ** 3
    
    print(f'Circle area: {area:.2f}, circle volume: {volume:.2f}')
    
#Volume of Cylinder
def cylinder_vol():
    radius = int(input('Enter the radius: '))
    height = int(input('Enter the height: '))

    vol = radius * height
    print(f'estimated volume of cylinder: "{vol:.2f}')
    
#Free Fall
def find_velocity(vi, a, d):
    v_f = math.sqrt(vi ** 2 + 2 * a * d)
    print(v_f)

#Ideal Gas Law
def gas_law():
    R = 8.34
    V = 12
    P = 20000000
    T = 20
    n = (P * V)/ (R * T )
    print(f'AMount of gas {n:.2f} in clinders')
    
#Triangle Area
def tri_area(b, h):
    area = (b * h) / 2
    
    print(f'Area {area:.2f}')
    
#Convert time to seconds
def time_to_seconds():
    days = int(input('Enter the days: '))
    hours = int(input('Enter the days: '))
    mins = int(input('Enter the days: '))
    seconds = int(input('Enter the days: '))
    
    total_seconds = (days * 86400) + (hours * 3600) + (mins * 60) + seconds 
    print(f'time in seconds is: {total_seconds}')    
    
#Convert Seconds to days, hours, mins
def con_seconds(seconds):
    days = seconds // (24 * 3600)
    seconds %= (24 * 3600)
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    print(f"{days}:{hours:02}:{minutes:02}:{seconds:02}")

#Calculate BMI
def bmi_cal(height, weight):
    bmi = weight / (height * weight) 
    print(f'calculation of bmi: {bmi:.3f} of body')

#Wind Chill
def wind_blow(Ta, V):
    WCI = 13.12 + (0.6215*Ta) - (11.37*V ** 0.16) + (0.3965**Ta*V**0.16)
    print(f'Wind blow is {WCI:.2f} according to temprature and speed.')
    
#Temprature Conversion
def temp_conv(C):
    #from celcius to Kelvin
    K = C + 273.15
    #from kelvin to Farhenhite
    F = (K - 273.15) * 9/5 + 32
    print(f'Tempratue in Kelvin {K:.2f}, and in Farhenhite {F:.2f}')
    
#sum of DIgits
def digit_sum(number):
    digits =[int(digit) for digit in str(number)]
    total_sum = sum(digits)
    formatted_output = '+'.join(str(digit) for digit in digits) + f'={total_sum}'
    print(formatted_output)

#Take three integars and sort them
def sort_numbera(a, b, c):

    list = [a, b, c]
    print(f'sorted list {sorted(list)}')
    print(f'sorted list {max(list)}')
    print(f'sorted list {min(list)}')


def loaf_price():
    loaf_price = 3.49
    discount_rate = 0.60

    # Read the number of loaves of day-old bread from the user
    num_loaves = int(input("Enter the number of day-old loaves: "))

    # Calculate the regular price, discount, and total price
    regular_price = num_loaves * loaf_price
    discount = regular_price * discount_rate
    total_price = regular_price - discount

    # Display the results with two decimal places and aligned output
    print(f"Regular price:  ${regular_price:6.2f}")
    print(f"Discount:       -${discount:6.2f}")
    print(f"Total price:    ${total_price:6.2f}")

    


if __name__ == '__main__':
    
   loaf_price()