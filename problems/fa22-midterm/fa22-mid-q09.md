# BEGIN PROB

Suppose that in addition to `tasks`, you have the DataFrame named
`clients`, shown below:

<center><img src='../assets/images/fa22-midterm/clients.png' width=35%></center>

The index of the DataFrame contains the names of clients that have been
consulted for, the `'rate'` column contains the pay rate (in dollars per
hour), and the `'active'` column says whether the client is actively being consulted for. Note that the clients which appear in `'clients'` are not exactly the same as the clients that appear in `tasks["client"].value_counts()` That is, there is a client in `tasks["client"]` which is not in `clients`, and a client that is in `clients` that does not appear in `tasks`.

Fill in the code below so that it produces a DataFrame which has all of the columns that appear in `tasks`, but with two additional columns,
`rate` and `activity`, listing the pay rate for each task and whether the client being consulted for is still active. The number of rows in your resulting DataFrame should be equal to the number of rows in `tasks` for which the value in `client` is in `clients`.

```py
tasks.merge(
    clients,
    how=___,
    ___,
    ___
)
```

# BEGIN SOLN
**Answer: ** `'inner'`, `left_on = 'client`, `right_index = True`

The `how` parameter in the merge should be set to inner because we want number of rows in `tasks` for which the value in `client` is in `clients`, which is a union of `tasks` and `client`. Since tasks is the left DataFrame for this merge, we want to merge on the `client` column of `tasks` which we do with `left_on = 'client`. The corresponding column for `clients` in thie merge is just the index, which we do with `right_index = True`.

<average>78</average>

# END SOLN

# END PROB