# BEGIN PROB

# BEGIN SUBPROB

Which of the following expressions evaluate to the name of the state, as a string, with the highest mean math section score in 2007? Select all that apply.

*Note: Assume that the highest mean math section score in 2007 was unique to only one state.*

Option 1:

```py
(sat.loc[(sat["Math"] == sat["Math"].max()) & 
       (sat["Year"] == 2007), "State"]
.iloc[0])
```

Option 2:

```py
sat.loc[sat["Year"] == 2007].set_index("State")["Math"].idxmax()
```

Option 3:

```py
sat.groupby("Year")["State"].max().loc[2007]
```

Option 4:

```py
(sat.loc[sat["Math"] == sat.loc[sat["Year"] == 2007, "Math"].max()]
   .iloc[0]  
   .loc["State"])
```

Option 5:

```py
(sat.groupby("Year").apply(
    lambda sat: sat[sat["Math"] == sat["Math"].max()]
).reset_index(drop=True)
.groupby("Year")["State"].max()
.loc[2007])
```

Option 6:

```py
sat.loc[sat['Year'] == 2007].loc[sat['Math'] == sat['Math'].max()]
```

[ ] Option 1
[ ] Option 2
[ ] Option 3
[ ] Option 4
[ ] Option 5
[ ] Option 6
[ ] None of the above

# BEGIN SOLN
**Answer: ** Option 2 and Option 5

# END SOLN
    
# END SUBPROB

# BEGIN SUBPROB
In the box, write a **one-line expression** that evaluates to a DataFrame that is equivalent to the following relation:

$$\Pi_{\text{Year, State, Verbal}} \left(\sigma_{\text{Year } \geq \: 2014 \text{ and Math } \leq \: 600} \left( \text{sat} \right) \right)$$

# BEGIN SOLN
**Answer: ** `sat.loc[(sat['Year'] >= 2014) & (sat['Math'] <= 600), ['Year', 'State', 'Verbal']]`

# END SOLN

# END SUBPROB

# BEGIN SUBPROB
The following two lines define two DataFrames, `val1` and `val2`.

```py
val1 = sat.groupby(["Year", "State"]).max().reset_index()
val2 = sat.groupby(["Year", "State", "# Students"]).min().reset_index()
```

Are `val1` and `val2` identical? That is, do they contain the same rows and columns, all in the same order?

( ) Yes
( ) No

# BEGIN SOLN
**Answer: ** Yes

# END SOLN

# END SUBPROB

# BEGIN SUBPROB
The data description stated that there is one row in `sat` for most combinations of `"Year"` (between `2005` and `2015`, inclusive) and `"State"`. This means that for most states, there are 11 rows in `sat` --- one for each year between 2005 and 2015, inclusive.

It turns out that there are 11 rows in `sat` for all 50 states, except for one state. Fill in the blanks below so that `missing_years` evaluates to an **array**, sorted in any order, containing the years for which that one state does not appear in `sat.

```py
state_only = sat.groupby("State").filter(___(a)___)

merged = sat["Year"].value_counts().to_frame().merge(
    state_only, ___(b)___
)

missing_years = ___(c)___.to_numpy()
```

What goes in blank (a)?

What goes in blank (b)?

What goes in blank (c)?

# BEGIN SOLN
**Answer: ** a: `lambda df: df.shape[0] < 11`, b: `left_index=True, right_on='Year', how='left'` (`how='outer'` also works), c: `merged[merged['# Students'].isna()]['Year']`

# END SOLN

# END SUBPROB

In the previous subpart, we established that most states have 11 rows in `sat` --- one for each year between 2005 and 2015, inclusive --- while there is one state that has fewer than 11 rows, because there are some years for which that state's SAT information is not known.

Suppose we're given a version of `sat` called `sat_complete` that has all of the same information as `sat`, but that also has rows for combinations of states and years in which SAT information is not known. While there are no null values in the `"Year"` or `"State"` columns of `sat_complete`, there are null values in the `"# Students"`, `"Math"`, and `"Verbal"` columns of `sat_complete`. An example of what `sat_complete` may look like is given below.

<center><img src='../assets/images/wi23-final/sat_tail.png' width=30%></center>
<center><img src='../assets/images/wi23-final/sat_other_tail.png' width=30%></center>

*Note that in the above example, `sat` simply wouldn't have rows for West Virginia in 2005 and 2006, meaning it would have 2 fewer rows than the corresponding `sat_complete`.*

# BEGIN SUBPROB
Given just the information in `sat_complete` --- that is, without including any information learned in part (d) --- what is the most likely missingness mechanism of the `"# Students"` column in `sat_complete`?

( ) Not missing at random
( ) Missing at random
( ) Missing completely at random

# BEGIN SOLN
**Answer: ** Not missing at random

# END SOLN

# END SUBPROB

# BEGIN SUBPROB
Given just the information in `sat_complete` --- that is, without including any information learned in part (d) --- what is the most likely missingness mechanism of the `"Math"` column in `sat_complete`?

( ) Not missing at random
( ) Missing at random
( ) Missing completely at random

# BEGIN SOLN
**Answer: ** Missing at random

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

Suppose we perform a permutation test to assess whether the missingness of column $Y$ depends on column $X$.

Suppose we observe a statistically significant result (that is, the $p$-value of our test is less than 0.05). True or False: It is still possible for column $Y$ to be not missing at random.

( ) True
( ) False

# BEGIN SOLN
**Answer: ** Trie

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

Suppose we do not observe a statistically significant result (that is, the $p$-value of our test is greater than 0.05). True or False: It is still possible for column $Y$ to be missing at random dependent on column $X$.

( ) True
( ) False

# BEGIN SOLN
**Answer: ** True

# END SOLN

# END SUBPROB

# END PROB