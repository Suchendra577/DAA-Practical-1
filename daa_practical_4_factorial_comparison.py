import time


def iterative_factorial(number):
    result = 1
    for value in range(2, number + 1):
        result *= value
    return result


def recursive_factorial(number):
    if number <= 1:
        return 1
    return number * recursive_factorial(number - 1)


def main():
    print("=" * 50)
    print("DAA Practical 4: Factorial Comparison")
    print("=" * 50)

    try:
        number = int(input("Enter a non-negative integer: "))
        if number < 0:
            print("Invalid input! Please enter a non-negative integer.")
            return

        iterative_start = time.perf_counter()
        iterative_result = iterative_factorial(number)
        iterative_time = time.perf_counter() - iterative_start

        recursive_start = time.perf_counter()
        recursive_result = recursive_factorial(number)
        recursive_time = time.perf_counter() - recursive_start

        print(f"\nNumber: {number}")
        print(f"Iterative factorial: {iterative_result}")
        print(f"Iterative execution time: {iterative_time:.9f} seconds")
        print(f"Recursive factorial: {recursive_result}")
        print(f"Recursive execution time: {recursive_time:.9f} seconds")
        print(f"Results match: {iterative_result == recursive_result}")
        print("-" * 50)
        print("Iterative time complexity: O(N)")
        print("Recursive time complexity: O(N)")
        print("Iterative space complexity: O(1)")
        print("Recursive space complexity: O(N) [Call Stack]")
    except ValueError:
        print("Invalid input! Please enter a whole number.")
    except RecursionError:
        print("The number is too large for the recursive implementation.")


if __name__ == "__main__":
    main()