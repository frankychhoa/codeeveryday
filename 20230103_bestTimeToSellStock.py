class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximum=-float('inf')
        buy,sell=0,1
        l,r=0,1
        while sell < len(prices):
            if prices[sell]-prices[buy] > maximum:
                maximum = prices[sell]-prices[buy]
            if prices[sell] <= prices[buy]:
                buy = sell
                sell += 1
            else:
                sell += 1
        if maximum < 0:
            return 0
        return maximum