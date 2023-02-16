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

::: responsebox
0.5in

`:, "Netflix":`
:::

What goes in blank (b)?

::: responsebox
0.5in

`:, 5:`
:::

What goes in blank (c)?

::: responsebox
0.5in

`axis=1`
:::

What goes in blank (d)?

::: responsebox
0.5in

`-1, 0`
:::

# END PROB