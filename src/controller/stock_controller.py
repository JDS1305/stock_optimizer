from typing import List
from domain.stock_price import StockPrice
from domain.transaction import Transaction
from use_case.stock_analyzer import StockAnalyzer


class StockController:
    @staticmethod
    def calculate_max_profit(prices: List[int], transactions: int):
        stock_prices = StockPrice(prices)
        transactions = StockAnalyzer.max_profit(stock_prices, transactions)
        return transactions
