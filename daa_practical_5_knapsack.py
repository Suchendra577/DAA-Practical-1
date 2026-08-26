def knapsack_dp(weights, values, capacity):
    """
    Solves the 0/1 Knapsack problem using dynamic programming.

    Args:
        weights (list): A list of weights of the items.
        values (list): A list of values of the items.
        capacity (int): The maximum capacity of the knapsack.

    Returns:
        int: The maximum value that can be obtained.
    """
    n = len(values)
    
    # dp[i][w] will store the maximum value that can be obtained
    # with first i items and capacity w.
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Build dp table in bottom-up manner
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            # If current item's weight is more than current capacity w,
            # then it cannot be included.
            if weights[i-1] > w:
                dp[i][w] = dp[i-1][w]
            else:
                # Else, either include current item or not.
                # Compare value if included with value if not included.
                dp[i][w] = max(values[i-1] + dp[i-1][w - weights[i-1]], dp[i-1][w])

    return dp[n][capacity]

# Example items
weights = [10, 20, 30, 40, 50]
values = [60, 100, 120, 140, 180]
capacity = 70

max_value = knapsack_dp(weights, values, capacity)
print(f"Items: {list(zip(weights, values))}")
print(f"Knapsack Capacity: {capacity}")
print(f"Maximum value in knapsack: {max_value}")
