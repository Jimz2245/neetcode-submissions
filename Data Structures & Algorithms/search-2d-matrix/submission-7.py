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
    











































                        
        