from collections import defaultdict
from typing import Dict, List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        1. if only one element found then return as desiered 
        2. create a hashmap
        3. insert sorted same values into the hashmap
        4. return the values in list
        """
        # step 1
        if len(strs) == 0:
            return list(strs)

        # step 2
        datas: Dict[str, List[str]] = {}
        for i, s in enumerate(strs):
            if "".join(sorted(s)) not in datas:
                datas["".join(sorted(s))] = [s]
            else:
                datas["".join(sorted(s))].append(s)
        return list(datas.values())
