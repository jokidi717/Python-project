for i in range(10):
    print(i)
    i = 10
    while i<=0:
      print(i)
      i+=1
for i in range(10,-1,-1):
    print(i)
i=10
while i>=0:
       print(i)
       i-=1

for i in range(1,8):
    print("*"*i)

for i in range(8):
    print("#"*8)

for i in range(11):
    print(f"{i} x {i} ={i*i}")

list = ["Python","Numpy","Pandas","Django","Flask"]
for lists in list:
    print(list)
for i in range(101):
  if(i%2==1):
   print(i)
for i in range(101):
    if(i%2!=1):
     print(i)
total_sum = 0
for i in range(101):
  total_sum += i
print(f"The sum of all numbers is {total_sum}")

sum = 0
for i in range(101):
  if(i%2==1):
   sum +=i
   print(f"The sum of all odd numbers{sum} ")

total_sum =0
for i in range(101):
    if(i%2!=1):
     total_sum += i
    print(f"The sum of even number{total_sum}")
           # A program that reads a sequence of numbers
# and counts how many numbers are even and how many are odd.
# The program terminates when zero is entered.
 
odd_numbers = 0
even_numbers = 0
 
# Read the first number.
number = int(input("Enter a number or type 0 to stop: "))
 
# 0 terminates execution.
while number != 0:
    # Check if the number is odd.
    if number % 2 == 1:
        # Increase the odd_numbers counter.
        odd_numbers += 1
    else:
        # Increase the even_numbers counter.
        even_numbers += 1
    # Read the next number.
    number = int(input("Enter a number or type 0 to stop: "))
 
# Print results.
print("Odd numbers count:", odd_numbers)
print("Even numbers count:", even_numbers)
for i in range(2, 8):
    print(i)
