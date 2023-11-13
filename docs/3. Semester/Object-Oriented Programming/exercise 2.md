# Exercises 2
| #   | Question                                                                                                                                                                         | #                                                                                                                                                                                         |
| --- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 7   | Consider the following two variable declarations: `byte small = 10; int big = 99;` how will you assign the value in the big variable to the small variable?                      | By casting the bigger one to the smaller one, though this is dangerous because an int could pottentially hold a higher number compared to a byte, since a byte can only have a max of 127 |
| 8   | Why do you need to use a cast when you assign a variable of a bigger size to a variable of smaller size, for example, assigning an int variable to a byte variable?              | Because casting is a way to safely try to convert between different types of data, and handle issues like overflows.                                                                      |
| 9   | Name two primitive data types in Java whose values can be floating-point numbers.                                                                                                | float and double                                                                                                                                                                          |
| 10  | If you declare a variable of the boolean type, what are the two possible values it can have?                                                                                     | True and False                                                                                                                                                                            |
| 11  | Can you cast a boolean value to an int type, as shown in the following statement? `boolean done = true; int x = (int) done;` What happens when you compile this snippet of code? | No, java unlike other languages does not treat true and false as 0 and 1                                                                                                                  |
| 12  | Are the boolean literals true and false the same as integers 1 and 0?                                                                                                            | No                                                                                                                                                                                        |
| 13  | Name an unsigned numeric data type in Java.                                                                                                                                      | java does not support unsigned numbers of any kind, char could technically work as an unsigned 16bit number but thats not in spirits with the answer                                      |




!!! Question
    What will be the value of x after this snippet of code is executed? Explain your answer with steps performed explaining how the value of x changes during the execution of the second statement
    ```java
    public static void main(String[] args) {
    int x = 23;
    x = x++ % x;
    System.out.println(x);
    System.out.println(23%24);
    }
    ```

Because the "++" is at the end which means java will use **post-increment**, it will only change after the variable is being used, so it becomes 23 % 24 as it is 23. 

!!! Question
    Explain why the following snippet of code does not compile:
    ```java
    int x = 10;
    boolean yes = (x = 20);
    ```
because you cant assign int to boolean you are missing a second = for comparison
!!! Question
    What will be the value assigned to the variable named yes when the following snippet of code is executed?
    ```java
    int x = 10;
    boolean yes = (x == 20);
    ```
false



!!! Question
    What will be the output when the following snippet of code is executed?
    ```java
    boolean b = true;
    String str = !b + " is not " + b;
    System.out.println(str);
    ```
false is not true because the negative of true is false.

!!! Question
    Complete the second statement using the ternary operator (? :) and the bitwise AND operator (&) that will make a message "x is odd". Your code must contain the following tokens in any order: x, &, ==, ?, :, "odd", and "even". You may use additional tokens as needed:
    ```java
    int x = 1969;
    String str = Integer./* your code goes here */;
    System.out.println("1969 in hex is " + str);
    ```
```java
int x = 19;
String msg = x % 2 == 0 ? "even" : "odd";
System.out.println("x is " + msg);
```

!!! Question
    Fix the compile-time errors in the following snippet of code. Make sure the fixed code prints the value of y:
    ```java
    int x = 10;
    int y = 20;
    if (x = 10)
        y++;
    System.out.println("y = " + y);
    else
        y--;
    System.out.println("y = " + y);
    ```
fixed.

```java
int x = 10;
int y = 20;
if (x == 10){
      y++;
      System.out.println("y = " + y);
} else{
      y--;
      System.out.println("y = " + y);
}
```


!!! Question
    Rewrite the following snippet of code using an if-else statement. Make sure that the switch and if-else statements both have the same output when you initialize the variable x to another value. (Hint: This is a tricky question because there are no break statements in any case labels.)
    ```java
    int x = 50;
    switch (x) {
    case 10:
        System.out.println("Ten");
    default:
        System.out.println("No-match");
    case 20:
        System.out.println("Twenty");
    }
    ```
```java
int x = 50;
if (x == 10) {
    System.out.println("Ten");
    System.out.println("No-match");
    System.out.println("Twenty");
} else if (x == 20) {
    System.out.println("Twenty
} else {
    System.out.println("No-match");
    System.out.println("Twenty");
}
```


!!! Question
    The intent of the following for statement is to print integers from 1 to 10 in reverse order. The code does not print the numbers as intended. Identify the logical error and fix the code, so it prints 10, 9, 8, 1:
    ```java
    for(byte b = 10; b >= 1; b++)
        System.out.println(b);
    ```
```java
for(byte b = 10; b >= 1; b--)
    System.out.println(b);
```

!!! Question
    Write a snippet of code using a for statement that calculates the sum of all integers from 1 to 10 and prints it on the standard output. The template for your code is as follows:
    ```java
    int sum = 0;
    for(<your-code>; <your-code>; <your-code>);
    System.out.println("Sum = " + sum);
    ```
```java
int sum = 0;
for(int i = 1; i <= 10; sum+=i++); // cursed
System.out.println("Sum = " + sum);
```
```java
int sum = 0;
for(int i = 1; i <= 10; sum += i, i++); // still cursed
System.out.println("Sum = " + sum);
```



!!! Question
    Revise your solution to exercise 10 (Exercise 11, Chapter 6) and make sure that System.out.println is called three times exactly and the calls are the same as in the switch statement (each of them is used only once)
    
    Rewrite the following snippet of code using an if-else statement. Make sure that the switch and if-else statements both have the same output when you initialize the variable x to another value. (Hint: This is a tricky question because there are no break statements in any case labels.)
    ```java
    int x = 50;
    switch (x) {
    case 10:
      System.out.println("Ten");
    default:
      System.out.println("No-match");
    case 20:
      System.out.println("Twenty");
    }
    ```

11 solution

```java
int x = 50;
if (x == 10) {
    System.out.println("Ten");
    System.out.println("No-match");
    System.out.println("Twenty");
}
if (x != 10 && != 20) {
    System.out.println("Twenty
} else {
    System.out.println("No-match");
    System.out.println("Twenty");
}
```
11 modified solution to meet 13
```java
int x = 50;
int x = 10;
if (x == 10) {
    System.out.println("Ten");
    x = 69;
} 
if (x != 10 && x != 20){
    System.out.println("No-match");
    x = 20;
}
if(x == 20){   
    System.out.println("Twenty");
}
```
```java
//less curseroni
int x = 20;
if (x == 10) {
    System.out.println("Ten");
} if (x != 20) {
    System.out.println("No-match");
}
System.out.println("Twenty");
  ```
!!! Question
    Use a nested for statement to print the following pyramid:
    ```
        *
       ***
      *****
     *******
    ```
```java
for (int i = 1; i <= 4; i++) {
// Printing leading spaces
for (int j = 1; j <= 5 - i; j++) {
    System.out.print(" ");
}
// Printing asterisks
for (int j = 1; j <= 2 * i - 1; j++) {
    System.out.print("*");
}
// Moving to the next line after each row
System.out.println();
}
```
!!! Question
    Complete the following snippet so that it computes the Fibonacci of an integer n (replace ?1 and ?2 by zero, one, or more statements)
    ```java
    int n = 15;
    int fib = 0;
    int k = 0;
    ?1
    while ( k < n ) {
      ?2
    }
    System.out.println("The Fibonacci of "+n+" is "+fib);
    ```
```java
int n = 15;
int fib = 0;
int k = 0;
int last = 1;
int tmp = last;
while (k < n) {
    tmp = last;
    last = fib + last;
    fib = tmp;
    k++;
}
System.out.println("The Fibonacci of " + n + " is " + fib);
```