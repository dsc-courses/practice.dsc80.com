# BEGIN PROB
Giorgia defines the following variables:
```
a = bus['late'].mean()
b = bus['late'].std()
```
She applies the imputation methods below to the `'late'` column, then recalculates `a` and `b`. For each imputation method, choose whether the new values of `a` and `b` will be lower ($-$), higher ($+$), exactly the same ($=$), or approximately the same ($\approx$) as the original values of `a` and `b`.

# BEGIN SUBPROB
Mean imputation
# BEGIN SOLN
**Answer** `a` - ($=$). `b` - ($-$).

`a`:
Since `a` is already calculated from the mean of `'late'`, adding the mean does not move the mean.
`b`:
Since we are adding more data right at the mean, we are lowering the standard deviation as a higher number of samples are gathered right at the mean. 
# END SOLN
# END SUBPROB

# BEGIN SUBPROB
Probabilistic imputation
# BEGIN SOLN
**Answer** `a` - ($\approx$). `b` - ($\approx$).

`a`:
Since we are drawing at random from the original distribution, the mean could go up or down, but will generally stay about the same since the distribution we sample from has the same mean.
`b`:
Since we are drawing at random from the original distribution, the standard deviation could go up or down, but will generally stay about the same since the distribution we sample from has the same standard deviation.
# END SOLN
# END SUBPROB

# END PROB