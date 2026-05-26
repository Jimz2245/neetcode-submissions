class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        vals = {}
        for idx in range(len(numbers)):
            diff = target - numbers[idx]
            if diff in vals:
                return [vals[diff] + 1, idx + 1]
            else:
                vals[numbers[idx]] = idx
        return [0,0]
        