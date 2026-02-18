#123. Best Time to Buy and Sell Stock III

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Time = O(2n)
        #Space = O(n)
        if not prices: return 0

        dp = [0 for _ in range(len(prices))]

        for t in range(1,2+1):
            pos = -prices[0]
            profit = 0
