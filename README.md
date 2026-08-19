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
├── daa_practical_5_coin_change.py # Practical 5: Coin change using dynamic programming
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

### 🔹 Practical 5: Coin Change Using Dynamic Programming
* **File:** `daa_practical_5_coin_change.py`
* **Overview:** Finds the minimum number of coins needed to make a user-provided amount using the dynamic programming approach.
* **Output:** Displays an optimal coin combination, the minimum coin count, execution time, and complexity analysis. It also reports when the amount cannot be formed.

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
| **Practical 5** | **Coin Change (Dynamic Programming)** | $\mathcal{O}(A \times C)$ | $\mathcal{O}(A \times C)$ | $\mathcal{O}(A \times C)$ | $\mathcal{O}(A)$ | N/A |

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
python daa_practical_5_coin_change.py
```
**Sample Terminal Run:**
```text
==================================================
DAA Practical 5: Coin Change Using Dynamic Programming
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
