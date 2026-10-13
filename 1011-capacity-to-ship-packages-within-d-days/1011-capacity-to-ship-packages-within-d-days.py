class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        i,j = max(weights), sum(weights)
        res = float("inf")
        def ships(cap):
            ship = 1
            curr = cap
            for x in weights:
                if curr - x < 0:
                    ship +=1
                    if ship > days:
                        return False
                    curr = cap
                curr -= x
            return True

        while (i<=j):
            mid = i + (j-i)//2
            if ships(mid):
                j = mid -1 
            else:
                i = mid + 1
        return i


        