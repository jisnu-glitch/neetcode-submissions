class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)
        for i in strs:
            count = [0] * 26
            for x in i:
                count[ord(x)-ord('a')] += 1
            res[tuple(count)].append(i)
        return list(res.values())
