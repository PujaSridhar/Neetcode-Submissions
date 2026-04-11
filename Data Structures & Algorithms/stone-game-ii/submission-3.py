class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        memo = {}
        suffixSum = [0] * (n+1)
        for i in range(n-1,-1,-1):
            suffixSum[i] = suffixSum[i+1] + piles[i]

        def solve(i,m):
            if i >= n:
                return 0
            if (i,m) in memo:
                return memo[(i,m)]
            if i + 2 * m >= n:
                return suffixSum[i]
            res = 0
            for x in range(1,2*m+1):
                res = max(res, suffixSum[i] - solve(i + x, max(m,x)))
            memo[(i,m)] = res
            return res
        return solve(0,1)
