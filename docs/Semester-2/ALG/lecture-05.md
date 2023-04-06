# Lecutere 05
```py
l = Left(i)
r = Right(i)
if l ≤ A.heap-size and A[l] < A[i]:
    smallest = l
else:
    smallest = i
if r ≤ A.heap-size and A[r] < A[smallest]:
    smallest = r

if smallest != i:
    exchange A[i] with A[smallest]
    Max-Heapify(A, smallest)
```


## exercise 1

Exercise 1.
Consider the Max-Heapify procedure as defined below.

### base case
A = [1]

it checks but fails at all if statements because l and r are both out of range and largest is equals i which lets the recursive function exit.

### inductive step:
A = [1, 2] // remember it sorts backwards
A = [2, 1]

here the left check completes and sets largest = l which then inturn allows the largest != i to run which swaps the location of i and largest, then the function runs again and it completes without any cases being true which then breaks us out of the recursion.

### the last step
A = [1, 3, 2, n4.......nx] // remember it sorts backwards


## exercise 2

Starting with the procedure Max-Heapify, write pseudocode for the procedure Min-Heapify(A, i), which performs the corresponding manipulation on a min-heap. How does the running time of MinHeapify compare to that of Max-Heapify?

```py
l = Left(i)
r = Right(i)
if l ≤ A.heap-size and A[l] < A[i]:
    smallest = l
else:
    smallest = i
if r ≤ A.heap-size and A[r] < A[smallest]:
    smallest = r

if smallest != i:
    exchange A[i] with A[smallest]
    Max-Heapify(A, smallest)
```

## exercise 3
Consider the pseudocode of the Partition procedure.

```py
def Partition(A, p, r):
    x = A[r]
    i = p − 1
    for j = p to r − 1:
        if A[j] >= x:
            i = i + 1
            exchange A[i] with A[j]
    exchange A[i + 1] with A[r]
    return i + 1
```

Assume that all elements in the array A[p . . r] are equal, that is, A[p] = A[p + 1] = · · · = A[r]. What value will Partition(A, p, r) return? How does Quicksort perform on arrays that have the same value compared with Insertion-Sort and Mergesort?


Quicksort: In this scenario, Quicksort performs poorly, as the Partition function will always return an index close to the end of the array, leading to a highly unbalanced partitioning. This results in a worst-case time complexity of O(n^2) for Quicksort.

Insertion-Sort: Insertion-Sort performs well on this type of input, as it has an adaptive nature. When all elements are equal, it will only take linear time, O(n), to sort the array.

Mergesort: Mergesort has a stable time complexity of O(n log n) regardless of the input. While it doesn’t perform as well as Insertion-Sort on this input


## exercise 4

Modify the pseudocode of the Partition procedure so that the Quicksort algorithm will sort in nonincreasing order. Argument about the correctness of your solution.


Consider the pseudocode of Counting-Sort
```py
def counting_sort(A, k):
    n = len(A)
    B = [0] * n
    C = [0] * (k + 1)

    for i in range(n):
        C[A[i]] += 1

    for i in range(1, k + 1):
        C[i] = C[i] + C[i - 1]

    for j in range(n - 1, -1, -1):
        B[C[A[j]] - 1] = A[j]
        C[A[j]] -= 1

    return B

```
```
Counting-Sort(A, B, k)
1 let C[0 . . k] be a new array
2 for i to k
3   C[i] = 0
4 for j = 1 to A.length
5   C[A[j]] = C[A[j]] + 1
6 for i = 1 to k
7   C[i] = C[i] + C[i − 1]
8 for j = A.length downto 1
9   B[C[A[j]]] = A[j]
10  C[A[j]] = C[A[j]] − 1
```
Modify the above pseudocode by replacing the for-loop header in line 8 as
8 for j = 1 to A.length
Is the modified algorithm correct? Is it also stable?
Justify your answers (not necessarily by providing a formal proof).

The modified algorithm is still correct in the sense that it will produce a sorted output. However, the algorithm is no longer stable. The reason for this is that by iterating from the beginning to the end of the input array A in line 8, we are processing the elements in their original order. When multiple elements with the same value are encountered, they will be placed in the output array B in the same order they were processed, which means that they will be placed in reverse order of their original appearance in A. This breaks the stability of the algorithm.