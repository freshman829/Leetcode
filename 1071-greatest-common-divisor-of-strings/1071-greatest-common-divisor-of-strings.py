class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        short_len = min(len(str1), len(str2))
        res = ""

        for i in range(short_len + 1):
            if i == 0:
                continue
            sl = slice(0, i)
            prefix = str1[sl]
            if self.isDivided(str1, prefix) and self.isDivided(str2, prefix) and len(res) < len(prefix):
                res = prefix
        return res
    
    
    def isDivided(self, string: str, prefix: str) -> bool:
        if len(string) % len(prefix) != 0:
            return False
        else:
            multi = len(string) // len(prefix)
            if prefix * multi == string:
                return True
            else:
                return False