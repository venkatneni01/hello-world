def get_largest_numbers(numbers, n):
    print("Before sorting:", numbers)
    numbers.sort()  # [4,1,7,3] becomes [1,3,4,7]
    print("After sorting:", numbers)
    result = numbers[-n:]  # if n=2, gets last 2 numbers [4,7]
    print(f"Getting last {n} elements:", result)
    return result

# Example with detailed steps
nums = [4, 1, 7, 3]
largest = get_largest_numbers(nums, 2)
print("Final result:", largest)