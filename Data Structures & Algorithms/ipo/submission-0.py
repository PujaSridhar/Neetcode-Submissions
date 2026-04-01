class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = sorted(zip(capital,profits))
        ptr = 0
        n = len(projects)
        availableProfits = []
        for _ in range(k):
            while ptr < n and projects[ptr][0] <= w:
                heapq.heappush(availableProfits, -projects[ptr][1])
                ptr += 1

            if not availableProfits:
                break
            w += -heapq.heappop(availableProfits)
        return w