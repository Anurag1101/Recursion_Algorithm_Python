# Program 1
# Recursive function to count down from n to 1
def count_down(n): 
    if n == 0:  # Base case: When n reaches 0, stop the recursion
        return
    print(n)  # Print the current number
    count_down(n - 1)  # Recursive call to count down from the next number

# Calling the count_down function with n 
n=int(input("Enter the number: "))
count_down(n)

# Program 2
# Recursive function to calculate the factorial of a number
def factorial(n): 
    if n == 0 or n == 1:  # Base case: Factorial of 0 and 1 is 1
        return 1
    else:
        return factorial(n - 1) * n  # Recursive call to calculate factorial of n-1

# Print the factorial of n
n=int(input("Enter the number: "))
print(factorial(n))

# Program 3
# Recursive function to calculate the sum of first n natural numbers
def sum_natural_numbers(n): 
    if n == 0:  # Base case: Sum of first 0 natural numbers is 0
        return 0
    return sum_natural_numbers(n - 1) + n  # Recursive call to sum numbers from n-1

# Print the sum of first n natural numbers
n=int(input("Enter the value of n: "))
print(sum_natural_numbers(n))

#Program 4

# Recursive function to print each element of a list
def print_list_elements(li, index=0): 
    if index == len(li):  # Base case: When index reaches the length of the list, stop
        return
    print(li[index])  # Print the element at the current index
    print_list_elements(li, index + 1)  # Recursive call to move to the next index

# Define a list of fruits
fruits = ["apple", "mango", "banana", "guava"]

# Call the function to print each fruit in the list
print_list_elements(fruits)

