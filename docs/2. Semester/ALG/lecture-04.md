# Lecture 04

the divide and conquer is used for reoccurences else known as recursive functions

3 different methods
!!! Substitution

    gues the form of the solution first then use mathematical induction to prove the solution
    can be used to find constants


!!! recursion-tree

    
!!! Master





## Exercise 1

Consider the following recurrence T(n) = T(2n/3) + Θ(1). Prove that T(n) = O(lg n).

a = 1

b = 3/2

d = 0

log~3/2~(1) == 0

O(n^d^ lg n) == O(n^0^ lg n)  == O(lg n)


## Exercise 2

Consider the following recurrence

```
T(n) =  {
        {    Θ(1)                if n = 1
        {    T(n − 1) + Θ(n)     if n > 1   
        {
```
Prove that T (n) = O(n^2^) using the substitution method.

guess == O(n^2)

c =

n~0~ > 1

T(n − 1) + Θ(n) 

<= c(n-1)^2^ * b*n

we assume b <= c

<= c*(n-1)^2^ * c*n 

== cn^2^ − 2cn + c + cn

we assume c <= cn 

<= cn^2^ − 2cn + cn + cn 

==  cn^2^

## exercise 3

Consider the following recurrence:

```
T(n) =  {
        { Θ(1)                             if n ≤ 1
        { T(⌊n/2⌋) + T(⌈n/2⌉ − 1) + Θ(n)     if n > 1
        {
```
Use the substitution method to prove that T(n) = O(n lg n).

n~0~ > 1

T(⌊n/2⌋) + T(⌈n/2⌉ − 1) + Θ(n)

==T(⌊n/2⌋) + T(⌈n/2⌉ − 1) + bn






















