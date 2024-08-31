# BEGIN PROB

Gabriel owns 3 dogs with a primary breed of `"Beagle"`. No other owner
has more than 2 `"Beagle"`s.

Fill in the blanks so that `gabriels_district` evaluates to the district
that Gabriel lives in.

```py
gabriels_district = (
    dogs.__(i)__
    .agg({"district": __(ii)__, 
            "primary_breed": lambda x: __(iii)__})
    .sort_values("primary_breed")
    ["district"]
    .__(iv)__
)
```

What goes in the blanks?

# BEGIN SOLUTION

**Answer**:

- (i): `groupby("owner_id")`. The idea is to condense the DataFrame into one row per `"owner_id"` such that we know the number of `"Beagle"`s that each owner has. Since Gabriel has the most `"Beagle"`s, if we can sort by number of `"Beagle"`s, Gabriel will be at the bottom (if we sort in increasing order).
- (ii): `max`, `min`, `mean`, or `median` (among other possibilities). Since all of the `"district"` rows for a particular `"owner_id"` are going to be the same, essentially any aggregation method that takes in a Series of identical district numbers – like `[3, 3, 3, 3]` – and returns the number will work.
- (iii): This function needs to take in a Series, `x`, and return the number of elements in the Series that are the string `"Beagle"`. One possible solution is:
    ```py
    (x == "Beagle").sum()
    ```
- (iv): `iloc[-1]`. Since we're sorting by number of `"Beagle"`s in increasing order, Gabriel will be at the bottom.

<average>63</average>

# END SOLUTION

# END PROB