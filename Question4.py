def find_duplicate_number(nums):
  """
  Returns the repeated number in the array.

  Args:
    nums: An array of integers where each integer is in the range [1, n].

  Returns:
    The repeated number in the array.
  """

  tortoise = 0
  hare = 0
  while True:
    tortoise = nums[tortoise]
    hare = nums[nums[hare]]
    if tortoise == hare:
      break
  tortoise = 0
  while tortoise != hare:
    tortoise = nums[tortoise]
    hare = nums[hare]
  return hare


if __name__ == "__main__":
  nums = [1, 3, 4, 2, 2]
  print(find_duplicate_number(nums))