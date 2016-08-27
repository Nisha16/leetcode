class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        m = 0
        i = 1
        while i <= n:
            d = n%(i*10)/i;
            res += d*m + (d == 1)*(n%i + 1) + (d>1)*i
            m = m*10 +i
            i = i*10
        return res 