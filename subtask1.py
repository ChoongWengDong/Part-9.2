def largest_square(n):
    q = 0  # Start with the smallest possible square number
    while (q + 1) ** 2 <= n:  # Check if the next square is still <= n
        q += 1
    return q ** 2  # Return the square of the largest valid q

# Example usage
n = int(input("Enter a number: "))
result = largest_square(n)
print(f"The largest square less than or equal to {n} is {result}")

# it looks like I learned how to use git today
