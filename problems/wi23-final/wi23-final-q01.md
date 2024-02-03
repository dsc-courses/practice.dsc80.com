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

Option 1:
`(sat.loc[(sat["Math"] == sat["Math"].max()) & (sat["Year"] == 2007), "State"].iloc[0])` This expression looks for entries where the math score equals the overall max `Math` score in the dataset and the year is 2007. However, this approach has a limitation: it assumes that the highest math score in the entire dataset occurred in 2007. 

Option 2:
`sat.loc[sat["Year"] == 2007].set_index("State")["Math"].idxmax()` After boolean indexing for entries made in 2007, it correctly returns the state name with the max `Math` score.

Option 3: 
`sat.groupby("Year")["State"].max().loc[2007]` This finds the maximum state name alphabet-wise, not the state with the highest math score. 

Option 4:
`(sat.loc[sat["Math"] == sat.loc[sat["Year"] == 2007, "Math"].max()].iloc[0].loc["State"])` This expression looks to match any recorded score that is equal to the max score in 2007, possibly returning a value outside of 2007. 

Option 5:
`(sat.groupby("Year").apply(lambda sat: sat[sat["Math"] == sat["Math"].max()]).reset_index(drop=True).groupby("Year")["State"].max().loc[2007])` Option 5 works by isolating rows with the highest score per year, and then among these, it finds the state for the year 2007.

Option 6:
`sat.loc[sat['Year'] == 2007].loc[sat['Math'] == sat['Math'].max()]` Similar to Option 4, this expression finds the maximum math score across all years and then tries to match it to the year 2007, which may not be correct.

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

No pair of `Year` and `State` will be appear twice in the DataFrame because each combination of `Year` and `State` are unqiue. Therefore, when grouping by these columns, each group only contains one unique row - the row itself. Thus, using the maximum operation on these groups simply retrieves the original rows.

Likewise, since every combination of `Year`, `State`, and `# Students` is also unique, the minimum operation, when applied after grouping, yields the same result: the original row for each group.

Recall that `.groupby` function in Pandas automatically sorts data based on the chosen grouping keys. As a result, the `val1` and `val2` DataFrames, created using these groupings, contain the same rows and columns, displayed in the same order.


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
**Answer: ** 

- a: `lambda df: df.shape[0] < 11`
- b: `left_index=True, right_on='Year', how='left'` (`how='outer'` also works)
- c: `merged[merged['# Students'].isna()]['Year']`

The initial step (in the `state_only` variable) involves identifying the state that has fewer than 11 records in the dataset. This is achieved by the lambda function `lambda df: df.shape[0] < 11`, leaving us with records from only the state that has missing data for certain years.

Next, applying `.value_counts()` to `sat["Year"]` produces a Series that enumerates the total occurrences of each year from 2005 to 2015. Converting this Series to a DataFrame with `.to_frame()`, we then merge it with the `state_only` DataFrame. This merging results in a DataFrame (merged) where the years lacking corresponding entries in `state_only` are marked as NaN.

Finally, the expression `merged[merged['# Students'].isna()]['Year']` in `missing_years` identifies the specific years that are absent for the one state in the sat dataset. This is determined by selecting years in the merged DataFrame where the `# Students` column has NaN values, indicating missing data for those years.

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
**Answer:** Not missing at random

The fact that there are null values specifically in the cases where SAT data is not available suggests that the missingness of the `# Students` column is systematic. It's not occurring randomly across the dataset, but rather in specific instances where SAT data wasn't recorded or available.

This could mean that the absence of student numbers is linked to specific reasons why the data was not recorded or collected, such as certain states not participating in SAT testing in specific years, or administrative decisions that led to non-recording of data.

The nature of this missingness suggests that it's not random or solely dependent on observed data in other columns, but rather it's related to the inherent nature of the `# Students` data itself.

# END SOLN

# END SUBPROB

# BEGIN SUBPROB
Given just the information in `sat_complete` --- that is, without including any information learned in part (d) --- what is the most likely missingness mechanism of the `"Math"` column in `sat_complete`?

( ) Not missing at random
( ) Missing at random
( ) Missing completely at random

# BEGIN SOLN
**Answer: ** Missing at random

If a state has reported the number of students taking the SAT, it implies that data collection and reporting were carried out. The administrative decision to report SAT scores (including `Math` scores) may be reflected in the `# Students` column. Conversely, if the `# Students` column is empty or null for a certain state and year, it might indicate an administrative decision not to participate or report data for that period. This decision impacts the availability of `Math` scores.

In this context,  the missing values in `Math` scores are linked to observable conditions or patterns in the dataset (like specific years, states, or availability of other related data).

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

Suppose we perform a permutation test to assess whether the missingness of column $Y$ depends on column $X$.

Suppose we observe a statistically significant result (that is, the $p$-value of our test is less than 0.05). True or False: It is still possible for column $Y$ to be not missing at random.

( ) True
( ) False

# BEGIN SOLN
**Answer: ** True

The observation of a statistically significant result (a p-value less than 0.05) in a permutation test suggests there is some association or dependency between the missingness in Y and the values in X. However, this result does not exclude the possibility that the missingness in Y is also influenced by factors not captured in column X, or by the values in Y itself.

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

Suppose we do not observe a statistically significant result (that is, the $p$-value of our test is greater than 0.05). True or False: It is still possible for column $Y$ to be missing at random dependent on column $X$.

( ) True
( ) False

# BEGIN SOLN
**Answer: ** True

Not observing a statistically significant result (a p-value greater than 0.05) in a permutation test means that the test did not find strong evidence of a dependency between X and the missingness in Y. However, this does not definitively prove that such a dependency does not exist. In statistical testing, a lack of significant findings is not the same as evidence of no effect or no association.

# END SOLN

# END SUBPROB

# END PROB