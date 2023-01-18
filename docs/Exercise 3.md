!!! info

    We will now study the theoretical complexity of the two algorithms. We will count comparisons made in the course of the algorithm.


## a) Argue that the linear search algorithm will use ***2n + 2*** comparisons in the worst case. Describe the inputs for which this will happen.


1. In the worst case i.e. the number not being in the list, every number will have to be checked, therefore the loop will run ***n*** times.

2. But because we need to do 1 check in the loop itself, this turns from ***n\*1*** into ***n\*2***.
 
3. After all the values have been checked it checks again if we should continue the loop but that returns false as the number is equals n so the loop ends and the short circuit doesnt execute so +1

4. then the if sentence checks if i is lower then n which is another +1

5. now our our final result turned into ***2\*n + 2***



### b) Show that the number of comparisons in the worst case for linear search is in Θ(n).

* In the worst case, the element we are searching for is not in the list or is at the last position of the list.

* The algorithm will have to iterate through the entire array to find the element, making n comparisons.
  
* The number of comparisons is directly proportional to the size of the list.
  
* Therefore, the time complexity for linear search in the worst case is O(n).


## c) Consider the binary search algorithm and assume that the list has length n = 2^k^


### Check that every full iteration of the while loop uses two comparisons.

```c
// the condition for this while loop is the first comparison.
while (i < j) {  
    m = (i + j) / 2;  

	// this if else statement is the 2nd check.
    if (x > array[m]) {  
        i = m + 1;  
    } else {  
        j = m;  
    }  
}  
```


### ~~~Show that in the first iteration of the while loop m = 2^k-1^~~~

```c
int i = 0;  
/* Fill in your code HERE */  
int j = N;  
int m;  

	// loop is the first check.
while (i < j) {  
    m = (i + j) / 2;  
    
    // this if else statement is the 2nd check.
    if (x > array[m]) {  
        i = m + 1;  
    } else {  
        j = m;  
    }  
}  
if (x == array[i]) {  
    return i;  
}else {  
    return -1;  
}
```

Because $n=2^k$ which means that $m = n/2$ which we can rewrite to $m = 2^k /2^1$, and then we take one [arithmetic rules](General-math) to get the desired result of $m=2^{k-1}$



### Argue that after the first time the while loop has run, we have excluded half the elements of the list. 

This statement is true because of the way binary search works, which is by splitting each half in the middle and then splits that middle again.

!!! note

    For binary search to work and be efficient it already has to be sorted.



### Check that we have to half the list log2(n) times, to end up with a list of just one element. (Remember that we assume n = 2^k. What happens if n is not a power of 2?)

```py
# searching for 5;
[1,2,3,4,5,6,7,8]

[1,2,3,4]  5 is in this side -> [5,6,7,8]
[5,6]<- 5 is in this side [7,8]
[5]<- 5 is in this side [5]

[5] <- there is only 1 element left.

```
We decide that n = 2^k^ and since the list gets halved each time, until only 1 element remains the number of elements remaining is divided by 2 k times.
If n is not the power of 2 "if" would just compare the last number (5) to the other list (6,7).


### 1. Consider the final steps of the algorithm. Once i = j the while loop checks its run condition once more. Then the algorithm continues to check if we have found the element in question. Show that the algorithm will need 2*log~2~(n) + 2 comparisons. 

For each loop we have 2 compartments and the loop runs log~2~(n) time, then we have an if statement at the end to break the loop. And because it has if statements after the loop we plus 1 to 2*log~2~(n) + 2



## d) Show that the number of comparisons needed for binary search is Θ(log~2~(n))

We need to figure out if 2*log~2~(n)+2 is Big O to log~2~(n) (+c) which we can do by setting c = 3 which therefore makes it grow faster than 2*log~2~(n)+2.
So yes it is Big O.
Now we need to find if also is Omega which we can do by just setting c to be 1.


!!! note

    we are essentially doing the oposite as in finding if its big O.
    Because our function is both Big O and Omega of our compartment number thingy log~2~(n).


## e) Compare these theoretical results with the results you got from your implementation
From the result before we can clearly see that Lin grows in a linear fashion and our binary function grows logarithmic.

## f) Assume we have a list of 10000 elements and need to search for several elements in it. We want to figure out when it pays off to sort the list before searching. Use the Θ approximations for the following exercises when calculating the number of comparisons made, i.e., assume linear search uses n comparisons and binary search uses log2(n) comparisons.

* How many comparisons will be used when we search for m elements using linear search? 

It would use n*m comparisons.

* We will see that a list of n elements can be sorted with an effort of Θ(n log2(n)). How many operations are needed if we sort the list first, then search for m elements using binary search? 

n log2(n) + (log2(n) * m)


*  At which point, i.e., for which m, do these two approaches have similar complexity? Which one is better when?

linear search is better before 13.305 searches afterwards binear search is faster

```r
# making x equals to m for maple to math it right
x := m
n := 10000;
bin1 := x*log[2](n) + n*log[2](n);
lin1 := n*x; 
approx(solve(bin1 = lin1)); 
= 13.305
```