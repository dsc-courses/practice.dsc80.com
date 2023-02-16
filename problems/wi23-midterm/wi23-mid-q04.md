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

::: responsebox
0.75in

`filter(lambda df: (df["IMDb"] >= 9).sum() >= 5)`
:::

# END PROB