# BEGIN PROB

Suppose the DataFrame `today` consists of 15 rows --- 3 rows for each of
5 different `"artist_names"`. For each artist, it contains the
`"track_name"` for their three most-streamed songs today. For instance,
there may be one row for `"olivia rodrigo"` and `"favorite crime"`, one
row for `"olivia rodrigo"` and `"drivers license"`, and one row for
`"olivia rodrigo"` and `"deja vu"`.

Another DataFrame, `genres`, is shown below in its entirety.

<center><img src='../assets/images/sp22-final/genres.png' width=35%></center>

# BEGIN SUBPROB

Suppose we perform an **inner** merge between `today` and
`genres` on `"artist_names"`. If the five `"artist_names"` in `today`
are the same as the five `"artist_names"` in `genres`, what fraction of
the rows in the merged DataFrame will contain `"Pop"` in the `"genre"`
column? Give your answer as a simplified fraction.

# BEGIN SOLN

**Answer: ** $\frac{2}{5}$

If the five `"artist_names"` in `today` and **genres** are the same, the
DataFrame that results from an inner merge will have 15 rows, one for
each row in `today`. This is because there are 3 matches for
`"harry styles"`, 3 matches for `"olivia rodrigo"`, 3 matches for
`"glass animals"`, and so on.

In the merged DataFrame's 15 rows, 6 of them will correspond to `"Pop"`
artists --- 3 to `"harry styles"` and 3 to `"olivia rodrigo"`. Thus, the
fraction of rows that contain `"Pop"` in the `"genre"` column is
$\frac{6}{15} = \frac{2}{5}$ (which is the fraction of rows that
contained `"Pop"` in `genres["genre"]`, too).

<average>97</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

Suppose we perform an **inner** merge between `today` and
`genres` on `"artist_names"`. Furthermore, suppose that the only
overlapping `"artist_names"` between `today` and `genres` are `"drake"`
and `"olivia rodrigo"`. What fraction of the rows in the merged
DataFrame will contain `"Pop"` in the `"genre"` column? Give your answer
as a simplified fraction.

# BEGIN SOLN

**Answer: ** $\frac{1}{2}$

If we perform an inner merge, there will only be 6 rows in the merged
DataFrame --- 3 for `"olivia rodrigo"` and 3 for `"drake"`. 3 of those 6
rows will have `"Pop"` in the `"genre"` column, hence the answer is
$\frac{3}{6} = \frac{1}{2}$.

<average>86</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

Suppose we perform an **outer** merge between `today` and
`genres` on `"artist_names"`. Furthermore, suppose that the only
overlapping `"artist_names"` between `today` and `genres` are `"drake"`
and `"olivia rodrigo"`. What fraction of the rows in the merged
DataFrame will contain `"Pop"` in the `"genre"` column? Give your answer
as a simplified fraction.

# BEGIN SOLN

**Answer: ** $\frac{2}{9}$

Since we are performing an outer merge, we can decompose the rows in the
merged DataFrame into three groups:

-   Rows that are in `today` that are not in `genres`. There are 9 of
    these (3 each for the 3 artists that are in `today` and not
    `genres`). `today` doesn't have a `"genre"` column, and so all of
    these `"genre"`s will be `NaN` upon merging.

-   Rows that are in `genres` that are not in `today`. There are 3 of
    these --- one for `"harry styles"`, one for `"glass animals"`, and
    one for `"doja cat"`. 1 of these 3 have `"Pop"` in the `"genre"`
    column.

-   Rows that are in both `today` and `genres`. There are 6 of these ---
    3 for `"olivia rodrigo"` and 3 for `"drake"` --- and 3 of those rows
    contain `"Pop"` in the `"genre"` column.

Tallying things up, we see that there are $9 + 3 + 6 = 18$ rows in the
merged DataFrame overall, of which $0 + 1 + 3 = 4$ have `"Pop"` in the
`"genre"` column. Hence, the relevant fraction is
$\frac{4}{18} = \frac{2}{9}$.

<average>29</average>

# END SOLN

# END SUBPROB

# END PROB