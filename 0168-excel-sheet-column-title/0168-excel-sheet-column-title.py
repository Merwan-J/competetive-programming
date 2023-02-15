class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""
        while columnNumber:
            remain = columnNumber % 26
            columnNumber //= 26
            if remain != 0:
                result = chr(ord("A") + remain - 1) + result
            # Special case for "Z"
            else:
                result = "Z" + result
                columnNumber -= 1

        return result