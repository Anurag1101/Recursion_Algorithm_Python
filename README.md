**Recursive Algorithms in Python**

This repository contains several recursive functions that demonstrate how recursion can be used to solve different types of problems. Recursion is a programming technique where a function calls itself to solve a problem, breaking it down into smaller instances until it reaches a base case.

**Programs Included**:

**1. Countdown Program**:
   
This program demonstrates a recursive function to count down from a given number n to 1. It takes a positive integer as input and prints each number in descending order using recursion.

**Function:** count_down(n)

**Input:** A positive integer n

**Output:** Prints numbers from n to 1

**Base Case:** When n equals 0, the recursion stops.

**Example:**

    Enter the number: 5
    Output: 5
            4
            3
            2
            1
    


**2. Factorial Calculation Program**:

This program calculates the factorial of a number using recursion. Factorial is defined as the product of all positive integers less than or equal to the number. For instance, the factorial of 5 is 5 * 4 * 3 * 2 * 1 = 120.

**Function:** factorial(n)

**Input:** A non-negative integer n

**Output:** The factorial of n

**Base Case:** If n is 0 or 1, the factorial is 1 (as 0! = 1! = 1).

**Example:**

    Enter the number: 6
    Output : 720


**3. Sum of First N Natural Numbers**:

This program calculates the sum of the first n natural numbers (i.e., 1 + 2 + 3 + ... + n) using recursion. The base case is when n is 0, at which point the sum is 0.

**Function:** sum_natural_numbers(n)

**Input:** A non-negative integer n

**Output:** The sum of the first n natural numbers

**Base Case:** If n is 0, the sum is 0.

**Example:**

    Enter the value of n: 20
    Output : 210


**4. Print Elements of a List**:

This program recursively prints each element in a list of fruits. The function takes a list and an optional index (defaulting to 0) as input and prints each element one by one using recursion.

**Function:**  print_list_elements(li, index=0)

**Input:**  A list li and an optional starting index (default is 0)

**Output:** Each element of the list printed in order

**Base Case:**  When the index reaches the length of the list, the recursion stops.

**Example:**

    Output: Fruits in the list:
            apple
            mango
            banana
            guava


How to Run the Programs
Navigate to the folder where the Python files are located. In this case, the folder path is:

bash
Copy code
C:\Users\anura\OneDrive\Desktop\Python\Recursion_Algorithm_Python
Run the Python file:

Open a terminal or command prompt and navigate to the directory:

bash
Copy code
cd "C:\Users\anura\OneDrive\Desktop\Python\Recursion_Algorithm_Python"
Run the Python script:

bash
Copy code
python recursion_programs.py
Provide inputs when prompted for each of the programs, and the output will be displayed directly in the terminal.

Concepts Demonstrated
Recursion: All the programs in this repository are based on the concept of recursion. The key idea is to define a problem in terms of a smaller instance of the same problem, with a base case to stop the recursion.
Base Case: The condition that stops the recursion and prevents an infinite loop.
Recursive Case: The part of the function where it calls itself with a smaller or simpler input.
Contributions
Feel free to fork this repository and submit a pull request if you'd like to contribute new recursive functions or improve the existing code.
