# BEGIN PROB

You create a table called `gums` that only contains the chewing gum
purchases of `df`, then you create a bag-of-words matrix called `bow`
from the `name` column of `gums`. The `bow` matrix is stored as a
DataFrame shown below:

<center><img src="../../assets/images/sp24-final/bow.png" width=400></center>

You also have the following outputs:

```python
>>> bow_df.sum(axis=0)    
pur            5          0     21                  0
gum           41          1     22
sugar          2          2     22                  >>> (bow_df['paperboard'] > 0).sum()
              ..                ..                  20
90             4          37    22
paperboard    22          38    10                  >>> bow_df['gum'].sum()
80            20          39    17                  41
Length: 139               Length: 40
```

For each question below, write your answer as an unsimplified math expression
(no need to simplify fractions or logarithms) in the space provided, or select
"Need more information" if there is not enough information provided to answer
the question.

# BEGIN SUBPROB

What is the TF-IDF for the word `pur` in document 0?

# BEGIN SOLN

**Answer:** 0

# END SOLN

# END SUBPROB



# BEGIN SUBPROB

What is the TF-IDF for the word `gum` in document 0?

# BEGIN SOLN

**Answer:** Need more information

# END SOLN

# END SUBPROB



# BEGIN SUBPROB

What is the TF-IDF for the word `paperboard` in document 1?

# BEGIN SOLN

**Answer:** \frac{1}{22}

\frac{1}{22} \log \left(\frac{40}{20} \right) = \frac{1}{22}

# END SOLN

# END SUBPROB

# END PROB