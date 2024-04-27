from typing import List
from domain.stock_price import StockPrice
from domain.transaction import Transaction


class StockAnalyzer:
    @staticmethod
    def max_profit(stock_prices: StockPrice, transactions: int) -> List[Transaction]:
        if not stock_prices.prices or transactions == 0:
            return []

        profits = []

        def max_profit_helper(prices, n, k):
            dp = [[0] * (k + 1) for _ in range(n)]

            for i in range(1, n):
                for j in range(1, k + 1):
                    max_profit_so_far = 0
                    for l in range(i):
                        max_profit_so_far = max(
                            max_profit_so_far, prices[i] - prices[l] + dp[l][j - 1])
                    dp[i][j] = max(dp[i - 1][j], max_profit_so_far)

            transactions_done = []
            for j in range(transactions, 0, -1):
                max_profit_for_j_transactions = dp[n - 1][j]
                for i in range(n - 1, 0, -1):
                    if dp[i][j] != dp[i - 1][j]:
                        buy_day = i - 1
                        sell_day = i
                        profit = prices[sell_day] - prices[buy_day]
                        transactions_done.append(
                            Transaction(buy_day, sell_day, profit))
                        j -= 1

            return transactions_done[::-1]

        return max_profit_helper(stock_prices.prices, len(stock_prices.prices), transactions)
