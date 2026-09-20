class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        below_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", 
                    "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        thousands = ["", "Thousand", "Million", "Billion"]

        def helper(n):
            if n == 0:
                return ""
            elif n < 20:
                return below_20[n] + " "
            elif n < 100:
                return tens[n // 10] + (" " + below_20[n % 10] if n % 10 != 0 else "") + " "
            else:
                return below_20[n // 100] + " Hundred " + helper(n % 100)

        res = ""
        for i in range(len(thousands) - 1, -1, -1):
            if num >= 1000**i:
                res += helper(num // 1000**i) + thousands[i] + " "
                num %= 1000**i

        return res.strip()