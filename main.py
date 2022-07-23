# Use an algorithm to determine how many rotations have been done on a
# sorted list to get a desired output

# test cases

# A list of size 8 rotated 5 times
test1 = {
    "input": {
        "num": [4, 5, 6, 7, 8, 1, 2, 3]
    },
    "output": 5
}

# A list that wasn't rotated at all
test2 = {
    "input": {
        "num": [1, 2, 4, 6, 7]
    },
    "output": 0
}

# A list that was rotated just once
test3 = {
    "input": {
        "num": [7, 1, 2, 3, 4, 5, 6]
    },
    "output": 1
}

# A list that was rotated n times, where n is the size of the list
test4 = {
    "input": {
        "num": [1, 2, 3, 4, 5, 6, 7]
    },
    "output": 0
}

# A list containing one element
test5 = {
    "input": {
        "num": [7]
    },
    "output": 0
}

# A list where numbers are repeated
test6 = {
    "input": {
        "num": [5, 6, 6, 9, 9, 9, 0, 0, 2, 3, 3, 3, 3, 4, 4, 4, 5]
    },
    "output": 6
}
test_list = [test1, test2, test3, test4, test5, test6]


def count_rotations_linear(nums):
    position = 1

    while position < len(nums):
        if position > 0 and nums[position] < nums[position - 1]:
            return position

        position += 1

    return 0

# for test in test_list:
#     if test["output"] == count_rotations_linear(nums=test["input"]["num"]):
#         print(f"{test} result: Passed")
#
#     else:
#         print(f"{test} Result: Failed")


def count_rotations_binary(nums, query):
    lo = 0
    hi = len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if mid > 0 and nums[mid] < nums[mid - 1]:
            return mid

        elif nums[mid] > nums[hi]:
            lo = mid + 1

        elif nums[mid] < nums[hi]:
            hi = mid - 1

        elif mid == 0:
            return 0

    return 0

for test in test_list:
    if test["output"] == count_rotations_binary(nums=test["input"]["num"]):
        print(f"{test} result: Passed")

    else:
        print(f"{test} Result: Failed")
