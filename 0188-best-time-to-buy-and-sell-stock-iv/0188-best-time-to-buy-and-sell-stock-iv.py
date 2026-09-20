class Solution:

  def maxProfit(self, k: int, prices: list[int]) -> int:
    if not prices or k == 0:
      return 0

    n = len(prices)

    # If k is very large, it's equivalent to unlimited transactions
    if k >= n // 2:
      return sum(
          max(prices[i + 1] - prices[i], 0) for i in range(n - 1)
      )

    # DP array: buy[j] and sell[j] for j-th transaction
    buy = [-prices[0]] * (k + 1)
    sell = [0] * (k + 1)

    for price in prices:
      for j in range(1, k + 1):
        buy[j] = max(buy[j], sell[j - 1] - price)
        sell[j] = max(sell[j], buy[j] + price)

    return sell[k]