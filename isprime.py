'''
Name: Godfred Opintan
Student_ID: 10955081
DCIT 104: Programming Fundamentals
Assignment: Write a programme to calculate the sum of prime numbers from to a given number
'''
'''
Prime numbers are numbers can be divided by only 1 and the given number. 
'''
def isPrime(number):
    #Defines a function isPrime which takes a number and check whether it is a prime number or not
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

#Inputs a number
endpoint = int(input("Enter a number \n"))
sum = 0 #A variable to sum up prime numbers

#Loops to find prime number
for i in range(2, endpoint):
    if isPrime(i):
        sum += i

print(sum)       