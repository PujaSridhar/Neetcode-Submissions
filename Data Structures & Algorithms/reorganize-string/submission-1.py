class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = Counter(s)
        heap = [(-count,char) for char, count in freq.items()]
        heapq.heapify(heap)
        prevCount, prevChar = 0, ""
        result = []

        while heap:
            count, char = heapq.heappop(heap)
            result.append(char)
            count += 1
            if prevCount < 0:
                heapq.heappush(heap, (prevCount, prevChar))
            prevCount, prevChar = count, char

        return ''.join(result) if len(result) == len(s) else ""