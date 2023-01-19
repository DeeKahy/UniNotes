

## Proof by using induction, that Mergesort returns the sorted list containing the same elements as the input list L. In the proof you may assume, that Merge returns a sorted list containing the elements of two sorted lists given as inputs.

Mathematical induction is a way to systematically calculate any position in a table. 
If I stand here can I argue that I also can stand a step higher (and so on and so on).

### basis step
Lets consider the simplest case where the list L has only one element. In this case, the MergeSort function will not call itself recursively and will return the input list L as the sorted list in the original state. Because it is already sorted.

``` mermaid
graph TD
    L("L = {5}") --> Sorted("Sorted = {5}")
```

### induction step
Assume that the statement is true for the case where the input list L has n elements >= 1. That is, the MergeSort function returns a sorted list containing the same elements as the input list L with n elements.

Now, consider the case where the input list L has n+1 elements. The MergeSort function will recursively divide the input list L into two subset, one with n/2 elements and the other with n/2 V n/2+1 element until it can not be split anymore.
By our assumtion the merge sort will return a sorted list consiting of the same elements as L. Which is the same as in our base step, 1 element goes in, the same element comes out.

Because we cannot split it any more the merge function will be called to merge the 2 sorted subsets into a single sorted array, since merge only rearanges the elements and doesnt delete, the returned sorted list will contain the same elements as the input list L.

### end

By induction, the thing is true for all cases where the input list L(n) is <= 1




``` mermaid
graph TD
    L("L = {3, 1}") --> N("n/2 | {1}");
    L --> N1("n/2+1 | {3}");
    N1 --> SF
    N --> SF("Sorted = {1, 3}")
```


