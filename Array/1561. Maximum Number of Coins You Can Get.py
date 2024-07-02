class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles = sorted(piles)
        myPile = []
        i = len(piles) - 2
        while len(myPile) != len(piles) // 3:
            myPile.append(piles[i])
            i -= 2
        return sum(myPile)

