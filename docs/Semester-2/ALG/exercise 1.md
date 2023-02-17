Solve the following exercises. The exercises that are more involved are marked with a star. If you
need some guidance for solving the exercise, place your trash bin in front of your group room’s door
and the first available teaching assistant will come to help you out.

Exercise 1.
Consider the problem of finding the two smallest numbers in a nonempty sequence of numbers ⟨a1, . . . , an⟩ not necessarily sorted.

(a) Formalise the above as a computational problem (be careful to precisely define the input, the output, and their relationship).



(b) Write the pseudocode of an algorithm that solves the above computational problem assuming the sequence is given as an array A[1 . . n].


```py
def getAndRemoveSmallest(A):
    smallest = maxint
    for x in A:
        if x < smallest:
            smallest = x
    
    A.remove(smallest)

mylist = [a1,a2,a3,..., an]
print(getAndRemoveSmallest(mylist))
print(getAndRemoveSmallest(mylist))
```


c1 1+1

c2 n+1 + n -1 +1 

c3 n + n-1

c4 n~a~  + n~a~ (0-n)

c5 1 + 1



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

O(n) 
