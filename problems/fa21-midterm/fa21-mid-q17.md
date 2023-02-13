# BEGIN PROB

Suppose the `"Flipper Length (mm)"` column has missing values. The distributions of species when the flipper length is missing (null) and when it is present (not null) are shown below:

<center><img src='../assets/images/fa21-midterm/missingness_distribution.png' width=40%></center>

Futhermore, the average flipper length of each species is as follows:

```py
>>> df.groupby('Species')['Flipper Length (mm)'].mean()
Species
Adelie       190.290780
Chinstrap    195.671642
Gentoo       217.147541
Name: Flipper Length (mm), dtype: float64
```

Suppose the overall mean flipper length is computed (using only the observed values). Which of the following is true?

( ) the mean will be biased high
( ) the mean will be biased low
( ) the mean will be unbiased

# BEGIN SOLN
**Answer: ** Option B

Notice from the graph that Gentoo has a disproportionately high number of missing values. And since Gentoo flipper length is higher than average, the overall mean computed will be lower than the actual mean, meaning that the mean will be biased low.

<average>68</average>

# END SOLN

# END PROB