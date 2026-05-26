class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        sortedPoints = sorted(points, key=self.distance)

        return sortedPoints[:k]
        
    def distance(self, coord: List[int]):
        sum = 0 
        for i in coord:
            sum += i ** 2
        return sum ** 0.5

        