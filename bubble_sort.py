import random

# A list of numbers in random order
test0 = {
    'input': {
     'num': [4, 2, 6, 3, 4, 6, 2, 1]
     },
    'output': [1, 2, 2, 3, 4, 4, 6, 6]
}
# A list that's already sorted
test1 = {
    'input': {
     'num': [1, 2, 2, 3, 4, 4, 6, 6]
     },
    'output': [1, 2, 2, 3, 4, 4, 6, 6]
}
# a list that's sorted in descending order
test2 = {
    'input': {
     'num': [6, 6, 4, 4, 3, 2, 2, 1]
     },
    'output': [1, 2, 2, 3, 4, 4, 6, 6]
}
# A list containing repeated elements
test3 = {
    'input': {
     'num': [4, 2, 6, 3, 4, 6, 2, 1]
     },
    'output': [1, 2, 2, 3, 4, 4, 6, 6]
}
# An empty list
test4 = {
    'input': {
     'num': []
     },
    'output': []
}
# A list containing just one element
test5 = {
    'input': {
     'num': [4]
     },
    'output': [4]
}
# A list containing one element repeated many times
test6 = {
    'input': {
     'num': [4, 4, 4, 4, 4, 4, 4, 4]
     },
    'output': [4, 4, 4, 4, 4, 4, 4, 4]
}
# A really long list
in_list = list(range(10000))
out_list = list(range(10000))
random.shuffle(in_list)

test7 = {
    'input': {
     'num': in_list
     },
    'output': out_list
}

test_list = [test0, test1, test2, test3, test4, test5, test6, test7]


def bubble_sort(nums):
    nums = list(nums)

    if nums is []:
        return nums

    for _ in range(len(nums) - 1):
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]

    return nums

for test in test_list:
    if test['output'] == bubble_sort(test['input']['num']):
        print("Test result passed")
    else:
        print("Test result failed")
