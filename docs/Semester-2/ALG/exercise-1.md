# Exercise Session 01

## Exercise 1

Solve the following exercises. The exercises that are more involved are marked with a star. If you
need some guidance for solving the exercise, place your trash bin in front of your group room’s door
and the first available teaching assistant will come to help you out.

Exercise 1.
Consider the problem of finding the two smallest numbers in a nonempty sequence of numbers ⟨a1, . . . , an⟩ not necessarily sorted.

(a) Formalise the above as a computational problem (be careful to precisely define the input, the output, and their relationship).

**Input:** A sequence of numbers of n > 1 numbers not necessarely sorted A = ⟨a1, a2, ..., an⟩

**Output:** A pair of numbers ⟨b1, b2⟩, where b1 and b2 are the two smallest numbers in A and b1 < b2.


(b) Write the pseudocode of an algorithm that solves the above computational problem assuming the sequence is given as an array A[1 . . n].



```py
def getAndRemoveSmallest(A):          
    smallest = [maxint, maxint]       
    for x in A:
        if x <= smallest[0]
            smallest.pop(1) # last
            smallest.append(x,0)  
            
    return smallest


mylist = [a1,a2,a3,..., an]
print(getAndRemoveSmallest(mylist))
```


(c) Assume that line i of your pseudocode takes constant time ci to execute. What is the worst case
running time of your algorithm?

```py
def getAndRemoveSmallest(A):         #      
    smallest = [maxint, maxint]      # c1 = 1
    for x in A:                      # c2 = n+1
        if x <= smallest[0]          # c3 = n
            smallest.pop(1)          # c4 = n~a~
            smallest.append(x,0)     # c5 = n~a~
                                     #
    return smallest                  # c6 = 1


mylist = [a1,a2,a3,..., an]
print(getAndRemoveSmallest(mylist))
```

T(n) = c1 + c2(n+1) + c3(n) + c4(n~a~) + c5(n~a~) + c6


## Exercise 2
Consider the following pseudocode for the function Find-Element takes as input an array A[1 . . n] and a number a
```ruby
Find-Element(A, a)      #
1 for i = 1 to A.length #
2   if A[i] = a         #
3       return i        #
4 return i              #
``` 

(a) Count the number of iterations of the for loop in the above pseudocode for the execution of Find-Element([1, 0, 5, 2, 4], 5) and report the value returned at the end of the call.

the loop will run 3 times and return the index which is 3

(b) Is the above algorithm solving the element search problem presented in class? Justify your answer.

no as it does not return 0 when not found but the index of last element


##Exercise 3.
Write a pseudocode of an algorithm to reverse an array of numbers, i.e., the last element should become the first, the second last should become the second, etc. For example, the reverse of [1, 2, 3, 4] is [4, 3, 2, 1].


```py
import math

def reverse_array(arr):
    for i in range(math.floor(len(arr)/2)):
        temp = arr[i]
        arr[i] = arr[len(arr)-i-1]
        arr[len(arr)-i-1] = temp
    return arr
```

(a) What is the worst-case running time of your algorithm?

c1(n/2 floored + 1) + (c2 + c3 + c4)(n/2 floored + 1)  + c5



(b) Try now to propose an algorithm that use only a constant amount of extra space. What is the worst-case running time of your algorithm?

we already did this from the start


## Exercise 4.
[CLRS-3, Problem 1–1] For each function f(n) and time t in the following table, determine the largest size n of a problem that can be solved in time t, assuming that the algorithm to solve the problem takes f(n) microseconds (1 microsecond = 10−6 seconds)


|         | 1 second | 1 minute |
| ------- | -------- | -------- |
| lg n    |          |          |
| sqrt(n) |          |          |
| n lg n  |          |          |
| n^2^    |          |          |
| n^3^    |          |          |
| 2^n^    |          |          |


