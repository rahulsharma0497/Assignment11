from collections import Counter


def intersect(nums1, nums2):
    counter1 = Counter(nums1)
    counter2 = Counter(nums2)

    intersection = []

    # Iterate over the elements in nums1
    for num in counter1:
        # Check if the element is present in nums2
        if num in counter2:
            # Add the minimum count to the intersection list
            intersection.extend([num] * min(counter1[num], counter2[num]))

    return intersection


# Test case
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print(intersect(nums1, nums2))  # Output: [2, 2]
