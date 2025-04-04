#Day 2: 30 Days of pyhton programming
firstname= "John"
lastname= "Mwangi"
fullname= "John Mwangi"
country= "Kenya"
city= "Nairobi"
age= 18
year= 2025
Is_married= "true"
Is_true= "yes"
Is_light_on="yes or no"


#Checking the datatype of the variables
print(type(firstname))
print(type(lastname))
print(type(Is_light_on))
print(len(firstname))

#Comparing of length
if len(firstname)> len(lastname):
    print('first name is longer')
if len(firstname)<len (lastname):
    print('last name is longer')
else:
    print('Both are the same length.')

num_one = 5
num_two = 4 
print(num_one+num_two)
diff = num_one - num_two
print(diff)  #Output: 1
product = (num_two * num_one)
print(product)
division = num_one / num_two 
print(division) #Output:1.25
remainder = num_two % num_one
print(remainder)
exp = num_one**num_two
print(exp)
floor_division = num_one // num_two
print(floor_division)

radius = 30
import math;
#Calculating area of the circle
area_of_circle = math.pi* radius **2

#Calculating circumference of the circle
circum_of_circle = 2 * math.pi * radius

print("Area of cirlce:", area_of_circle)
print("Circumference of circle:", circum_of_circle)

#Taking radius as user input and calculating area
user_radius  = float(input("Enter the radius of the circle:"))
user_area_of_circle = math.pi * user_radius ** 2

print("Area of circle with user input radius:", user_area_of_circle)

# Taking user details as input
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
country = input("Enter your country: ")
age = input("Enter your age: ")

print("User Details:")
print("First Name:", first_name)
print("Last Name:", last_name)
print("Country:", country)
print("Age:", age)

# Checking Python reserved keywords
help('keywords')

