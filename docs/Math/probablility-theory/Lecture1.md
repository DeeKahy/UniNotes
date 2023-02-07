
## stuff
- numbers will also be called scalars
- vectors are denoted with lower case

- Zero vecotr vector of multiple 0
- ones vector vector of multiple 1
- e~i~ vector 0 with a singular 1 somewhere?
vector with vectors within is called a list of vectors # could also be a matrix



### vectors of the same length can be added to each other making a new vector with added together values.


```py
import numpy as np

vector1 = np.array([1, 2, 3])
vector2 = np.array([4, 5, 6])

result = vector1 + vector2

print(result)

# Output:
# [5 7 9]
```

### vectors of the same length can be substracted to each other making a new vector with substracted together values.

```py
import numpy as np

vector1 = np.array([1, 2, 3])
vector2 = np.array([4, 5, 6])

result = vector1 - vector2

print(result)

# Output:
# [-3 -3 -3]
```

### you can multiple vector with a scalar.

```py
import numpy as np

vector = np.array([1, 2, 3])
scalar = 2

result = vector * scalar

print(result)

# Output:
# [2 4 6]
```



### Here is an example of a linear combination of numpy vectors in Python:
```py
import numpy as np

vector1 = np.array([1, 2, 3])
vector2 = np.array([4, 5, 6])

coeff1 = 2
coeff2 = 3

result = coeff1 * vector1 + coeff2 * vector2

print(result)

# Output:
# [10 21 36]
```
In this example, two vectors vector1 and vector2 are combined linearly using two scalar coefficients coeff1 and coeff2. The result is a new vector result with the same shape as the input vectors, equal to the sum of the scaled input vectors. The linear combination can be written mathematically as result = coeff1 * vector1 + coeff2 * vector2.



### we need product thingy written down

we can try to make sense of this in exercises

### same with "differencing" and "sum oand average"


### superposition property else known as linear functions

means that you can move fx addition outside of the function and still get the same

a linear function to which you add a constant is called affine.
affine functions do not cross 0x and 0y but linear does
affine functions are linear functions offset