class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = []
        count = 0

        for x in nums:
            count += x
            res.append(count)

        count = 0
        seen = {0: 1}

        for x in res:
            diff = x - k

            if diff in seen:
                count += seen[diff]

            seen[x] = seen.get(x, 0) + 1

        return count

        