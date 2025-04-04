
#Basic if statement to check if a number is positive,negative or zero
num = int(input("Enter a number: "))
if num > 0:
    print(num, "is a positive.")
elif num ==0:
    print(num,"is neither positive or negative,it is zero")
else:
    print(num,"is a negative number.")
print("outside boby of if statement")

#program for calculating the sum in a list
sum = 0
list = [1,2,3,4,5,6,7,8,9,10]
for i in list:
    sum +=i
    print("sum +i")
    print(range(10))
    alist=list(range(10))
    #Range with 2 parameters
    print(range(2,8))
    listb=list(range(2,8))
    print("Print the whole listb:", listb)
    #Range actually takes three parameters
    print(range(0,10,2))
    listc=list(range(0,10,2))
    print('print the listc: ',listc)

    
