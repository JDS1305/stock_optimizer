from controller.stock_controller import StockController


def main():
    prices = [3, 5, 0, 9, 4, 8, 7, 2, 1, 6]
    transactions = 3

    transactions_result = StockController.calculate_max_profit(
        prices, transactions)

    print("Maximum profit can be achieved through the following transactions:")
    for transaction in transactions_result:
        print(
            f"Buy on day {transaction.buy_day}, sell on day {transaction.sell_day}, profit: {transaction.profit}")


if __name__ == "__main__":
    main()
