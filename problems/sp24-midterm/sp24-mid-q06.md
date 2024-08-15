# BEGIN PROB

After loading in the DataFrame `df` from Question~\ref{q:pivoting}, Sam realizes that his puppy Bentley ate some of his data! The first few rows of `df` are shown below for convenience.

<center><img src="../../assets/images/sp24-midterm/df.png" width=750></center>

# BEGIN SUBPROB

Suppose that Sam sorted `df` by `is_morning`, and then Bentley ate the first five values from the `duration` column. What is the missingness mechanism for the `duration` column?

( ) Missing by design  
( ) MNAR  
( ) MAR on `is_morning` only  
( ) MAR on `is_morning` and `hour` only  
( ) MAR on `is_morning`, `hour`, and `time` only  
( ) MCAR

# BEGIN SOLN

**Answer:** MAR on `is_morning`, `hour`, and `time` only  

# END SOLN

# END SUBPROB



# BEGIN SUBPROB

Sam believes that the data are MAR on `hour` only, so he decides to use probabilistic imputation to fill in the missing values. He uses the following code copied from Lecture 8 (line numbers shown in parentheses):

```python
(1)  def impute(s):
(2)      s = s.copy()
(3)      n = s.isna().sum()
(4)      fill = np.random.choice(s.dropna(), n)
(5)      s[s.isna()] = fill
(6)      return s
(7)  df.groupby('hour')['duration'].transform(impute)
```

1.  Even though this code is copied from lecture, it can raise an error on Sam’s data if a certain condition is met. Which of these, if true, would cause the code to error?

( ) The missing values in `duration` are actually NMAR.
( ) The missing values in `duration` are actually MAR on `street`, not `hour`.
( ) There are no missing values in `duration`.
( ) At least one `hour` value doesn't have any missing `duration` values.
( ) At least one `hour` value only has missing `duration` values.
( ) There are no rows where `hour == 12`.

2.  Which line in the code would raise the error?

( ) Line 1
( ) Line 2
( ) Line 3
( ) Line 4
( ) Line 5
( ) Line 6
( ) Line 7


# BEGIN SOLN

**Answer:** 
1. At least one `hour` value only has missing `duration` values.

**Answer:** 
2. Line 4

# END SOLN

# END SUBPROB

# END PROB