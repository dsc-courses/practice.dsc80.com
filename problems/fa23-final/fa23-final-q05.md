# BEGIN PROB
Giorgia defines the following variables:
```py
a = bus['late'].mean()
b = bus['late'].std()
```
She applies the imputation methods below to the `'late'` column, then recalculates `a` and `b`. For each imputation method, choose whether the new values of `a` and `b` will be lower ($-$), higher ($+$), exactly the same ($=$), or approximately the same ($\approx$) as the original values of `a` and `b`.

# BEGIN SUBPROB
Mean imputation
# BEGIN SOLN
**Answer**: `a`'s new value will be exactly the same as before ($=$); `b`'s new value will be lower than before ($-$) 

By replacing all of the missing values in the `'late'` column with the observed mean, the mean value won't change. However, the squared distances of values to the mean, on average, will decrease, because the imputed dataset will be less spread out, so the standard deviation will decrease.

# END SOLN
# END SUBPROB

# BEGIN SUBPROB
Probabilistic imputation
# BEGIN SOLN
**Answer**: `a`'s new value will be approximately the same as before ($\approx$); `b`'s new value will be approximately the same as before ($\approx$)

Now, to fill in missing values, we're sampling at random from the originally observed set of values. The shape of the imputed distribution will be similar to the shape of the original distribution, so its mean and standard deviation will be similar to that of the original distribution (though not necessarily exactly equal).

# END SOLN
# END SUBPROB

# END PROB