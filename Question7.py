def searchRange(nums, target):
    left = findLeftIndex(nums, target)
    right = findRightIndex(nums, target)
    return [left, right]

def findLeftIndex(nums, target):
    left, right = 0, len(nums) - 1
    index = -1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] >= target:
            right = mid - 1
        else:
            left = mid + 1

        if nums[mid] == target:
            index = mid

    return index

def findRightIndex(nums, target):
    left, right = 0, len(nums) - 1
    index = -1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] <= target:
            left = mid + 1
        else:
            right = mid - 1

        if nums[mid] == target:
            index = mid

    return index

# Test case
nums = [5, 7, 7, 8, 8, 10]
target = 8
print(searchRange(nums, target))  # Output: [3, 4]
