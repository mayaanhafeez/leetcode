class Solution(object):
    def removeDuplicates(self, nums):
        i = 0
        j = i
        while j < len(nums)-1:
            if nums[j] != nums[j+1]:
                j+=1
                i+=1
                nums[i]= nums[j]
            else:
                j+=1
            print(nums)
        return i+1

sol = Solution()
nums = [0,0,1,1,1,2,2,3,3,4]
print(sol.removeDuplicates(nums))
nums = [1,1,2]
print(sol.removeDuplicates(nums))

