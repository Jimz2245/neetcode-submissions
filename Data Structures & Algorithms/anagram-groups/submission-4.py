class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for str in strs:
            newStr = ''.join(sorted(str))
            res[newStr].append(str)
        return list(res.values())