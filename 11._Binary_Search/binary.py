def binary_search(array, target):
    left, right = 0, len(array) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        # Check if target is present at mid
        if array[mid] == target:
            return mid
        # If target is greater, ignore the left half
        elif array[mid] < target:
            left = mid + 1
        # If target is smaller, ignore the right half
        else:
            right = mid - 1
    
    # If the target is not present in array
    return -1

# Get a sorted list of numbers from the user
user_input = input("Enter a sorted list of numbers separated by space: ")
array = list(map(int, user_input.split()))

# Get the target number to search for from the user
target = int(input("Enter the target number to search for: "))

# Perform binary search
result = binary_search(array, target)

# Print the result
if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found in array")
