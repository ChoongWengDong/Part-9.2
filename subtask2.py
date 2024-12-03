def sequence_stats():
    n = 0  # Counter for numbers
    s = 0  # Sum of numbers
    m = None  # Minimum value (start as None for easy comparison)

    print("Enter numbers separated by commas or spaces (-1 to end):")
    
    # Take input as a single line
    input_line = input()

    # Split the input by commas or spaces, and convert to integers
    inputs = [int(x) for x in input_line.replace(",", " ").split()]

    # Iterate over the inputs
    for x in inputs:
        if x == -1:  # Stop if we reach -1
            break
        
        n += 1  # Increment count
        s += x  # Add to sum
        
        # Update minimum value
        if m is None or x < m:
            m = x

    # Handle case when no valid numbers were entered
    if n == 0:
        return 0, 0, -1, -1  # No valid numbers entered
    
    # Calculate the mean
    a = s / n
    return n, s, m, a

# Example usage
count, total, minimum, mean = sequence_stats()
print(f"Count: {count}")
print(f"Sum: {total}")
print(f"Minimum: {minimum}")
print(f"Mean: {mean}")

# it looks like I learned how to use git today

