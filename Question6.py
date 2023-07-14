def findMin(nums):
    left, right = 0, len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2

        # Check if mid element is greater than the last element
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

    return nums[left]

# Test case
nums = [4, 5, 6, 7, 0, 1, 2]
print(findMin(nums))  # Output: 0
