class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if row[len(row)-1] >= target:
                l = 0
                r = len(row) - 1
                while l <= r:
                    m = int((l + r)/2)
                    if row[m] == target:
                        return True
                    elif row[m] > target:
                        r = m - 1
                    else:
                        l = m + 1
        return False
    











































        for row in range(len(matrix)):
            if target <= matrix[row][len(matrix[row]) - 1]:
                low = 0
                high = len(matrix[row]) - 1
                while low <= high:
                    mid = (high + low) // 2
                    if target == matrix[row][mid]:
                        return True
                    elif matrix[row][mid] > target:
                        high = mid - 1
                    else:
                        low = mid + 1
                return False
        return False
                        
        