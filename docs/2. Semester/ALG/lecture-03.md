# Lecture 03

Divide & conquer

divide problem into a number of disjoint subproblems that are smaller instances of same problem

Conquer the subproblem by solving them recursively. If the subproblem is small (and easy) enough solve it trivially 

Combine the solution of the subproblems into the solution for the original problem

else it can be trivial to solve


## exercise 1
Consider the array A = [3, 41, 52, 26, 38, 57, 49, 9]. Give the state of the array after five sub-calls of the algorithm Merge are performed during the execution of the call Merge-Sort(A, 1, 8).

A = [3, 26, 41, 52, 38, 57, 9, 49]

## exercise 2

**CLRS-3 2.3–3**. Use mathematical induction to show that when n is an exact power of 2 (that is, n = 2k for some k ∈ **N** \ {0}), the solution of the following recurrence is T(n) = n lg n

n = 2k


CLRS-3 2.3–4. We can express insertion sort as a recursive procedure as follows. In order to sort A[1 . . n], we recursively sort A[1 . . n − 1] and then insert A[n] into the sorted array A[1 . . n − 1]. Write a recurrence for the worst-case running time of this  recursive version of insertion sort.




CLRS-3 2.3–6. Observe that the while loop of lines 5–7 of the Insertion-Sort procedure uses a linear search to scan (backward) through the sorted subarray A[1 . . j − 1]. Can we use a binary search instead to improve the overall worst-case running time of  insertion sort to Θ(n lg n)?

no as in worse case scenario you still need to shift all bigger elements one to the right.
## exercise 3
Consider the problem of finding the smallest element in a nonempty array of numbers A[1 . . n]

(a) Write an incremental algorithm that solves the above problem and determine its asymptotic worst-case running time.

```py
def find_smallest(A):
    smallest = A[0]   # initialize smallest to the first element in A
    for i in range(1, len(A)):   # iterate through the remaining elements in A
        if A[i] < smallest:   # if the current element is smaller than the current smallest
            smallest = A[i]   # update smallest to the current element
    return smallest
```
The worst-case running time of this algorithm is O(n), since it has to iterate through all n elements in the array at least once in every case.

(b) Write a divide-and-conquer algorithm that solves the above problem and determine its asymptotic worst-case running time.
```py
import math

def find_smallest(A,p,q):
    if q<= p:
        return A[p]
    else:
        m = math.floor((p+q)/2)
        minL = find_smallest(A,p,m)
        minR = find_smallest(A,m+1,q)
        return min(minL,minR)
```
in worst case it is still O(n) assuming we only have 1 thead to work with, if we had 2 then it would be twice as fast O(n/2).

(c) Assume that the length of A is a power of 2. Write a recurrence describing how many comparison operations (among elements of A) your divide-and-conquer algorithm performs, and solve the recurrence using the recursion-tree method. Remark: count ONLY the comparisons performed among elements in A. E.g., a comparison like i ≤ A.length shall not be counted, whereas A[i] ≤ k where k is a variable storing some element of A shall be counted. Moreover, if you use expressions like min(A[i], A[j]) for some indices i, j, that also counts as 1 comparison.















