class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for str in strs:
            sort = tuple(sorted(str))
            if sort in hashmap:
                hashmap[sort].append(str)
            else:
                hashmap[sort] = [str]
        return list(hashmap.values())