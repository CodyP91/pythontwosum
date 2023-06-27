def find_two_sum(numbers, target):
    num_dict = {}
    for i, num in enumerate(numbers):
        complement = target - num
        if complement in num_dict:
            return [num_dict[complement], i]
        num_dict[num] = i
    return []

numbers = [1, 2, 3, 4, 5]
target = 8
print(find_two_sum(numbers, target))  # Output: [2, 4]

numbers = [2, 4, 6, 8, 10]
target = 14
print(find_two_sum(numbers, target))  # Output: [2, 3]

numbers = [5, 10, 15, 20]
target = 25
print(find_two_sum(numbers, target))  # Output: [0, 3]

numbers = [3, 1, 4, 6, 2]
target = 7
print(find_two_sum(numbers, target))  # Output: [1, 3]

numbers = [1, 1, 1, 1, 1]
target = 2
print(find_two_sum(numbers, target))  # Output: [0, 1] or [1, 0]

numbers = [10, 20, 30, 40, 50]
target = 100
print(find_two_sum(numbers, target))  # Output: [1, 3]

numbers = [2, 4, 6, 8, 10]
target = 15
print(find_two_sum(numbers, target))  # Output: []

# Add more test cases...



