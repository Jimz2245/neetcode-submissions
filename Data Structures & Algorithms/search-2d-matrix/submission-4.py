class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in range(len(matrix)):
            if target <= matrix[row][len(matrix[row]) - 1]:
                low = -1
                high = len(matrix[row])
                mid = int(high / 2)
                while low < mid and high > mid:
                    if target == matrix[row][mid]:
                        return True
                    elif matrix[row][mid] > target:
                        high = mid
                        mid = int((high+low) / 2)
                    else:
                        low = mid
                        mid = int((low+high) / 2)
                return False
        return False
                        
        