class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        taskCount = Counter(tasks)
        maxFreq = max(taskCount.values())
        maxCount = sum(1 for count in taskCount.values() if count == maxFreq)
        slotsNeeded = (maxFreq - 1) * (n + 1) + maxCount
        return max(slotsNeeded, len(tasks))