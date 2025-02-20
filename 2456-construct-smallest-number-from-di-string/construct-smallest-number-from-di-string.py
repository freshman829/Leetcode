class Solution(object):
    def smallestNumber(self, pattern):
        """
        :type pattern: str
        :rtype: str
        """
        result = []
        for i in range(len(pattern) + 1):
            if not (i == len(pattern) or pattern[i] == 'I'):
                continue
            for x in reversed(range(len(result) + 1, (i + 1) + 1)):
                result.append(x)
        return "".join(map(str, result))


            
            