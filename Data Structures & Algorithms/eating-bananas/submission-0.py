class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        right= max(piles)
        res=right
        while low<= right:
            mid= (low + right ) // 2

            time=0
            for p in piles:
                time+=  math.ceil(float(p)/mid )
            
            if time <= h:
                res= mid
                right = mid -1
            else:
                low = mid+1
        return res