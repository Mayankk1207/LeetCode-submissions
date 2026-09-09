class Solution(object):
    def findWinners(self, matches):
        losses = {}

        for winner, loser in matches:
            losses[loser] = losses.get(loser, 0) + 1

        w0 = []
        w1 = []

        for winner, loser in matches:
            if winner not in losses:
                w0.append(winner)

            if losses.get(loser) == 1:
                w1.append(loser)

        return [sorted(set(w0)), sorted(set(w1))]
