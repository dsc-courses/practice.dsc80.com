# BEGIN PROB

# BEGIN SUBPROB

Only one of the following variables is of a numerical feature type; the
rest are categorical. Which one is it?

( ) `"owner_id"`
( ) `"owner_age"`
( ) `"district"`
( ) `"dog_sex"`
( ) `"birth_year"`       

# BEGIN SOLUTION

**Answer**: `"birth_year"`

Some of the other columns may be stored as numbers, like `'"district"`, but they are not numerical – you can't do arithmetic with them. `"birth_year"` is the only column on which arithmetic operations are well-defined, making it numerical.

Many students answered `"owner_age"`, but the values in `"owner_age"` are age categories, not actual ages. `"district"` is incorrect because districts are nominal categories, like phone numbers, zip codes, and Social Security Numbers.

<average>76</average>

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Suppose `"21-30"` is the most common value in the `"owner_age"` column.
Just for this part, suppose we also have access to a `"owner_age_years"`
column that contains the actual age of each owner in years, e.g. `36`
instead of `"31-40"`.

True or False: The most common value in the `"owner_age_years"` column
must be between `21` and `30`, inclusive.

( ) True
( ) False

# BEGIN SOLUTION

**Answer**: It could be the case that 21-30 is the most common age category, but 33 is the single most common age. What if everyone in the 31-40 age category is aged 33, but everyone in the 21-30 age category is "spaced out"?

<average>71</average>

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Fill in the blank so that `most_common` evaluates to the most common
district in `dogs`. Assume there are no ties.

```py
most_common = ____
```

# BEGIN SOLUTION

**Answer**:

```py
dogs["district"].value_counts().idxmax()
```

Above, we presented one possible solution, but there are many:

- `dogs["district"].value_counts().idxmax()`
- `dogs["district"].value_counts().index[0]`
- `dogs.groupby("district").size().sort_values(ascending=False).index[0]`
- `dogs.groupby("district").count()["owner_id"].sort_values(ascending=False).index[0]`

<average>72</average>

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Fill in the blank so that `female_breeds` evaluates to a Series
containing the primary breeds of all female dogs.

```py
female_breeds = dogs.____
```

# BEGIN SOLUTION

**Answer**:

```py
loc[dogs["dog_sex"] == "f", "primary_breed"]
```

Another possible answer is:

```py
query("dog_sex == 'f'")["primary_breed"]`

Note that the question _didn't_ ask for unique primary breeds.

<average>79</average>

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Fill in the blank so that `midpoints` evaluates to a Series that contains the midpoint of each dog owner's age group as a float. For example, the midpoint of the age group `"51-60"` is `55.5`. Your answer must fit on one line, and cannot use the `def` keyword.

```py
midpoints = dogs["owner_age"].____
```

# BEGIN SOLUTION

**Answer**: 

```py
str.split("-").str[0].astype(float) + 4.5
```

There are many possible solutions. Many students tried to average the two numbers, which is correct:

```py
apply(lambda x: 0.5 * (int(x.split("-")[0]) + int(x.split("-")[1])))
```

However, we thought it's much easier to just add 4.5 to the first number (which is what the "answer" presented does), or even concatenate the first digit with the string "5.5" – these are all equivalent to the midpoint.

<average>68</average>

# END SOLUTION

# END SUBPROB

# END PROB