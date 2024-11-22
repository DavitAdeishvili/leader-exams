# 10) "Eureka" numbers (5 ქულა)

# The Eureka numbers are numbers like this: 135 = 1^1 + 3^2 + 5^3. Which means that we have to take a number and sum its digits raised to the consecutive powers.
# First digit to power 1, second to power 2 and so on... If the result of that sum is the same as the number itself that means that number is Eureka.

# Create a function which receives a range like (a, b) and outputs every Eureka number in it.

# NOTE: Every number which has one digit is Eureka, because for example 5 = 5^1...

# Examples:
# 1, 10  --> [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 1, 100 --> [1, 2, 3, 4, 5, 6, 7, 8, 9, 89]


def eureka_numbers (start, end):
    eureka_numbers = []
    for num in range (start, end+1):
        num_str = str(num)
        total = 0
        for i in range (len(num_str)):
            digit = int (num_str[i])
            position = i + 1
            total += digit ** position
        if total == num:
            eureka_numbers.append(num)
    return eureka_numbers
        

print (eureka_numbers(1,10))
print (eureka_numbers(1,100))