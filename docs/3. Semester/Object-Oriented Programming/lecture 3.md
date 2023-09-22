!!! Question "(Chapter 7, exercise 7, [JavaFundamentals])"
    What is the output of the following code?
```java
public class Employee {
    String name;
    boolean retired;
    double salary;

    public static void main(String[] args) {
        Employee emp = new Employee();
        System.out.println(emp.name);
        System.out.println(emp.retired);
        System.out.println(emp.salary);
    }
}
```
Output is for String is null boolean is false and double is 0.0
!!! Question "(Chapter 8, exercise 5, [JavaFundamentals]) Create a class named Point2D with two int instance variables named x and y."
    Both instance variables should be declared private. Do not ini�alize the two instance variables. Add seters and geters for the two instance variables that will allow the users of the Point2D class to change and access their values. Declare the seters as setX(int x) and setY(int y) and geters as getX() and getY().
```java
public class Point2D {
    private int x;
    private int y;

    public void setX(int x) {
        this.x = x;
    }

    public int getX() {
        return this.x;
    }

    public void setY(int y) {
        this.y = y;
    }

    public int getY() {
        return this.y;
    }
    public static void main(String[] args) {

    }
}
```
!!! Question "(Chapter 8, exercise 6, [JavaFundamentals])" 
    Implement a method named distance in the Point2D class that you created in the previous exercise. The method accepts an instance of the Point2D class and returns the distance between the current point and the point represented by the parameter. The method should be declared as follows:

```java
public class Point2D {
 /* Code from the previous exercise goes here. */
public double distance(Point2D p) {
 /* Your code for this exercise goes here. */
 } 
}
```

answer
```java
public class Point2D {
    private int x;
    private int y;

    public void setX(int x) {
        this.x = x;
    }

    public int getX() {
        return this.x;
    }

    public void setY(int y) {
        this.y = y;
    }

    public int getY() {
        return this.y;
    }

    public double distance(Point2D point) {
        return (Math.sqrt(Math.pow(this.x - point.x, 2)) + (Math.pow(this.y - point.y, 2)));
    }


    public static void main(String[] args) {
        Point2D point1 = new Point2D();
        point1.setX(5);
        point1.setY(10);
        Point2D point2 = new Point2D();
        point2.setX(5);
        point2.setY(10);
        System.out.println(point1.distance(point2));

    }
}
```
Prints out 0
```java

```
!!! Question "(Chapter 8, exercise 7, [JavaFundamentals])" 
    Enhance the Point2D class by adding a static factory method named create(). A factory method in a class is used to create objects of the class. The create() method should be declared as follows:

```java
public class Point2D {
 /* Code from the previous exercise goes here. */
public static Point2D create(int x, int y) {
 /* Your code for this exercise goes here. */
 }
}
```
answer
```java
public class Point2D {
    private int x;
    private int y;

    public void setX(int x) {
        this.x = x;
    }

    public int getX() {
        return this.x;
    }

    public void setY(int y) {
        this.y = y;
    }

    public int getY() {
        return this.y;
    }

    public double distance(Point2D point) {
        return (Math.sqrt(Math.pow(this.x - point.x, 2)) + (Math.pow(this.y - point.y, 2)));
    }

    public static Point2D create(int x, int y) {
        Point2D temp = new Point2D();
        temp.setX(x);
        temp.setY(y);
        return temp;
    }

    public static void main(String[] args) {
        Point2D point1 = Point2D.create(5, 10);
        Point2D point2 = Point2D.create(5, 11);
        System.out.println(point1.distance(point2));

    }
}
```
Prints out 1.0
!!! Question "(Chapter 8, exercise 10, [JavaFundamentals])" 
    What will be the output when the following PassByValueTest class is run?
```java
 // PassByValueTest.java
package com.jdojo.cls.excercise;

public class PassByValueTest {
    public static void main(String[] args) {
        int x = 100;
        System.out.println("x = " + x);
        change(x);
        System.out.println("x = " + x);

        Point2D p = new Point2D();
        p.setX(40);
        p.setY(60);
        System.out.println("p.x = " + p.getX()
                + ", p.y = " + p.getY());

        changePointReference(p);
        System.out.println("p.x = " + p.getX()
                + ", p.y = " + p.getY());

        changePoint(p);
        System.out.println("p.x = " + p.getX()
                + ", p.y = " + p.getY());
    }

    public static void change(int x) {
        x = 200;
    }

    public static void changePointReference(Point2D p) {
        p = new Point2D();
    }

    public static void changePoint(Point2D p) {

        int newX = p.getX() / 2;
        int newY = p.getY() / 2;
        p.setX(newX);
        p.setY(newY);
    }
}
```
Prints out:

x = 100

x = 100

p.x = 40, p.y = 60

p.x = 40, p.y = 60

p.x = 20, p.y = 30

!!! Question "(Chapter 9, exercise 13, [JavaFundamentals])" 
    Create a Circle class that has three private final instance variables named x, y, and radius. The x and y instance variables represent the x and y coordinates of the center of the circle; they are of int data type. The radius instance variable represents the radius of the circle; it is of the double data type. Add a constructor to the Circle class that accepts the values for its instance variables x, y, and radius. Add geters for the three instance variables

```java
public class Circle {
    private int x;
    private int y;
    private double radius;

    public int getX() {
        return x;
    }

    public int getY() {
        return y;
    }

    public double getRadius() {
        return radius;
    }

    public Circle(int x, int y, double radius) {
        this.x = x;
        this.y = y;
        this.radius = radius;
    }
    
    public static void main(String[] args) {

    }
}
```

!!! Question "(Chapter 9, exercise 14, [JavaFundamentals])"
    Enhance the Circle class by adding four instance methods named centerDistance, distance, overlaps, and touches. All these methods accept a Circle as a parameter. The centerDistance method returns the distance (as a double) between the centers of the circle and another circle passed in as the parameter. The distance method returns the minimum distance (as a double) between the two circles. If two circles overlap, the distance method returns a negative number. The overlaps method returns true if two circles overlap and false otherwise. The touches method returns true if two circles touch each other and false otherwise. The distance method must use the centerDistance method. The body of the overlaps and touches methods must contain only one statement that uses the distance method.
    
    Hint The distance between two circles is the distance between their centers minus their radii. Two circles overlap if the distance between them is negative. Two circles touch if the distance between them is zero

```java
public class Circle {
    private int x;
    private int y;
    private double radius;

    public int getX() {
        return x;
    }

    public int getY() {
        return y;
    }

    public double getRadius() {
        return radius;
    }

    public Circle(int x, int y, double radius) {
        this.x = x;
        this.y = y;
        this.radius = radius;
    }

    public double centerDistance(Circle circle) {
        return (Math.sqrt(Math.pow(this.x - circle.x, 2)) + (Math.pow(this.y - circle.y, 2)));
    }

    public double distance(Circle circle) {
        return centerDistance(circle) - radius - circle.radius;
    }

    public boolean overlaps(Circle circle) {
        return distance(circle) < 0;
    }

    public boolean touches(Circle circle) {
        return distance(circle) == 0;
    }

    public static void main(String[] args) {
        
    }
}
```
!!! Question "(Chapter 9, exercise 15, [JavaFundamentals])" 
    Enhance the Circle class by adding two methods named perimeter and area that compute and return the perimeter and area of the circle, respectively

```java
public class Circle {
    private int x;
    private int y;
    private double radius;

    public int getX() {
        return x;
    }

    public int getY() {
        return y;
    }

    public double getRadius() {
        return radius;
    }

    public Circle(int x, int y, double radius) {
        this.x = x;
        this.y = y;
        this.radius = radius;
    }

    public double centerDistance(Circle circle) {
        return (Math.sqrt(Math.pow(this.x - circle.x, 2)) + (Math.pow(this.y - circle.y, 2)));
    }

    public double distance(Circle circle) {
        return centerDistance(circle) - radius - circle.radius;
    }

    public boolean overlaps(Circle circle) {
        return distance(circle) < 0;
    }

    public boolean touches(Circle circle) {
        return distance(circle) == 0;
    }

    public double perimeter() {
        return 2 * Math.PI * radius;
    }

    public double area() {
        return Math.PI * Math.pow(radius, 2);
    }

    public static void main(String[] args) {

    }
}
```
!!! Question "(Chapter 9, exercise 16, [JavaFundamentals])"
    Add a second constructor to the Circle class that takes a double parameter, which is the radius of the circle. This constructor should call another existing constructor of the Circle class with three parameters passing zero as the values for x and y.
```java
public class Circle {
    private int x;
    private int y;
    private double radius;

    public int getX() {
        return x;
    }

    public int getY() {
        return y;
    }

    public double getRadius() {
        return radius;
    }

    public Circle(int x, int y, double radius) {
        this.x = x;
        this.y = y;
        this.radius = radius;
    }
    public Circle(double radius){
        this(0,0,radius);
    }
    public double centerDistance(Circle circle) {
        return (Math.sqrt(Math.pow(this.x - circle.x, 2)) + (Math.pow(this.y - circle.y, 2)));
    }

    public double distance(Circle circle) {
        return centerDistance(circle) - radius - circle.radius;
    }

    public boolean overlaps(Circle circle) {
        return distance(circle) < 0;
    }

    public boolean touches(Circle circle) {
        return distance(circle) == 0;
    }

    public double perimeter() {
        return 2 * Math.PI * radius;
    }

    public double area() {
        return Math.PI * Math.pow(radius, 2);
    }

    public static void main(String[] args) {

    }
}
```
!!! Question
    Explain your answer to exercise 5 in detail.

You overwrite copy of a point you need to overwrite each value independently for it to work.

!!! Question
    Did you use the keyword this in the definition of the class Circle? If you used it, was it necessary? Why?

From what I know yes as I am calling itself constructor

!!! Question 
    Write a method contains that determines if an instance of the Point2D class passed as parameter is contained by the current instance of Circle. This method returns true if the point is contained in the circle and false otherwise. In which of the classes will the new method be included? Justify your choice.

```java

public class Circle {
    private int x;
    private int y;
    private double radius;

    public int getX() {
        return x;
    }

    public int getY() {
        return y;
    }

    public double getRadius() {
        return radius;
    }

    public Circle(int x, int y, double radius) {
        this.x = x;
        this.y = y;
        this.radius = radius;
    }

    public Circle(double radius) {
        this(0, 0, radius);
    }

    public double centerDistance(Circle circle) {
        return (Math.sqrt(Math.pow(this.x - circle.x, 2)) + (Math.pow(this.y - circle.y, 2)));
    }

    public double distance(Circle circle) {
        return centerDistance(circle) - radius - circle.radius;
    }

    public boolean overlaps(Circle circle) {
        return distance(circle) < 0;
    }

    public boolean touches(Circle circle) {
        return distance(circle) == 0;
    }

    public double perimeter() {
        return 2 * Math.PI * radius;
    }

    public double area() {
        return Math.PI * Math.pow(radius, 2);
    }

    public boolean contains(Point2D point) {
        return (Math.sqrt(Math.pow(this.x - point.getX(), 2)) + (Math.pow(this.y - point.getY(), 2))) <= this.radius;
    }

    public static void main(String[] args) {

    }
}
```
I wrote it in circle class as it is a circle that can contain a point and not the other way around

!!! Question
    Write a program that allows for creating circles and points (using the classes created in the previous exercises). The program must allow the user to create any number of circles or points in any order and store the circles and points in a suitable data structure (some options are arrays, java.util.ArrayList, java.util.Vector, java.util.LinkedList). 
    
    Hint: you can use the methods Integer.parseInt(String) and Double.parseDouble(String) to parse String values as an integer value or a double value. Additionally, consider using java.util.Scanner to scan the user’s input.