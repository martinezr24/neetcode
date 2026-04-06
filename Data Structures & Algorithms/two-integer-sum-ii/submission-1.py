class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while (left < right):
            needed = target - numbers[left]
            if needed > numbers[right]:
                left += 1
            elif needed < numbers[right]:
                right -= 1
            else:
                return [left + 1, right + 1]