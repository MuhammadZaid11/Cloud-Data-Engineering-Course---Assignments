# debugging_script.py (Corrected)

def perform_operations(numbers):
    total = 0
    product = 1

    # Loop through each number to calculate total and product
    for num in numbers:
        total += num
        product *= num

    # Calculate average
    average = total / len(numbers)

    # Display results
    print("Total:", total)
    print("Product:", product)
    print("Average:", average)


# Test the function
numbers = [1, 2, 3, 4, 5]
perform_operations(numbers)
