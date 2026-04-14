class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ''

        while columnNumber:
            columnNumber -= 1
            result = chr(columnNumber % 26 + 65) + result
            columnNumber //= 26
        
        return result