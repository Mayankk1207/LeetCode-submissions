class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        seen = {}

        for x, y in enumerate(heights):
            seen[y] = names[x]

        sorts = sorted(seen, reverse=True)
        return [seen[x] for x in sorts]