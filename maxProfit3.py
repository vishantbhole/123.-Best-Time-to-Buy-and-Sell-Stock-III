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
            for i in range(1, len(prices)):
                pos = max(pos, dp[i]-prices[i])
                profit = max(profit, pos+prices[i])
                dp[i] = profit
        return profit


if __name__ == "__main__":
    sol = Solution()
    prices = [3,3,5,0,0,3,1,4]
    print("Output is : ", sol.maxProfit(prices))
