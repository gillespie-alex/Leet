class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # three possible states that the the investor can be in: buy, sell, cool (nothing/holding)
        # Once the investor buys he can only continue in two states: sell or cool
        # After selling, the investor must enter the cool state
        cache = {}
        global BUY; global SELL;
        BUY = -1
        SELL = 1
        # 'state' will represent the current state ie. if "BUY" we are looking to buy
        def dfs(i, state):
            if i >= len(prices):
                return 0
            profit = 0
            global BUY; global SELL;
            
            if (i,state) in cache:
                return cache[(i,state)]
            
            if state == BUY:
                profit = max(dfs(i + 1, state), dfs(i + 1, SELL) - prices[i])
                
            elif state == SELL:
                profit = max(dfs(i + 1, state), dfs(i + 2, BUY) + prices[i]) 
                
            cache[(i,state)] = profit
            return profit
        
        
        
        return dfs(0, BUY)

        