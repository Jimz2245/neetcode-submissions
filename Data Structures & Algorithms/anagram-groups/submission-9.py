class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for s in strs:
            sort = "".join(sorted(s))
            res.setdefault(sort, []).append(s)
        return list(res.values())

        