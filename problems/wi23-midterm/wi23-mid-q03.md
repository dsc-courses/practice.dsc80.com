# BEGIN PROB

As you saw in the first few rows of `tv`, some TV shows are available
for streaming on multiple streaming services. Fill in the blanks so that
the two expressions below, Expression 1 and Expression 2, **both**
evaluate to the `"Title"` of the TV show that is available for streaming
on the **greatest number of streaming services**. Assume there are no
ties and that the `"Title"` column contains unique values.

Expression 1:

    tv.set_index("Title").loc[__(a)__].T.sum(axis=0).idxmax()

Expression 2:

    (
        tv.assign(num_services=tv.iloc[__(b)__].sum(__(c)__))
            .sort_values("num_services")
            .iloc[__(d)__]
    )

***Hint***: `.T` transposes the rows and columns of a DataFrame --- the
indexes of `df` are the columns of `df.T` and vice versa.

What goes in blank (a)?

What goes in blank (b)?

What goes in blank (c)?

What goes in blank (d)?

# BEGIN SOLN
**Answer: ** a) `:, "Netflix":` or some variation of that; b) `:, 5:` or some variation of that; c) `axis=1`; d) `-1, 0`

In Expression 1, we need to know that idxmax returns the index of the row with the maximum value. Then we can deduce that Expression 1 basically sums up the value of the columns for each row and returns the index of the row with the greatest sum. Since we want the TV show that is available on the most streaming services, we essentially need to select all the streaming services indicator columns (which are the columns including and after `"Netflix"`) or `:, "Netflix":`. Thus, selecting these columns, summing over the rows, and then applying `idxmax()` will effectively yield the the TV show that is available on the most streaming services.

Looking at Expression 2, we can split our attention for this problem into two parts: the code inside the `assign` statement, and the code outside of it. Glancing at the code inside of the `assign` statement, (and also noticing the variable `num_services`), we realize that we, once again, want to sum up the values in the streaming services indicator columns. We do this by first selecting the last 4 columns or `.iloc[:, 5:]` (notice the `iloc`), and then summing over `axis=1`. We use `axis=1` (different from `axis=0` in Expression 1), because unlike Expression 1, we're summing over each row, instead of column. If there had not been a `.T` in the code for Expression 1, we would've also used `axis=1` in Expression 1.

Finally, we need to select the `"Title"` of the last row in DataFrame in Expression 2, (b/c `sort_values` sorts in ascending order by default), which we simply do through `.iloc[-1 ,0]`.

# END SOLN

# END PROB