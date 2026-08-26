"""DAA Practical 6: Matrix Chain Multiplication using Dynamic Programming.

Example:
    Matrix dimensions = [10, 30, 5, 60]
    Matrices = A1(10 x 30), A2(30 x 5), A3(5 x 60)
    Minimum scalar multiplications = 4500
    Optimal order = ((A1 x A2) x A3)
"""

import time


def matrix_chain_order(dimensions):
    """Return the minimum multiplication cost and the optimal order."""
    matrix_count = len(dimensions) - 1
    costs = [[0] * matrix_count for _ in range(matrix_count)]
    order = [[""] * matrix_count for _ in range(matrix_count)]

    for index in range(matrix_count):
        order[index][index] = f"A{index + 1}"

    for chain_length in range(2, matrix_count + 1):
        for start in range(matrix_count - chain_length + 1):
            end = start + chain_length - 1
            costs[start][end] = float("inf")

            for split in range(start, end):
                multiplication_cost = (
                    costs[start][split]
                    + costs[split + 1][end]
                    + dimensions[start] * dimensions[split + 1] * dimensions[end + 1]
                )
                if multiplication_cost < costs[start][end]:
                    costs[start][end] = multiplication_cost
                    order[start][end] = (
                        f"({order[start][split]} x {order[split + 1][end]})"
                    )

    return costs[0][matrix_count - 1], order[0][matrix_count - 1]


def main():
    print("=" * 50)
    print("DAA Practical 6: Matrix Chain Multiplication")
    print("=" * 50)

    try:
        dimensions = list(
            map(int, input("Enter matrix dimensions separated by spaces: ").split())
        )

        if len(dimensions) < 2 or any(dimension <= 0 for dimension in dimensions):
            print("Invalid input! Enter at least two positive dimensions.")
            return

        start_time = time.perf_counter()
        minimum_cost, optimal_order = matrix_chain_order(dimensions)
        execution_time = time.perf_counter() - start_time

        matrix_count = len(dimensions) - 1
        print(f"\nMatrix dimensions: {dimensions}")
        print(f"Number of matrices: {matrix_count}")
        print(f"Optimal multiplication order: {optimal_order}")
        print(f"Minimum scalar multiplications: {minimum_cost}")
        print(f"Execution time: {execution_time:.9f} seconds")
        print("-" * 50)
        print("Time complexity: O(N^3)")
        print("Space complexity: O(N^2)")
        print("N = number of matrices")
    except ValueError:
        print("Invalid input! Please enter positive integers only.")


if __name__ == "__main__":
    main()