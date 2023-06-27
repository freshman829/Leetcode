import math
class Solution:
    def reverse(self, x: int) -> int:
        flag = True
        if x < 0:
            flag = False
        strX = str(abs(x))
        reverse = strX[::-1]
        rev = int(reverse)
        if not flag:
            rev = 0 - rev
        if rev < -2**31 or rev > 2**31 - 1:
            return 0
        return rev
        
            
        
        
        