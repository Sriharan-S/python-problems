# The provided code stub reads two integers from STDIN,  and . Add code to print three lines where:

# The first line contains the sum of the two numbers.
# The second line contains the difference of the two numbers (first - second).
# The third line contains the product of the two numbers.
# Example


# Print the following:

# 8
# -2
# 15
# Input Format

# The first line contains the first integer, .
# The second line contains the second integer, .

# Output Format

# Print the three lines as explained above.

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(f"{a+b}\n{a-b}\n{a*b}")
