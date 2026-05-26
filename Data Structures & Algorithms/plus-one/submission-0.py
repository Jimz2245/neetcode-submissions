class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits)):
            if carry:
                temp = digits[len(digits) - i - 1] + carry
                digits[len(digits) - i - 1] = temp % 10
                carry = temp // 10
            else:
                continue
        if carry == 1:
            digits.insert(0, 1)
        return digits
        