class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # Alice can always choose to take all even-indexed piles 
        # or all odd-indexed piles. Since the total sum is odd, 
        # one of those sums is guaranteed to be greater.
        return True