!!!important

    not done!

## Assume that Merge uses (exactly) a + b − 1 comparisons to combine two lists with a and b elements. Furthermore, assume that the length of the input list L is n = 2k. Prove by using induction on k, that Mergesort uses "n(log 2(n) + 1) = 2k (k + 1)" comparisons to sort L. What type of induction did you use?


### basis step

if n = 2 

### Inductive Step:

























Base case

k = 

n = 2^k^

let n = 2


2 * 1 * (1 + 1)






We can prove that the MergeSort function uses "n(log 2(n) + 1) = 2k (k + 1)" comparisons to sort the input list L by using mathematical induction on k, where k is the number of elements in the input list L.

### base case

Lets consider the simplest case where the list L has only one element. In this case, the MergeSort function will not call itself recursively and will not use any comparison to sort the input list L. (k = 1)

### Inductive Step:

Assume that the statement is true for the case where the input list L has 2^k^ elements. That is, the MergeSort function uses "2^k^ (k + 1)" comparisons to sort the input list L with 2^k^ elements.









2^(k+1)^ = 2*2^k^ 

n(log~2~(n) + 1) = 2^k^(k + 1)
a + b − 1


