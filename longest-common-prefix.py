class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs.sort(key=len)
        base = strs[0]
        flag = True
        lcp = ""
        for i in range(0, len(base)):
            for word in strs:
                if word[i] == base[i]:
                    flag = flag & True
                else:
                    flag = False
                    break

            if flag == True:
                lcp += base[i]
        return lcp

def main():
    sol = Solution()
    print(sol.longestCommonPrefix(["ab", "a"]))

    print(sol.longestCommonPrefix(["flower","flow","flight"]))
main()
