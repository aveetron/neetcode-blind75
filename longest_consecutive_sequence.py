from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in nums:
            length = 0
            # define the entry point
            if (n-1) not in numSet:
                while (n+length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest 
     
s = Solution()
print(s.longestConsecutive([9,1,4,7,3,-1,0,5,8,-1,6]))


a = [77,0,8,21,45,2,3,-2,-4]
print(sorted(a))
print(set(a))