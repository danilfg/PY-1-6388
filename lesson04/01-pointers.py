# pointer variables
nums = [4, 8, 15, 16]
nums_pointer = nums
# nums_copy = nums.copy()
nums_copy = nums[:]

# pointers in the loops (list items removing)
for x in nums:
    if x % 2 == 0:
        nums.remove(x)

# print(nums)

# write out of function
test = [1, 2, 4]


def modify_list(list_obj):
    for index, x in enumerate(list_obj):
        list_obj[index] = x ** 2


modify_list(test)

print(test)
