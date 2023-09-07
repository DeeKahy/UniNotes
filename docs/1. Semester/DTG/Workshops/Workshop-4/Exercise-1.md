

## 1. How many ways can we choose {x, y, z}, where 100000 < x, y, z ≤  1000000?

(1000000-100000+1)^3 = 729'002'430'002'700'001




## 2. Complete the accompanying code by adding the functions isPrime, is2mod5 and isGcd1 so they check the corresponding condition. (Hint for isGcd1: The function does not need to compute the gcd, but can simply check possible divisors. Hint for is2mod5: Find a way to apply the modulus throughout the calculations. Otherwise you will get much too big numbers very quickly when calculating 9x .)

```c
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

/* This function should return 1 if x is prime and 0 otherwise */
int isPrime(int x){
    if(x <= 1) return 0;
    for(int i = 2; i <= sqrt(x); i++){
        if(x % i == 0) return 0;
    }
    return 1;
}


/* This function should return 1 if gcd(x,2)=1 and 0 otherwise */
int isGcd1(int x){
    int a = x;
    int b = 2;
    int r;

    while (b != 0) {
        r = a % b;
        a = b;
        b = r;
    }
    return (a == 1);
}

/* This function should return 1 if 9^x-2 mod 5 = 2 and 0 otherwise */
int is2mod5(int x){
    return ((int)pow(9, x) - 2) % 5 == 2;
}


int main(void){
  int x;
  int p, q, r;

  printf("What number do you want to test?\n");
  scanf("%d", &x);
  printf("x is %d\n", x);

  p = isPrime(x);
  q = isGcd1(x);
  r = is2mod5(x);

  if ((p && !r) || !(p || !q || r) || (!p && !q && r)){
    printf("You have found a valid x\n");
    printf("p is %d, q is %d, and r is %d\n", p,q,r);
  } else {
    printf("Try again!\n");
  }S

  return EXIT_SUCCESS;
}

```

## 3. Try (ten) different values of x and see if you can find one that fulfills all conditions.

1 = try again
2 = p is 1, q is 0, and r is 0
3 = try again
4 = try again
5 = try again
6 = try again
7 = try again
8 = try again
9 = try again
10 = try again
11 = p is 1, q is 1, and r is 0












