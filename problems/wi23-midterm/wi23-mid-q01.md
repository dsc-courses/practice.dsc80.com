# BEGIN PROB

# BEGIN SUBPROB

What kind of variable is `"Netflix"`?

( ) Quantitative discrete 
( ) Quantitative continuous 
( ) Qualitative ordinal 
( ) Qualitative nominal

# BEGIN SOLN

**Answer**: Quantitative discrete

Remember, a variable is quantitative (i.e. numerical) if arithmetic operations have meaning. If we add up the values in the `"Netflix"` column for a subset of the rows, we get the number of TV shows in that subset that are available for streaming on Netflix. If we take the average of the values in the `"Netflix"` column for a subset of the rows, we get the proportion of TV shows in that subset that are available for streaming on Netflix. Since arithmetic operations have meaning, `"Netflix"` is quantitative, and since it can only take on a finite number of values (just 0 or 1) it is also discrete.

# END SOLN

# END SUBPROB

In the following subparts, consider the variable `double_count`, defined
below.

`double_count = tv["Title"].value_counts().value_counts()`

# BEGIN SUBPROB

What is `type(double_count)`?

( ) Series 
( ) SeriesGroupBy 
( ) DataFrame 
( ) DataFrameGroupBy

# BEGIN SOLN

**Answer**: Series

The `.value_counts()` method, when called on a Series `s`, produces a new Series in which

- the index contains all unique values in `s`.
- the values contain the frequencies of all unique values in `s`.

Since `tv["Title"]` is a Series, `tv["Title"].value_counts()` is a Series, and so is `tv["Title"].value_counts.value_counts()`. We provide an interpretation of each of these Series in the solution to the next subpart.

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

Which of the following statements are true? Select all that apply.

[ ] The only case in which it would make sense to set the index of `tv` to `"Title"` is if `double_count.iloc[0] == 1` is `True`. 
[ ] The only case in which it would make sense to set the index of `tv` to `"Title"` is if `double_count.loc[1] == tv.shape[0]` is `True`. 
[ ] If `double_count.loc[2] == 5` is `True`, there are 5 TV shows that all share the same `"Title"`. 
[ ] If `double_count.loc[2] == 5` is `True`, there are 5 pairs of 2 TV shows such that each pair shares the same `"Title"`. 
[ ] None of the above.

# BEGIN SOLN

**Answers**:

- The only case in which it would make sense to set the index of `tv` to `"Title"` is if `double_count.loc[1] == tv.shape[0]` is `True`. 
- If `double_count.loc[2] == 5` is `True`, there are 5 pairs of 2 TV shows such that each pair shares the same `"Title"`.

To answer, we need to understand what each of `tv["Title"]`, `tv["Title"].value_counts()`, and `tv["Title"].value_counts().value_counts()` contain. `tv["Title"]`, as we know, contains the name of each TV show.

`tv["Title"].value_counts()` is a Series whose index is a sequence of the unique TV show titles in `tv["Title"]`, and whose values are the frequencies of each title. The first few entries in `tv["Title"].value_counts()` may look something like the following:

```py
Breaking Bad                             1
Fresh Meat                               1
Doctor Thorne                            1
                                       ...
Styling Hollywood                        1
Vai Anitta                               1
Fearless Adventures with Jack Randall    1
Name: Title, Length: 5368, dtype: int64
```

Then, `tv["Title"].value_counts().value_counts()` will be a Series whose index is a sequence of the unique values in the above Series, and whose values are the frequencies of each value above. In the case where all titles in `tv["Title"]` are unique, then `tv["Title"].value_counts()` will only have one unique value, 1, repeated many times. Then, `tv["Title"].value_counts().value_counts()` will only have one row total, and will look something like:

```py
1    5368
Name: Title, dtype: int64
```

This allows us to distinguish between the first two answer choices. The key is remembering 

- The first answer choice, "The only case in which it would make sense to set the index of `tv` to `"Title"` is if `double_count.iloc[0] == 1` is `True`.", is false. As we can see in the example above, the 


# END SOLN

# END SUBPROB

# END PROB