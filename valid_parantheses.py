class Solution(object):

    def get_type(self, c):
        if c in "()":
            return 1
        if c in "{}":
            return 2
        if c in "[]":
            return 3

    def is_open(self,c):
        open = ["(", "{", "["]
        close = [")", "}", "]"]
        if c in open:
            return 1
        else:
            return 0

    def isValid(self, s):
        stack = []
        if len(s) <= 1:
            return False
        for i in range(0, len(s)):
            if self.is_open(s[i]) == 1:
                stack.append(s[i])
            else:
                if len(stack) != 0:
                    char = stack.pop()
                    if self.get_type(s[i])== self.get_type(char):
                        continue
                    else:
                        return False
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False


sol = Solution()

print(sol.isValid("()[]{}"))
