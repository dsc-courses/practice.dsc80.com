# BEGIN PROB

As a music enthusiast who checks Spotify's Top 200 daily, you have
noticed that many more songs from the "Hip-Hop/Rap\" genre were popular
in 2021 than were popular in years prior. You decide to investigate
whether this could have happened by chance, or if Hip-Hop/Rap is
actually becoming more popular.

You acquire ten DataFrames, one for each year between 2012 and 2021
(inclusive), containing the Top 200 songs on each day of each year. Each
DataFrame has four columns, `"year"`, `"artist_names"`, `"track_name"`,
and `"genre"`, and $365 \cdot 200 = 73000$ rows (or, in the case of leap
years 2012 and 2016, $366 \cdot 200 = 73200$ rows). You concatenate
these DataFrames into a big DataFrame called `all_years`.

To conduct a hypothesis test, you assume that all of the songs that were
ever in the Top 200 in a particular year are a sample of all popular
songs from that year. As such, `all_years` contains a sample of all
popular songs from 2012-2021. Your hypotheses are as follows:

-   **Null Hypothesis**: The number of unique Hip-Hop/Rap songs that
    were popular in 2021 is equal to the average number of unique
    Hip-Hop/Rap songs that were popular each year between 2012 and 2021
    (inclusive).

-   **Alternative Hypothesis:** The number of unique Hip-Hop/Rap songs
    that were popular in 2021 is greater than the average number of
    unique Hip-Hop/Rap songs that were popular each year between 2012
    and 2021 (inclusive).

To generate data under the null, you decide to treat the songs that were
in the Top 200 in 2021 as a random sample from the songs that were in
the Top 200 in all ten years. As your test statistic, you use the
**number of unique Hip-Hop/Rap songs** in your sample.

**Complete the implementation of the hypothesis test given on the next
page.**

**Note:** Remember that songs can appear multiple times in `all_years`
--- many songs appear in the Top 200 multiple times in the same year,
and some even appear in the Top 200 in different years. However, for the
purposes of this question, you can assume that no two different
`"artist_names"` have songs with the same `"track_name"`; that is, each
`"track_name"` belongs to a unique `"artist_names"`.

```py
all_years = # DataFrame that contains all 10 years' charts

# Helper function to compute the number of 
# unique Hip-Hop/Rap songs in a given DataFrame
def unique_rap(df):
    rap_only = df[df["genre"] == "Hip-Hop/Rap"]
    return rap_only.groupby(__(a)__).count()__(b)__[0]

count_2021 = unique_rap(all_years[all_years["year"] == 2021])
counts = np.array([])

for _ in range(10000):
    samp = all_years.sample(__(c)__, replace=True)
    counts = np.append(counts, unique_rap(samp))
    
p_val = (__(d)__).mean()
```
        

# BEGIN SUBPROB

What goes in blank (a)?

( ) `"year"`
( ) `"artist_names"`
( ) `"track_name"`
( ) `"genre"`

# BEGIN SOLN

**Answer: ** Option C: `"track_name"`

The first thing to notice is that first line in the function filters for all the rap songs in df. Next, since the helper function is supposed to return the number of unique Hip-Hop/Rap songs in a given DataFrame, we group by `"track_name"` so that each group/category is a unique song. Grouping by `"year"`, `"artist_names"`, or `"genre"` won't help us compute the number of unique songs. 

<average>89</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

What goes in blank (b)?

( ) `.shape`
( ) `.loc`
( ) `.iloc`
( ) Nothing (i.e. add `[0]` immediately after `.count()`)

# BEGIN SOLN

**Answer: ** Option A: `.shape`

Note that after grouping by `"track_name"`, each individual row in the resulting dataframe is a unique song within the rap genre. Thus the number of rows in the resulting dataframe is just the number of unique rap songs in a dataframe. To get the number of rows of a dataframe, we simply do `.shape[0]`

<average>89</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

What goes in blank (c)?

( ) `count_2021.shape[0]`
( ) `200`
( ) `365`
( ) `200 * 365`

# BEGIN SOLN

**Answer: ** Option D: `200 * 365`

Consider the following statement from the problem: "To generate data under the null, you decide to treat the songs that were in the Top 200 in 2021 as a random sample from the songs that were in the Top 200 in all ten years." Thus it follows that we need to generate `200 * 365` songs since there are `200 * 365` songs in the Top 200 in 2021. 

Alternatively, it makes sense to sample `200 * 365` songs from `all_years` because we use the number of unique rap songs as a test statistic for each sample. Thus our sample should be the same size as the number of songs in the Top 200 in 2021.

<average>52</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

What goes in blank (d)?

# BEGIN SOLN

**Answer: ** `(counts >= count_2021)`

Note that `counts` is a np.array that contains the number of Rap songs from each sample. Because our alternative hypothesis is that "The number of unique Hip-Hop/Rap songs that were popular in 2021 is greater than the average number of unique Hip-Hop/Rap songs that were popular each year between 2012 and 2021", simply doing `(counts < count_2021)` will return an array of booleans denoting whether or not `count_2021` was greater than the number of rap songs in each sample. The `.mean()` will simply compute the appropriate proportion, or p-value. 

<average>53</average>

# END SOLN

# END SUBPROB

# END PROB