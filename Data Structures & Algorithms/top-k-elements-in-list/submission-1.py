class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        r={}

        for i in nums:
            r[i] = r.get(i,0) + 1

        d=dict(sorted(r.items(), key=lambda item: item[1], reverse=True))

        return list(d.keys())[:k]
