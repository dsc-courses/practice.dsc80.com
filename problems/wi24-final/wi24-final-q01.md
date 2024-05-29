# BEGIN PROB

Consider the variable `summed`, defined below.

`summed = hotels.groupby("Chain")["Number of Rooms"].sum().idxmax()`

# BEGIN SUBPROB

What is `type(summed)`?

( ) `int`
( ) `str`
( ) `Series`
( ) `DataFrame`
( ) `DataFrameGroupBy`

# BEGIN SOLUTION

**Answer:** `str`

When we do a `groupby` on the `Chain` column in `hotels`, this means that the values in the `Chain` column will be the indices of the DataFrame or Series we get as output, in this case the Series `hotels.groupby("Chain")["Number of Rooms"].sum()`. 

Since the values of `Chain` are strings, and since `.idxmax()` will return a value from the index of the aforementioned Series, `summed` is a string.

<average>88</average>

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

In one sentence, explain what the value of `summed` means. Phrase your explanation as if you had to give it to someone who is not a data science major; that is, don’t say something like “it is the result of grouping `hotels` by `"Chain"`, selecting the `"Number of Rooms"` column, ...”, but instead, give the value context.

# BEGIN SOLUTION

**Answer:** `summed` is the name of the hotel chain with the most total rooms

The result of the `.groupby()` and `.sum()` is a Series indexed by the unique `Chains`, whose values are the total number of rooms in hotels owned by each chain. The `idxmax()` function gets the index corresponding to the largest value in the Series, which will be the hotel chain name with the most total rooms.

<average>97</average>

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Consider the variable `curious`, defined below.

`curious = frame["Chain"].value_counts().idxmax()`

Fill in the blank: `curious` is guaranteed to be equal to `summed` only if `frame` has one row for every ____ in San Diego.

( ) hotel
( ) hotel chain
( ) hotel room
( ) neighborhood

# BEGIN SOLUTION

**Answer:** hotel room

`curious` gets the most common value of `Chain` in the DataFrame `frame`. We already know that `summed` is the hotel chain with the most rooms in San Diego, so `curious` only equals `summed` if the most common `Chain` in `frame` is the hotel chain with the most total rooms; this occurs when each row of `frame` is a single hotel room.

<average>80</average>

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Fill in the blanks so that `popular_areas` is an array of the names of the unique neighborhoods that have at least 5 hotels and at least 1000 hotel rooms.

```py
    f = lambda df: __(i)__
    popular_areas = hotels.groupby(__(ii)__).__(iii)__.__(iv)__
```

1. What goes in blank (i)?

2. What goes in blank (ii)?

( ) `"Hotel Name"`
( ) `"Location"`
( ) `"Chain"`
( ) `"Number of Rooms"`

3. What goes in blank (iii)?

( ) `agg(f)`
( ) `filter(f)`
( ) `transform(f)`

4. What goes in blank (iv)?

# BEGIN SOLUTION

**Answers**:

1. `df.shape[0] >= 5 and df["Number of Rooms"].sum() >= 1000`
2. `"Location"`
3. `filter(f)`
4. `["Location"].unique()` or equivalent

We'd like to only consider certain neighborhoods according to group characteristics (having >= 5 hotels and >= 1000 hotel rooms), and `.filter()` allows us to do that by excluding groups not meeting those criteria. So, we can write a function that evaluates those criteria on one group at a time (the `df` of input to `f` is the subset of `hotels` containing just one `Location` value), and calling `filter(f)` means that the only remaining rows are hotels in neighborhoods that match those criteria. Finally, all we have to do is get the unique neighborhoods from this DataFrame, which are the neighborhoods for which `f` returned `True`.

<average>83</average>

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Consider the code below.

```py
    cond1 = hotels["Chain"] == "Marriott"
    cond2 = hotels["Location"] == "Coronado"
    combined = hotels[cond1].merge(hotels[cond2], on="Hotel Name", how=???)
```

1. If we replace `???` with `"inner"` in the code above, which of the following will be equal to `combined.shape[0]`?

2. If we replace `???` with `"outer"` in the code above, which of the following will be equal to `combined.shape[0]`?

# BEGIN SOLUTION

**Answers**:

1. `(cond1 & cond2).sum()`
2. `cond1.sum() + cond2.sum() - (cond1 & cond2).sum()`

Note that `cond1` and `cond2` are boolean Series, and `hotels[cond1]` and `hotels[cond2]` are the subsets of `hotels` where `Chain == "Marriott` and `"Location" == "Coronado"`, respectively.

1. When we perform an inner merge, we're selecting every row where a `Hotel Name` appears in *both* `hotels[cond1]` and `hotels[cond2]`. This is the same set of indices (and therefore hotel names, since those are unique) as where `(cond1 & cond2) == True`. So, the length of `combined` will be the same as the number of `True`s in `(cond1 & cond2)`.

2. When we perform an outer merge, we're selecting every row that appears in *either* DataFrame, although there will not be repeats for hotels that are both Marriott properties and are in Coronado. So, to find the total number of rows in either DataFrame, we take the sum of the sizes of each, and subtract rows that appear in both, which corresponds to answer `cond1.sum() + cond2.sum() - (cond1 & cond2).sum()`.

<average>79</average>

# END SOLUTION

# END SUBPROB

# END PROB




