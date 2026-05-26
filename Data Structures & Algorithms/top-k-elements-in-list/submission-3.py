class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count each number's frequency
        # e.g. [1,1,1,2,2,3] → {1:3, 2:2, 3:1}
        count = {}  
        for num in nums:
            count[num] = 1 + count.get(num, 0)  

        # bucket array where index = frequency
        # e.g. freq = [[], [3], [2], [1], [], [], []]
        freq = [[] for i in range(len(nums) + 1)]
        for num, cnt in count.items():
            freq[cnt].append(num)

        # scan highest frequency → lowest, collect until we have k elements
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res