class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        for i in range(len(prices)):
            curItem = prices[i]
            discount = 0
            for j in range(i + 1, len(prices)):
                if (prices[j] <= curItem):
                    discount = prices[j]
                    break
            prices[i] = curItem - discount
        return prices
