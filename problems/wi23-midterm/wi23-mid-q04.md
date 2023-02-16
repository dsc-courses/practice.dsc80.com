# BEGIN PROB

In 2020, during the early COVID era, popular shows like *Never Have I
Ever*, *The Last Dance*, and *The Queen's Gambit* were all released.
What they all share in common, other than high viewership numbers and
popularity on social media, are high ratings on both IMDb and Rotten
Tomatoes.

Fill in the blank below so that `top_years` evaluates to an **array** of
the **years** in which **at least 5 TV shows with an IMDb rating of 9 or
higher were released**.

    top_years = tv.groupby("Year").filter(____)["Year"].unique()

What goes in the blank?

# BEGIN SOLN

**Answer**: `lambda df: (df["IMDb"] >= 9).sum() >= 5`

The `filter` method of a `DataFrameGroupBy` object takes in a function. That function should itself take in a DataFrame, corresponding to all of the rows for a particular `"Year"`, and return either `True` or `False`. The result, `tv.groupby("Year").filter(<our function>)`, will be a DataFrame containing only the rows in which the returned Boolean by our function is `True`. For instance, `tv.groupby("Year").filter(lambda df: df.shape[0] >= 2)` will contain all of the rows for `"Years"` with at least 2 TV shows.

In our case, we want `tv.groupby("Year").filter(<our function>)` to evaluate to a DataFrame with all of the `"Years"` that have at least 5 TV shows that have an `"IMDb"` rating of at least 9 (since the provided code afterwards, `["Year"].unique()`, finds all of the unique `"Year"`s in the DataFrame we produce). If `df` is a DataFrame of TV shows, then `(df["IMDb"] >= 9).sum()` is the number of TV shows in that DataFrame with an `"IMDb"` rating of at least 9, and `(df["IMDb"] >= 9).sum() >= 5` is `True` only for DataFrames in which there are at least 5 TV shows with an `"IMDb"` rating of at least 9. Thus, the answer we were looking for is `lambda df: (df["IMDb"] >= 9).sum() >= 5`.

Another good answer we saw was `lambda df: df.loc[df["IMDb"] >= 9, "Title"].nunique() >= 5`.

Fun fact: In the DataFrame we used to produce the exam, the only year that satisfied the above criteria was 2020!

# END SOLN

# END PROB