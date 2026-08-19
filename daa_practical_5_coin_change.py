import time


def minimum_coin_change(coins, amount):
    """Return the minimum number of coins and one optimal coin combination."""
    infinity = amount + 1
    minimum_coins = [infinity] * (amount + 1)
    last_coin = [-1] * (amount + 1)
    minimum_coins[0] = 0

    for current_amount in range(1, amount + 1):
        for coin in coins:
            if coin <= current_amount:
                candidate = minimum_coins[current_amount - coin] + 1
                if candidate < minimum_coins[current_amount]:
                    minimum_coins[current_amount] = candidate
                    last_coin[current_amount] = coin

    if minimum_coins[amount] == infinity:
        return None, []

    combination = []
    current_amount = amount
    while current_amount > 0:
        coin = last_coin[current_amount]
        combination.append(coin)
        current_amount -= coin

    return minimum_coins[amount], combination


def main():
    print("=" * 50)
    print("DAA Practical 5: Coin Change Using Dynamic Programming")
    print("=" * 50)

    try:
        coin_input = input("Enter coin denominations separated by spaces: ")
        coins = sorted(set(map(int, coin_input.split())), reverse=True)
        amount = int(input("Enter the amount to make: "))

        if not coins or any(coin <= 0 for coin in coins):
            print("Invalid input! Coins must be positive integers.")
            return
        if amount < 0:
            print("Invalid input! The amount cannot be negative.")
            return

        start_time = time.perf_counter()
        coin_count, combination = minimum_coin_change(coins, amount)
        execution_time = time.perf_counter() - start_time

        print(f"\nCoin denominations: {coins}")
        print(f"Target amount: {amount}")
        if coin_count is None:
            print("No combination of the given coins can make the amount.")
        else:
            print(f"Minimum number of coins: {coin_count}")
            print(f"Selected coins: {combination}")
        print(f"Execution time: {execution_time:.9f} seconds")
        print("-" * 50)
        print("Time complexity: O(A * C)")
        print("Space complexity: O(A)")
        print("A = target amount, C = number of coin denominations")
    except ValueError:
        print("Invalid input! Please enter integers only.")


if __name__ == "__main__":
    main()