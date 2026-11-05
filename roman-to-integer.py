class Solution(object):
    def romanToInt(self, s):
        map = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000,
        }
        if len(s) == 1:
            return map[s]

        num = 0
        num += map[s[0]]
        for i in range(len(s)-1, 0, -1):
            if map[s[i]] > map[s[i-1]]:
                num +=  map[s[i-1]]
            else:
                num -=  map[s[i-1]]

        return num


def main():
    sol = Solution()
    print("solution")
    print(sol.romanToInt("V"))
    print("solution")
    print(sol.romanToInt("LVIII"))
    print("solution")
    print(sol.romanToInt("MCMXCIV"))

main()

