def missing_number(nums):
  """
  Returns the only number in the range [0, n] that is missing from the array.

  Args:
    nums: An array of distinct numbers in the range [0, n].

  Returns:
    The only number in the range [0, n] that is missing from the array.
  """

  n = len(nums)
  expected_sum = n * (n + 1) // 2
  actual_sum = sum(nums)
  return expected_sum - actual_sum


if __name__ == "__main__":
  nums = [3, 0, 1]
  print(missing_number(nums))