import math
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        final_result = []
        for i, n in enumerate(nums):
            final_result.append(math.prod(nums[:i]) * math.prod(nums[i+1:]))

        return final_result

s = Solution()
print(s.productExceptSelf([1,2,4,6]))