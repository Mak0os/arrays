# Program Name: Lab8.py
# Course: IT1114/Section XXX
# Student Name: Daniel Urdaneta
# Assignment Number: Lab8
# Due Date: 11/3/2024
# Purpose: This program combines two randomly generated integer arrays into one larger array with distinct values.
# It prompts the user for the number of elements in each array, then combines and sorts the unique values without using array.sort().
# Resources: N/A

import random

def get_random_array(n, range_min=0, range_max=500):
    """Generate an array of n random integers between range_min and range_max."""
    return [random.randint(range_min, range_max) for _ in range(n)]

def remove_duplicates_and_combine(arr1, arr2):
    """Combine two arrays into one with unique elements only."""
    combined_set = set(arr1) | set(arr2)  # Union of two sets removes duplicates
    return list(combined_set)

def bubble_sort(arr):
    """Sort an array using bubble sort (as an alternative to array.sort())."""
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def main():
    # Prompt user for input
    N = int(input("Enter a positive integer N (greater than 1): "))
    if N <= 1:
        print("Please enter a value greater than 1.")
        return

    # Create two arrays with N random integers between 0 and 500
    array1 = get_random_array(N)
    array2 = get_random_array(N)

    # Combine arrays and remove duplicates
    combined_array = remove_duplicates_and_combine(array1, array2)

    # Sort the array without using array.sort()
    sorted_array = bubble_sort(combined_array)

    # Display the contents of the sorted final array, one number per line
    print("The contents of the final array:")
    for num in sorted_array:
        print(num)

# Run the main function if this file is executed
if __name__ == "__main__":
    main()
