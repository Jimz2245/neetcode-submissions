class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)):
            temp = len(digits) - 1
            if digits[temp - i] != 9:
                digits[temp - i] += 1
                return digits
            digits[temp - i] = 0
        return [1] + digits
        