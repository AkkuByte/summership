""" •a code which is a function that takes two numbers as input and returns the
GCD of the two numbers and also computes the number of steps.
Outputs the
number of steps and the GCD. Show the intermediate steps of the Euclidean algorithm. """
def gcd(a, b):
    steps = 0
    while b:
        steps += 1
        print(f"Step {steps}: a = {a}, b = {b}")
        a, b = b, a % b
    print(f"GCD is {a} and it took {steps} steps.")
    return a    
# Example usage:
# take two numbers as input
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
gcd(num1, num2) 