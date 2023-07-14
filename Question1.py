def mySqrt(x):
    if x == 0:
        return 0

    left, right = 1, x
    result = 0
    while left <= right:
        mid = left + (right - left) // 2
        if mid <= x // mid:
            result = mid
            left = mid + 1
        else:
            right = mid - 1

    return result

# Test case
print(mySqrt(4))  # Output: 2
