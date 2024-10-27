# Fibonacci Sequence Generator (4 ქულა)
# Create a program that receives an integer n and returns the first n numbers in the Fibonacci sequence. The sequence starts with 0 and 1, and each subsequent number is the sum of the previous two.
# Examples:
# 5 --> [0, 1, 1, 2, 3]
# 7 --> [0, 1, 1, 2, 3, 5, 8]

def fibonacci_square_generator(n):
    sequence = [0,1]
    while len (sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:n]

print (fibonacci_square_generator(5))
print (fibonacci_square_generator(7))