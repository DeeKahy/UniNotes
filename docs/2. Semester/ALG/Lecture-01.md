# Lecture 01
*Algorithms, Correctness, and Efficiency [8 February 2023]*

## Lecture 1

!!! terms
    permutation = reordering
    
    input/output sequence = list || array

    n~a~ = number of n times a occurs in the sequence

    T(n) T for time

an algorythm must allways have an input and an output
!!! definition
    an algorithm is said to be correct if, for every input instance, it halts with the correct output. we say that a correct algorythm solves the given computational problem.





## Exercise 1

!!! error

    Exercise 4

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

**alg** T(n)=f(n)*10^-6^=1


| f(n)    | 1 second | 1 minute |
| ------- | -------- | -------- |
| lg n    | 2^(10^6) |          |
| sqrt(n) |          |          |
| n lg n  |          |          |
| n^2^    |          |          |
| n^3^    |          |          |
| 2^n^    |          |          |

!!! error

    we do not know how to solve this

## Exercise 5
Let A and B be two arrays of numbers sorted in non-decreasing order, respectively of length n and m. Write the pseudocode of an algorithm that checks whether the set of elements in A is equal to the set of elements in B, i.e., all elements of A  re contained in B and vice versa. What is the worst-case running time of your algorithm?
```py
def compare(A, B):
    # is all of A inside of B?
    for x in A:                # c1 = n+1
        passed = 0             # c2 = n
        for i in B:            # c3 = n * m + 1
            if x < i:          # c4 = n * m
                passed = 1     # c5 = n 
                break          # c6 = n 

            # break out of loop if number is higher
            elif x < i:        # c7 = n * m ~a~
                break          # c8 = n

        # break out of loop if number is higher
        if passed != 1:        # n
            print("Not all of A is contained in B")
            return             # 1
    print("all of A is contained in B")

def compare2(A,B):
    # is all of B inside of A?
    for x in B:
        passed = 0
        for i in A:
            if x == i:
                passed = 1
                break
            elif x < i:
                break

        if passed != 1:
            print("Not all of B is contained in A")
            return
    print("all of B is contained in A")


B= [1,2,3,4,5]    
A = [1,2,3,4,5,6,7,8]

compare(A,B)
compare2(A,B)
```


T(n)=2(c1(n+1) + c2 + c3(n*m+1) + c4(n*m) + c5(n) c6(n) + c7(n*m~a~) + c8(n) + c9(n) + c10)