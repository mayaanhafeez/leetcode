class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        l = len(needle)
        for i in range(0,len(haystack)-len(needle)+1):
            print(len(haystack))
            print(len(needle))

            if needle == haystack[i:i+l]:
                return i
            else:
                continue
        return -1

sol = Solution()
print(sol.strStr("sadbutsad", "sad"))
