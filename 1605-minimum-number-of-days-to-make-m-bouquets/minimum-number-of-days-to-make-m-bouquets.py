class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n=len(bloomDay)
        if m*k>n:
            return -1
        left=min(bloomDay)
        right=max(bloomDay)
        while left<right:
            mid=(left+right)//2
            flowers=0
            boquets=0
            for day in bloomDay:
                if day<=mid:
                    flowers+=1
                    if flowers==k:
                        boquets+=1
                        flowers=0
                else:
                        flowers=0
            if boquets>=m:
                right=mid
            else:
                left=mid+1
        return left



        