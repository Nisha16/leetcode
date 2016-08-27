    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if k >= (n>>1):return self.maxProfit2(prices)
        dp =[[0 for j in xrange(n)]for i in xrange(k+1)]
        
        for i in xrange(1,k+1):
            maxTemp=-prices[0]
            for j in xrange(1,n):
                dp[i][j]=max(dp[i][j-1],prices[j] + maxTemp)
                maxTemp =max(maxTemp,dp[i-1][j-1] - prices[j])
        return dp[k][n-1]
        
    def maxProfit2(self,prices):
        ans = 0
        for i in xrange(1,len(prices)):
            if prices[i]>prices[i-1]:
                ans +=prices[i]-prices[i-1]
        return ans 