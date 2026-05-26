class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # defaultdict(list) auto-creates an empty list for any new key
        res = defaultdict(list)
        
        for s in strs: 
            # Create a frequency counter with 26 slots — one per letter a-z
            count = [0] * 26
            
            for c in s:
                # ord(c) - ord('a') converts a character to its 0-based index
                count[ord(c) - ord('a')] += 1
            
            # Anagrams always produce the SAME count array
            # Lists can't be dict keys (unhashable), so we convert to a tuple
            res[tuple(count)].append(s)
        
        # Each key groups all strings that share the same letter frequencies
        # .values() gives us the grouped lists; wrap in list() to match return type
        return list(res.values())