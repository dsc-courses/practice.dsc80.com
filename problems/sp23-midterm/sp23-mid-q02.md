# BEGIN PROB

# BEGIN SUBPROB

Which expression will evaluate to a Series containing the name of the
most popular gaming platform for each skill level.

( ) Code Snippet 1:

    demo.groupby('Skill Level')['Gaming Platform'].value_counts()

( ) Code Snippet 2:

    demo.groupby('Skill Level')['Gaming Platform']\
        .agg(lambda x: x.value_counts().index[0])

( ) Code Snippet 3:

    demo.groupby('Gaming Platform')['Skill Level']\
        .agg(lambda x: x.value_counts().index[0])

( ) Code Snippet 4:

    demo[['Skill Level','Gaming Platform']].value_counts().idxmax()

# BEGIN SOLUTION

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

What will be the **type** of the objects returned by the following
lines? Note that if the object is a collection of elements, like a
Series or DataFrame, give the type of the collection, not the type of
the elements it contains!

Possible choices for the following boxes: `pd.DataFrame`, `pd.Series`,
`int`, `float`

  -------------------------------------- --
    `games[[‘Break Duration’, ‘Score’]]` 
        `games.loc[2][‘Total Duration’]` 
               `games[games.columns[5]]` 
                        `games.iloc[-3]` 
  -------------------------------------- --

# BEGIN SOLUTION

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Let's say you wanted to count the number of married gamers in the `demo`
dataset. Since married gamers are denoted by an `‘M’` in the
`Marital Status` column, you write this code:

    counter = 0
    for i in range(len(demo)):
        if demo.iloc[i]["Marital Status"] == 'M':
            counter = counter + 1

For loops are a bad idea to use with `pandas` objects, because they are
not vectorized and are therefore much slower than using
`pandas/numpy`-native functions. What is a one-line solution you could
use instead to retrieve the same value?

::: responsebox
1in
:::

# BEGIN SOLUTION

# END SOLUTION

# END SUBPROB

# END PROB