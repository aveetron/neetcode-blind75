from typing import Dict, List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
      """
      Input: nums = [1,2,2,3,3,3], k = 2
      Output: [2,3]
      """
      datas: Dict[str, int] = {}
      for num in nums:
        if str(num) not in datas:
          datas[str(num)] = 1
        else:
          datas[str(num)] = datas[str(num)] + 1

      # sort datas
      datas = dict(sorted(datas.items(), key=lambda x: x[1], reverse=True))
      return [int(n) for n in sorted(list(datas.keys())[:k])]
      
s = Solution()
print(s.topKFrequent([1,2,2,3,3,3], 2))