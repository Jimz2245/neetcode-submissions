class Solution:

    def encode(self, strs: List[str]) -> str:
        code = ""
        for s in strs:
            code = code + s + "#/#"
        return code

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        strs = s.split("#/#")
        return strs[:-1]
