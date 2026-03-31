class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []

        for (x,y) in points:
            distance = -(x*x+y*y)
            if len(maxHeap) < k:
                heapq.heappush(maxHeap,(distance,x,y))
            else:
                heapq.heappushpop(maxHeap,(distance,x,y))
        return [[x,y] for (distance,x,y) in maxHeap]