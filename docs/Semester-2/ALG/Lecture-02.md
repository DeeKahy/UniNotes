# Lecture 02
Insertion sort & Asymptotic notation [15 February 2023]
!!! notice
    no notes from the lecture

## Exercise 1.
**CLRS-3 3.1–1** Let f(n) and g(n) be asymptotically nonnegative functions. Using the basic definition of Θ-notation, prove that max(f(n), g(n)) = Θ(f(n) + g(n)). Remark: A function f(n) is asymptotically nonnegative if there exists n0 such that f(n) 0 for all n ≥ n0



f(n) and g(n) = asymptotically nonnegative functions
max(f(n), g(n)) = Θ(f(n) + g(n))

because the definiton of Θ is asymptotically tightbound, if we max the function we would just reach Θ



Solution 1.
CLRS-3 3.1–1 Let f(n) and g(n) be asymptotically nonnegative functions. Using the basic definition
of Θ notation, prove that max(f(n), g(n)) = Θ(f(n) + g(n)).
We have to prove that there exists c1, c2 > 0, and n0 such that 0 ≤ c1(f(n) + g(n)) ≤
max(f(n), g(n)) ≤ c2(f(n) + g(n)) for all n ≥ n0. We know that f(n) and g(n) are asympototically nonnegative, then we can choose n0 > 0 such that f(n) ≥ 0 and g(n) ≥ 0 for all n ≥ n0.
Let c1 = 1/2, c2 = 1, and n ≥ n0. On the one hand, we have that max(f(n), g(n)) ≤ f(n)+g(n)
because the max of two nonnegative numbers is always smaller than their sum. On the other
hand, we have 1/2(f(n)+g(n)) ≤ max(f(n), g(n)) because the average of two numbers is always
less than or equal to the maximum of the two.

**CLRS-3 3.1–4** Is 2^n+1^ = =(2n)? Is 2^2n^ = O(2n)?

2^n+1^ = Θ(2n) yes because its just 2n since the +1 doesnt matter for Θ.

2^2n^ = O(2n) is not true because 2^2^ = 4 so it would be O(4)


## Exercise 2.

Consider the algorithm SumUpTo that takes as input a natural number n ∈ N.

```py
def SumUpTo(n):
    s = 0
    for (i + 1) in range(n):
        s = s + i
    
    return s
```

Use the technique of loop invariants to prove that, given n ∈ N, SumUpTo terminates and returns (n* (n+1)) / 2

**Initialisation:** s is always 0 if n is 0 as the loop does not run

**Maintenance:** for each itteration is executes 
s = s + i which means it runs n times and adds the current n at every step to it

**Termination:** it terminates at i~n~ = n and returns (n* (n+1)) / 2

## Exercise 3.
By getting rid of the asymptotically insignificant parts on the expressions, give a simplified asymptotic tight bounds (big-theta notation) for the following functions in n. Here, k ≥ 1, e > 0 and c > 1 are constants.

* 0.001n^2^ + 70000n = # Θ(n^2^)
* 2^n^ + n^10000^ = # Θ(n^2^)
* n^k^ + c^n^ = # Θ(c^n^)
* logk n + n^e^ = # Θ(n^e^)
* 2^n^ + 2^n/2^ = # Θ(2^n^)
* n^log^ ^c^ + c^log^ ^n^ # they cancel eachother out so they are the same.

(hint: look at some properties of the logarithm at CLRS-3 p. 56 or CLRS-4 p. 66)