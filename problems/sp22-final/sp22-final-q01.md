# BEGIN PROB

\[(11 pts)\]

For each day in May 2022, the DataFrame `streams` contains the number of
streams for each of the "Top 200\" songs on Spotify that day --- that
is, the number of streams for the 200 songs with the most streams on
Spotify that day. The columns in `streams` are as follows:

-   `"date"`: the date the song was streamed

-   `"artist_names"`: name(s) of the artists who created the song

-   `"track_name"`: name of the song

-   `"streams"`: the number of times the song was streamed on Spotify
    that day

The first few rows of `streams` are shown below. Since there were 31
days in May and 200 songs per day, `streams` has 6200 rows in total.

<center><img src='../assets/images/sp22-final/streams.png' width=60%></center>

Note that:

-   `streams` is already sorted in a very particular way --- it is
    sorted by `"date"` in reverse chronological (decreasing) order, and,
    within each `"date"`, by `"streams"` in increasing order.

-   Many songs will appear multiple times in `streams`, because many
    songs were in the Top 200 on more than one day.

# BEGIN SUBPROB

(3 pts\*) Complete the implementation of the function `song_by_day`,
which takes in an integer `day` between 1 and 31 corresponding to a day
in May, and an integer `n`, and returns the song that had the `n`-th
most streams on `day`. For instance,\
`song_by_day(31, 199)` should evaluate to `"pepas"`, because `"pepas"`
was the 199th most streamed song on May 31st.

**Note:** You are not allowed to sort within `song_by_day` --- remember,
`streams` is already sorted.

    def song_by_day(day, n):
        day_str = f"2022-05-{str(day).zfill(2)}"
        day_only = streams[__(a)__].iloc[__(b)__]
        return __(c)__

What goes in blank (a)?

What goes in blank (b)?

What goes in blank (c)?

# BEGIN SOLN

**Answer: ** a) `streams['day'] == day_str`, b) `(200 - n)`, c) `day_only['track_name']`

The first line in the function gives us an idea that maybe later on in the function we're going to filter for all the days that match the given data. Indeed, in blank a, we filter for all the rows in which the `'day'` column matches `day_str`. In blank b, we could access directly access the row with the `n`-th most stream using iloc. (Remember, the image above shows us that the streams are sorted by most streamed in ascending order, so to find the `n`-th most popular song of a day, we simply do `200-n`). Finally, to return the track name, we could simply do `day_only['track_name']`.

<average>63</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

(3 pts\*) Below, we define a DataFrame `pivoted`.

    pivoted = streams.pivot_table(index="track_name", columns="date", 
                                  values="streams", aggfunc=np.max)

After defining `pivoted`, we define a Series `mystery` below.

    mystery = 31 - pivoted.apply(lambda s: s.isna().sum(), axis=1)

`mystery.loc["pepas"]` evaluates to 23. In one sentence, describe the
relationship between the number 23 and the song `"pepas"` in the context
of the `streams` dataset. For instance, a correctly formatted but
incorrect answer is "I listened to the song `"pepas"` 23 times today.\"

# BEGIN SOLN

**Answer: ** See below.

`pivoted.apply(lambda s: s.isna().sum(), axis=1)` computes the number of
days that a song was not on the Top 200, so
`31 - pivoted.apply(lambda s: s.isna().sum(), axis=1)` computes the
number of days the song was in the Top 200. As such, the correct
interpretation is that **`"pepas"` was in the Top 200 for 23 days in
May**.

<average>68</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

(2 pts\*) In defining `pivoted`, we set the keyword argument `aggfunc`
to `np.max`. Which of the following functions could we have used instead
of `np.max` without changing the values in `pivoted`? **Select all that
apply.**

[ ] `np.mean`
[ ] `np.median`
[ ] `len`
[ ] `lambda df: df.iloc[0]`
[ ] None of the above

# BEGIN SOLN

**Answer: ** Option 1, 2 and 4

For each combination of `"track_name"` and `"date"`, there is just a
single value --- the number of streams that song received on that date.
As such, the `aggfunc` needs to take in a Series containing a single
number and return that same number.

-   The mean and median of a Series containing a single number is equal
    to that number, so the first two options are correct.

-   The length of a Series containing a single number is 1, no matter
    what that number is, so the third option is not correct.

-   `lambda df: df.iloc[0]` takes in a Series and returns the first
    element in the Series, which is the only element in the Series. This
    option is correct as well. (The parameter name `df` is irrelevant.)

<average>80</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

(3 pts\*) Below, we define another DataFrame `another_mystery`.

    another_mystery = (streams.groupby("date").last()
                              .groupby(["artist_names", "track_name"])
                              .count().reset_index())

`another_mystery` has 5 rows. In one sentence, describe the significance
of the number 5 in the context of the `streams` dataset. For instance, a
correctly formatted but incorrect answer is "There are 5 unique artists
in `streams`.\" Your answer should not include the word "row\".

# BEGIN SOLN

**Answer: ** See below.

1in Since `streams` is sorted by `"date"` in descending order and,
within each `"date"`, by `"streams"` in ascending order,
`streams.groupby("date").last()` is a DataFrame containing the song with
the most `"streams"` on each day in May. In other words, we found the
"top song\" for each day. (The DataFrame we created has 31 rows.)

When we then execute `.groupby(["artist_names", "track_name"]).count()`,
we create one row for every unique combination of song and artist,
amongst the "top songs\". (If no two artists have a song with the same
name, this is the same as creating one row for every unique song.) Since
there are 5 rows in this new DataFrame (resetting the index doesn't do
anything here), it means that **there were only 5 unique songs that were
ever the "top song\" in a day in May**; this is the correct
interpretation.


<average>50</average>

# END SOLN

# END SUBPROB

# END PROB