import unittest
from ..src.use_case.stock_analyzer import StockAnalyzer
from ..src.domain.stock_price import StockPrice
from ..src.domain.transaction import Transaction


class TestStockAnalyzer(unittest.TestCase):
    def test_max_profit_simple(self):
        prices = [1, 2, 3, 4, 5]
        stock_prices = StockPrice(prices)
        transactions = 1
        expected_transactions = [Transaction(buy_day=0, sell_day=4, profit=4)]
        actual_transactions = StockAnalyzer.max_profit(
            stock_prices, transactions)
        self.assertEqual(actual_transactions, expected_transactions)

    def test_max_profit_multiple_transactions(self):
        prices = [7, 1, 5, 3, 6, 4]
        stock_prices = StockPrice(prices)
        transactions = 2
        expected_transactions = [
            Transaction(buy_day=1, sell_day=2, profit=4),
            Transaction(buy_day=3, sell_day=4, profit=3)
        ]
        actual_transactions = StockAnalyzer.max_profit(
            stock_prices, transactions)
        self.assertEqual(actual_transactions, expected_transactions)

    def test_max_profit_no_transactions(self):
        prices = [7, 6, 4, 3, 1]
        stock_prices = StockPrice(prices)
        transactions = 2
        expected_transactions = []
        actual_transactions = StockAnalyzer.max_profit(
            stock_prices, transactions)
        self.assertEqual(actual_transactions, expected_transactions)

    def test_max_profit_empty_prices(self):
        prices = []
        stock_prices = StockPrice(prices)
        transactions = 2
        expected_transactions = []
        actual_transactions = StockAnalyzer.max_profit(
            stock_prices, transactions)
        self.assertEqual(actual_transactions, expected_transactions)

    def test_max_profit_zero_transactions(self):
        prices = [7, 1, 5, 3, 6, 4]
        stock_prices = StockPrice(prices)
        transactions = 0
        expected_transactions = []
        actual_transactions = StockAnalyzer.max_profit(
            stock_prices, transactions)
        self.assertEqual(actual_transactions, expected_transactions)

    def test_max_profit_single_price(self):
        prices = [7]
        stock_prices = StockPrice(prices)
        transactions = 1
        expected_transactions = []
        actual_transactions = StockAnalyzer.max_profit(
            stock_prices, transactions)
        self.assertEqual(actual_transactions, expected_transactions)

    def test_max_profit_single_transaction(self):
        prices = [7, 6, 5, 4, 3, 2, 1]
        stock_prices = StockPrice(prices)
        transactions = 1
        expected_transactions = [Transaction(buy_day=0, sell_day=0, profit=0)]
        actual_transactions = StockAnalyzer.max_profit(
            stock_prices, transactions)
        self.assertEqual(actual_transactions, expected_transactions)

    def test_max_profit_large_prices(self):
        prices = [i for i in range(1, 1001)]
        stock_prices = StockPrice(prices)
        transactions = 2
        expected_transactions = [Transaction(
            buy_day=0, sell_day=999, profit=999)]
        actual_transactions = StockAnalyzer.max_profit(
            stock_prices, transactions)
        self.assertEqual(actual_transactions, expected_transactions)


if __name__ == '__main__':
    unittest.main()
