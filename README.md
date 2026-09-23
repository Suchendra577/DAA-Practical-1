# Design and Analysis of Algorithms (DAA) - Practical Repository

[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Jupyter Notebook](https://img.shields.io/badge/Jupyter-Notebook-orange.svg?logo=jupyter&logoColor=white)](https://jupyter.org/)
[![Algorithms](https://img.shields.io/badge/Algorithms-DAA%20Lab-green.svg)](#-practicals-summary)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A curated collection of Design and Analysis of Algorithms (DAA) practical lab assignments, featuring implementations of core searching and sorting algorithms, complexity analyses, and execution benchmarking in Python and Jupyter Notebooks.

---

## 📌 Repository Structure

```text
DAA-Practicals/
├── DAA_Practical_1.ipynb       # Practical 1: Bubble, Selection, Merge, & Quick Sort
├── DAA_Practical_2.ipynb       # Practical 2: Linear Search & Binary Search
├── DAA_Practical_3.ipynb       # Practical 3: Heap Sort Algorithm (Interactive Notebook)
├── daa_practical_3_heap_sort.py# Practical 3: Standalone Heap Sort Python Script
├── daa_practical_4_factorial_comparison.py # Practical 4: Factorial comparison
├── daa_practical_5_knapsack.py # Practical 5: 0/1 Knapsack using dynamic programming
├── daa_practical_6_matrix_chain.py # Practical 6: Matrix chain multiplication using dynamic programming
├── daa_practical_7_coin_change.py # Practical 7: Coin change using dynamic programming
├── daa_practical_8_graph_dfs_bfs.py # Practical 8: Graph implementation with DFS & BFS traversal
└── README.md                   # Comprehensive Laboratory Documentation
```

---

## 🚀 Practicals Summary

### 🔹 Practical 1: Fundamental Sorting Algorithms
* **File:** `DAA_Practical_1.ipynb`
* **Algorithms Implemented:** 
  - **Bubble Sort:** Repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.
  - **Selection Sort:** Divides the array into sorted and unsorted regions, repeatedly selecting the smallest element from the unsorted region.
  - **Merge Sort:** Divide-and-conquer algorithm that divides the array into sub-arrays, sorts them recursively, and merges the sorted sub-arrays.
  - **Quick Sort:** Divide-and-conquer algorithm that selects a 'pivot' element and partitions the array around the pivot.

---

### 🔹 Practical 2: Searching Algorithms
* **File:** `DAA_Practical_2.ipynb`
* **Algorithms Implemented:**
  - **Linear Search:** Sequential search algorithm that checks every element in the list until a match is found or the list ends.
  - **Binary Search:** Efficient logarithmic search algorithm that operates on **sorted** arrays by repeatedly dividing the search interval in half.

---

### 🔹 Practical 3: Heap Sort Algorithm
* **Files:** `DAA_Practical_3.ipynb` & `daa_practical_3_heap_sort.py`
* **Overview:** Heap Sort is an efficient, comparison-based, in-place sorting algorithm that utilizes a **Max-Binary Heap** data structure.
* **Core Operations:**
  1. **`heapify(arr, n, i)`**: Maintains the max-heap property for a subtree rooted at index `i`.
  2. **Max-Heap Construction**: Converts an unsorted array into a Max-Heap starting from the last non-leaf node (`n // 2 - 1`) down to index `0`.
  3. **Element Extraction**: Swaps the root element (maximum value) with the last element of the heap and recursively calls `heapify` on the reduced heap.

#### Code Snippet (Heap Sort):
```python
import time

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    return arr
```

---

  ### 🔹 Practical 4: Factorial Comparison
  * **File:** `daa_practical_4_factorial_comparison.py`
  * **Overview:** Compares iterative and recursive approaches for calculating the factorial of a user-provided non-negative integer.
  * **Output:** Displays both factorial results, execution time, whether the results match, and the time and space complexity of each approach.

  ---

### 🔹 Practical 5: 0/1 Knapsack Using Dynamic Programming
* **File:** `daa_practical_5_knapsack.py`
* **Overview:** Selects items with maximum total value without exceeding the user-provided knapsack capacity.
* **Input:** Item weights, item values, and knapsack capacity.
* **Example:** For weights `[2, 3, 4, 5]`, values `[3, 4, 5, 6]`, and capacity `5`, the maximum value is `7` using items 1 and 2.
* **Output:** Displays selected items, total weight, maximum value, execution time, and complexity analysis.

---

### 🔹 Practical 6: Matrix Chain Multiplication Using Dynamic Programming
* **File:** `daa_practical_6_matrix_chain.py`
* **Overview:** Finds the parenthesization of a chain of matrices that minimizes the number of scalar multiplications.
* **Input:** Matrix dimensions. For `N` matrices, enter `N + 1` dimensions.
* **Example:** Dimensions `[10, 30, 5, 60]` represent `A1(10 x 30)`, `A2(30 x 5)`, and `A3(5 x 60)`. The minimum cost is `4500`.
* **Output:** Displays the optimal multiplication order, minimum scalar multiplication count, execution time, and complexity analysis.

---

### 🔹 Practical 7: Coin Change Using Dynamic Programming
* **File:** `daa_practical_7_coin_change.py`
* **Overview:** Finds the minimum number of coins needed to make a user-provided amount using the dynamic programming approach.
* **Output:** Displays an optimal coin combination, the minimum coin count, execution time, and complexity analysis. It also reports when the amount cannot be formed.

---

### 🔹 Practical 8: Implementation of Graph and Searching (DFS and BFS)
* **File:** `daa_practical_8_graph_dfs_bfs.py`
* **Overview:** Builds an undirected graph as an adjacency list from user-provided vertices and edges, then traverses it using both **Breadth-First Search (BFS)** and **Depth-First Search (DFS)**.
* **Core Operations:**
  1. **`build_graph(vertex_count, edges)`**: Constructs an adjacency list from the given vertices and edges.
  2. **`breadth_first_search(graph, start_vertex)`**: Explores the graph level by level using a queue (`collections.deque`), visiting the nearest vertices first.
  3. **`depth_first_search(graph, start_vertex)`**: Explores the graph by going as deep as possible along each branch before backtracking, implemented recursively.
* **Input:** Number of vertices, number of edges, each edge as a pair of vertices, and a starting vertex.
* **Example:** For `6` vertices, edges `[(0, 1), (0, 2), (1, 3), (2, 4), (3, 5)]`, and starting vertex `0`:
  - BFS traversal order: `[0, 1, 2, 3, 4, 5]`
  - DFS traversal order: `[0, 1, 3, 5, 2, 4]`
* **Output:** Displays the BFS traversal order, DFS traversal order, execution time for each, any unreachable vertices, and the complexity analysis.

#### Code Snippet (BFS & DFS):
```python
from collections import deque

def breadth_first_search(graph, start_vertex):
    visited = {start_vertex}
    traversal_order = []
    queue = deque([start_vertex])

    while queue:
        current_vertex = queue.popleft()
        traversal_order.append(current_vertex)

        for neighbour in sorted(graph[current_vertex]):
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

    return traversal_order

def depth_first_search(graph, start_vertex):
    visited = set()
    traversal_order = []

    def visit(vertex):
        visited.add(vertex)
        traversal_order.append(vertex)
        for neighbour in sorted(graph[vertex]):
            if neighbour not in visited:
                visit(neighbour)

    visit(start_vertex)
    return traversal_order
```

---

## 📊 Algorithmic Complexity Comparison

| Practical | Algorithm | Best Case Time | Average Case Time | Worst Case Time | Space Complexity | Stability |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| **Practical 1** | **Bubble Sort** | $\mathcal{O}(N)$ | $\mathcal{O}(N^2)$ | $\mathcal{O}(N^2)$ | $\mathcal{O}(1)$ | Stable |
| **Practical 1** | **Selection Sort** | $\mathcal{O}(N^2)$ | $\mathcal{O}(N^2)$ | $\mathcal{O}(N^2)$ | $\mathcal{O}(1)$ | Unstable |
| **Practical 1** | **Merge Sort** | $\mathcal{O}(N \log N)$ | $\mathcal{O}(N \log N)$ | $\mathcal{O}(N \log N)$ | $\mathcal{O}(N)$ | Stable |
| **Practical 1** | **Quick Sort** | $\mathcal{O}(N \log N)$ | $\mathcal{O}(N \log N)$ | $\mathcal{O}(N^2)$ | $\mathcal{O}(\log N)$ | Unstable |
| **Practical 2** | **Linear Search** | $\mathcal{O}(1)$ | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ | N/A |
| **Practical 2** | **Binary Search** | $\mathcal{O}(1)$ | $\mathcal{O}(\log N)$ | $\mathcal{O}(\log N)$ | $\mathcal{O}(1)$ | N/A |
| **Practical 3** | **Heap Sort** | $\mathcal{O}(N \log N)$ | $\mathcal{O}(N \log N)$ | $\mathcal{O}(N \log N)$ | $\mathcal{O}(1)$ | Unstable |
| **Practical 4** | **Iterative Factorial** | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ | N/A |
| **Practical 4** | **Recursive Factorial** | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ | N/A |
| **Practical 5** | **0/1 Knapsack (Dynamic Programming)** | $\mathcal{O}(N \times W)$ | $\mathcal{O}(N \times W)$ | $\mathcal{O}(N \times W)$ | $\mathcal{O}(N \times W)$ | N/A |
| **Practical 6** | **Matrix Chain Multiplication (Dynamic Programming)** | $\mathcal{O}(N^3)$ | $\mathcal{O}(N^3)$ | $\mathcal{O}(N^3)$ | $\mathcal{O}(N^2)$ | N/A |
| **Practical 7** | **Coin Change (Dynamic Programming)** | $\mathcal{O}(A \times C)$ | $\mathcal{O}(A \times C)$ | $\mathcal{O}(A \times C)$ | $\mathcal{O}(A)$ | N/A |
| **Practical 8** | **Breadth-First Search (BFS)** | $\mathcal{O}(V + E)$ | $\mathcal{O}(V + E)$ | $\mathcal{O}(V + E)$ | $\mathcal{O}(V)$ | N/A |
| **Practical 8** | **Depth-First Search (DFS)** | $\mathcal{O}(V + E)$ | $\mathcal{O}(V + E)$ | $\mathcal{O}(V + E)$ | $\mathcal{O}(V)$ | N/A |

---

## 💻 How to Run

### Option 1: Using Python CLI
Run a standalone Python practical directly from your terminal. For Practical 4:
```bash
python daa_practical_4_factorial_comparison.py
```
**Sample Terminal Run:**
```text
==================================================
DAA Practical 4: Factorial Comparison
==================================================
Enter a non-negative integer: 5

Number: 5
Iterative factorial: 120
Iterative execution time: 0.000001000 seconds
Recursive factorial: 120
Recursive execution time: 0.000001000 seconds
Results match: True
--------------------------------------------------
Iterative time complexity: O(N)
Recursive time complexity: O(N)
Iterative space complexity: O(1)
Recursive space complexity: O(N) [Call Stack]
```

For Practical 5:
```bash
python daa_practical_5_knapsack.py
```
**Sample Terminal Run:**
```text
==================================================
DAA Practical 5: 0/1 Knapsack Using Dynamic Programming
==================================================
Enter item weights separated by spaces: 2 3 4 5
Enter item values separated by spaces: 3 4 5 6
Enter knapsack capacity: 5

Weights: [2, 3, 4, 5]
Values: [3, 4, 5, 6]
Capacity: 5
Selected item numbers: [1, 2]
Total selected weight: 5
Maximum value: 7
Execution time: 0.000020000 seconds
--------------------------------------------------
Time complexity: O(N * W)
Space complexity: O(N * W)
N = number of items, W = knapsack capacity
Result verified: True
```

For Practical 6:
```bash
python daa_practical_6_matrix_chain.py
```
**Sample Terminal Run:**
```text
==================================================
DAA Practical 6: Matrix Chain Multiplication
==================================================
Enter matrix dimensions separated by spaces: 10 30 5 60

Matrix dimensions: [10, 30, 5, 60]
Number of matrices: 3
Optimal multiplication order: ((A1 x A2) x A3)
Minimum scalar multiplications: 4500
Execution time: 0.000020000 seconds
--------------------------------------------------
Time complexity: O(N^3)
Space complexity: O(N^2)
N = number of matrices
```

For Practical 7:
```bash
python daa_practical_7_coin_change.py
```
**Sample Terminal Run:**
```text
==================================================
DAA Practical 7: Coin Change Using Dynamic Programming
==================================================
Enter coin denominations separated by spaces: 1 5 6 9
Enter the amount to make: 11

Coin denominations: [9, 6, 5, 1]
Target amount: 11
Minimum number of coins: 2
Selected coins: [6, 5]
Execution time: 0.000010000 seconds
--------------------------------------------------
Time complexity: O(A * C)
Space complexity: O(A)
A = target amount, C = number of coin denominations
```

For Practical 8:
```bash
python daa_practical_8_graph_dfs_bfs.py
```
**Sample Terminal Run:**
```text
==================================================
DAA Practical 8: Implementation of Graph and Searching (DFS and BFS)
==================================================
Enter the number of vertices: 6
Enter the number of edges: 5
Enter each edge as two space-separated vertices (e.g. 0 1):
Edge 1: 0 1
Edge 2: 0 2
Edge 3: 1 3
Edge 4: 2 4
Edge 5: 3 5
Enter the starting vertex: 0

Vertices: 6
Edges: [(0, 1), (0, 2), (1, 3), (2, 4), (3, 5)]
Starting vertex: 0

BFS traversal order: [0, 1, 2, 3, 4, 5]
BFS execution time: 0.000051400 seconds

DFS traversal order: [0, 1, 3, 5, 2, 4]
DFS execution time: 0.000010100 seconds
--------------------------------------------------
Time complexity: O(V + E)
Space complexity: O(V)
V = number of vertices, E = number of edges
```

### Option 2: Using Jupyter Notebook / VS Code / Google Colab
1. Launch Jupyter Notebook server:
   ```bash
   jupyter notebook
   ```
2. Open any notebook (`DAA_Practical_1.ipynb`, `DAA_Practical_2.ipynb`, or `DAA_Practical_3.ipynb`) or run a standalone Python script.
3. Execute all cells to view interactive prompts, benchmarks, and execution outputs.

---

## ⚙️ How to Push to GitHub

To publish or update this repository on GitHub:

```bash
# 1. Initialize Git repository (if not already done)
git init

# 2. Add remote repository URL
git remote add origin https://github.com/<YOUR_USERNAME>/<YOUR_REPOSITORY_NAME>.git

# 3. Stage all practicals & documentation
git add .

# 4. Commit changes
git commit -m "feat: Add DAA Practical 3 (Heap Sort) and update professional README"

# 5. Push to GitHub main branch
git branch -M main
git push -u origin main
```

---

## 📄 License
This repository is open source under the [MIT License](LICENSE).
