## Polynomial interpolation

We begin with polynomial interpolation, where the goal is to find a polynomial passing through some datapoints. The resulting polynomial may be used for evaluating the model between datapoints, which is known as the interpolation of the data, or  lsewhere, which is typically referred to as the extrapolation. Consider a dataset given by n pairs of real numbers

> (t1, y1), (t2, y2), . . . , (tn, yn), 

which we interpret as n points in R^2^. Our underlying assumption is going to be that for all i = 1, . . . , n, j = 1, . . . , n we have ti 6 = tj for i 6 = j. We would like to find a polynomial