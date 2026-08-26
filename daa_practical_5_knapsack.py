"""DAA Practical 5: 0/1 Knapsack using Dynamic Programming.

Example:
    Weights = [2, 3, 4, 5]
    Values = [3, 4, 5, 6]
    Capacity = 5
    Maximum value = 7 (items with weights 2 and 3)
"""

import time


def knapsack(weights, values, capacity):
    """Return the maximum value and selected item indexes."""
    item_count = len(weights)
    table = [[0] * (capacity + 1) for _ in range(item_count + 1)]

    for item in range(1, item_count + 1):
        weight = weights[item - 1]
        value = values[item - 1]
        for current_capacity in range(capacity + 1):
            table[item][current_capacity] = table[item - 1][current_capacity]
            if weight <= current_capacity:
                table[item][current_capacity] = max(
                    table[item][current_capacity],
                    value + table[item - 1][current_capacity - weight],
                )

    selected_items = []
    current_capacity = capacity
    for item in range(item_count, 0, -1):
        if table[item][current_capacity] != table[item - 1][current_capacity]:
            selected_items.append(item - 1)
            current_capacity -= weights[item - 1]

    selected_items.reverse()
    return table[item_count][capacity], selected_items


def main():
    print("=" * 50)
    print("DAA Practical 5: 0/1 Knapsack Using Dynamic Programming")
    print("=" * 50)

    try:
        weights = list(map(int, input("Enter item weights separated by spaces: ").split()))
        values = list(map(int, input("Enter item values separated by spaces: ").split()))
        capacity = int(input("Enter knapsack capacity: "))

        if not weights or len(weights) != len(values):
            print("Invalid input! Weights and values must contain the same number of items.")
            return
        if any(weight <= 0 for weight in weights) or any(value < 0 for value in values):
            print("Invalid input! Weights must be positive and values cannot be negative.")
            return
        if capacity < 0:
            print("Invalid input! Capacity cannot be negative.")
            return

        start_time = time.perf_counter()
        maximum_value, selected_items = knapsack(weights, values, capacity)
        execution_time = time.perf_counter() - start_time

        selected_weight = sum(weights[index] for index in selected_items)
        selected_value = sum(values[index] for index in selected_items)

        print(f"\nWeights: {weights}")
        print(f"Values: {values}")
        print(f"Capacity: {capacity}")
        print(f"Selected item numbers: {[index + 1 for index in selected_items]}")
        print(f"Total selected weight: {selected_weight}")
        print(f"Maximum value: {maximum_value}")
        print(f"Execution time: {execution_time:.9f} seconds")
        print("-" * 50)
        print("Time complexity: O(N * W)")
        print("Space complexity: O(N * W)")
        print("N = number of items, W = knapsack capacity")
        print(f"Result verified: {selected_value == maximum_value}")
    except ValueError:
        print("Invalid input! Please enter integers only.")


if __name__ == "__main__":
    main()