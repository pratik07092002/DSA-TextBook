from typing import List


def nextPermutation( nums: List[int]) -> None:
    n = len(nums)
    
    # Finding pivot
    pivot = -1
    for i in range(n - 2, -1, -1):
        if nums[i] < nums[i + 1]:
            pivot = i
            break

    # If no pivot found then reverse whole array
    if pivot == -1:
        nums.reverse()
        return

    # if pivot found Find the smallest number > nums[pivot] from right
    for j in range(n - 1, pivot, -1):
        if nums[j] > nums[pivot]:
                # Swap these 2 numbers
            nums[j], nums[pivot] = nums[pivot], nums[j]
            break

        # Reverse everything after pivot
    nums[pivot + 1:] = reversed(nums[pivot + 1:])

