## What is induction?
Induction is a method of mathematical reasoning in which a conclusion is drawn from a sequence of statements, each of which is supported by evidence. 

### example

We want to prove that the sum of the first n odd numbers is always equal to n^2.

Base case: When n = 1, the sum of the first odd number (1) is 1^2 = 1.

Inductive step: Assume that the statement is true for n = k (where k is any positive integer). We will now prove that it is also true for n = k+1.

The sum of the first k+1 odd numbers is the sum of the first k odd numbers plus the (k+1)th odd number.

The sum of the first k odd numbers is k^2 (by our assumption), and the (k+1)th odd number is (2k+1).

Therefore, the sum of the first k+1 odd numbers is k^2 + (2k+1) = k^2 + 2k + 1 = (k+1)^2.

Thus, we have shown that the statement is true for n = k+1, and since it is also true for n = 1 (the base case), it is true for all positive integers n by induction.


## What sorting algorithms do we know
### Merge Sort
Merge sort is a divide and conquer algorithm that divides an array into two smaller sub-arrays and then merges them back together in a sorted order. It first divides the array into two equal parts, recursively sorts each half, and then merges the two sorted halves back together. It has a time complexity of O(n log n) and is a stable sort.

### Bubble Sort
Bubble sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted. It has a time complexity of O(n^2) and is a stable sort.

### Quick Sort
QuickSort is a divide-and-conquer algorithm. It selects a 'pivot' element from the array and partition the other elements into two sub-arrays, according to whether they are less than or greater than the pivot. The sub-arrays are then recursively sorted. It has a time complexity of O(n log n) and is an unstable sort.

## Which searching algorithm is better, linear og binary search?
```m
# making x equals to m for maple to math it right
x := m
n := 10000;
bin1 := x*log[2](n) + n*log[2](n);
lin1 := n*x; 
approx(solve(bin1 = lin1)); 
= 13.305
```


## Forms

!!! note

    P(x) "∧" ¬Q(x) = CNF

    P(x) "∨" ¬Q(x) = DNF

    "(P ∨ Q)" ∧ "(P ∨ ¬Q)" = PCNF

    "(P ∧ Q)" ∨ "(P ∧ ¬Q)" = PDNF

    (P ∨ Q) ∧ "(P)" = CNF because there is no second (clause)
    
    (P ∧ Q) ∨ "(P)" = DNF because there is no second (clause)

## How many minterms can you make when you have 4 and 5 variables?

The number of minterms made depends on variable count =v | number of minterms = 2^v^

!!! example

    5 variables = 2^5^ = 32
    4 variables = 2^4^ = 16

The number of minterms that can be made when you have 3 variables is 2^3 = 8 minterms. This is because for each variable, there are 2 possibilities (either 0 or 1), and for 3 variables, there are 2^3 = 8 possible combinations.

Similarly, the number of minterms that can be made when you have 5 variables is 2^5 = 32 minterms. This is because for each variable, there are 2 possibilities (either 0 or 1), and for 5 variables, there are 2^5 = 32 possible combinations.

## What is Big O notation
Big O notation is a way to describe the upper bound of the running time of an algorithm, which gives an idea of how the time complexity of the algorithm scales as the input size increases.


## What is Big Theta notation
Big Theta notation, is a way to describe the tight bound of the running time of an algorithm,

## what is big omega notation
Big O notation is a way to describe the lower bound of the running time of an algorithm,

## 

## How to calculate time complexity
1.     Break down the algorithm into smaller parts, each with its own operations count.

2. Identify the part of the algorithm that takes the most time, which is the part that dominates the running time. This is known as the "time-critical" part of the algorithm.

3. Write an expression that represents the number of operations as a function of the input size. This is known as the time complexity of the algorithm.

4. Use the Big O notation to express the time complexity of the algorithm, where O(f(n)) represents the upper bound of the running time. For example, O(n) represents a linear time complexity, O(n^2) represents a quadratic time complexity and so on.

5. Simplify the time complexity expression if possible, to express it in the simplest form.

6. Validate the time complexity by testing the algorithm with different input sizes and observing how the running time changes.


## Time Compexity Table

| Algorythm      | Best        | Average     | Worst        | Worst    |
| -------------- | ----------- | ----------- | ------------ | -------- |
| Selection Sort | Ω(n^2)      | θ(n^2)      | O(n^2)       | O(1)     |
| Bubble Sort    | Ω(n)        | θ(n^2)      | O(n^2)       | O(1)     |
| Insertion Sort | Ω(n)        | θ(n^2)      | O(n^2)       | O(1)     |
| Heap Sort      | Ω(n log(n)) | θ(n log(n)) | O(n log(n))  | O(1)     |
| Quick Sort     | Ω(n log(n)) | θ(n log(n)) | O(n^2)       | O(n)     |
| Merge Sort     | Ω(n log(n)) | θ(n log(n)) | O(n log(n))  | O(n)     |
| Bucket Sort    | Ω(n +k)     | θ(n +k)     | O(n^2)       | O(n)     |
| Radix Sort     | Ω(nk)       | θ(nk)       | O(nk)        | O(n + k) |
| Count Sort     | Ω(n +k)     | θ(n +k)     | O(n +k)      | O(k)     |
| Shell Sort     | Ω(n log(n)) | θ(n log(n)) | O(n^2)       | O(1)     |
| Tim Sort       | Ω(n)        | θ(n log(n)) | O(n log (n)) | O(n)     |
| Tree Sort      | Ω(n log(n)) | θ(n log(n)) | O(n^2)       | O(n)     |
| Cube Sort      | Ω(n)        | θ(n log(n)) | O(n log(n))  | O(n)     |


