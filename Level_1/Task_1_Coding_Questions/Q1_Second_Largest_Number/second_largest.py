# Task 1 - Find the Second Largest Number

array = [5, 3, 8, 2, 7]

def find_second_largest(arr):

    # Convert list to a set to remove duplicate values
    unique_numbers = list(set(arr))

    # If unique numbers are less than 2, second largest cannot be found
    if len(unique_numbers) < 2:
        return None

    # Initialize variables with negative infinity
    largest = float('-inf')
    second_largest = float('-inf')

    # Find largest and second largest values using loop
    for item in unique_numbers:
        if item > largest:
            second_largest = largest
            largest = item
        elif second_largest < item < largest:
            second_largest = item

    return second_largest

print("Array : ", array)
print("Second Largest Number :", find_second_largest(array))
