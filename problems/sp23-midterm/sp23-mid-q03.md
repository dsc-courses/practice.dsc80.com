# BEGIN PROB

# BEGIN SUBPROB

JJ wants to know the average duration and average score of gaming
sessions for each gamer who has played at least 2 sessions. Can you help
to fill the missing pieces in the following code snippet so that `ans`
returns a DataFrame with two columns: `”Average Duration”` and
`”Average Score”`.

*Hint:* The first `groupby` indicates what name you should assign to the
new column and look carefully at one of the columns in the `games`.

    temp = games.assign(--(a)--).groupby('Gamer ID').--(b)--

    ans = temp.groupby('Gamer ID').--(c)--.rename( 
            columns={'Total Duration': 'Average Duration', 
                    'Score': 'Average Score'}
    )

What goes in (a)?

::: responsebox
0.75in
:::

What goes in (b)?

::: responsebox
0.75in
:::

What goes in (c)?

::: responsebox
0.75in
:::

# BEGIN SOLUTION

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

What is the total number of gaming sessions for each hour of the day,
and how does it vary between weekdays and weekends? Suppose Caicai wrote
these below:

    games['Hour'] = pd.to_datetime(games['Start Time']).dt.hour
    games['Day of Week'] = pd.to_datetime(
                            games['Start Time']
                        ).dt.day_name()
    tab = games.groupby(['Hour', 'Day of Week']
                            )['Gamer_Session ID'].count().unstack()

The `unstack()` method pivots a level of the (necessarily MultiIndex)
index labels. It returns a DataFrame having a new level of column labels
whose inner-most level consists of the pivoted index labels. An example
is provided below:

    >>> index = pd.MultiIndex.from_tuples([('one', 'a'), ('one', 'b'),
    ...                                    ('two', 'a'), ('two', 'b')])
    >>> s = pd.Series(np.arange(1.0, 5.0), index=index)
    >>> s
    one  a   1.0
         b   2.0
    two  a   3.0
         b   4.0
    dtype: float64
    >>> s.unstack()
         a   b
    one  1.0  2.0
    two  3.0  4.0

*Hint: When you `groupby` by two columns, you will get an MultiIndex
(covered in DSC10 and DSC80) as your index.*

Weiyue, on the other hand, prefers to use another method. Please
complete the code below so that `tab2` is the same as `tab`. (You may
assume that the first two lines written by Caicai have been executed.)
You **must** provide keyword arguments to receive credits.

    tab2 = games.pivot_table(--(a)--)

What goes in (a)?

::: responsebox
1in
:::

# BEGIN SOLUTION

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Continuing from part b, let us assume that both Caicai and Weiyue have
obtained the same dataframe. However, test-case enthusiast Lailai has
written the following test case and claimed that it failed.

        assert np.sum(tab.to_numpy() != tab2.to_numpy()) == 0

Weiyue, on the other hand, argues that failing the test case below does
not necessarily indicate that the results he and Caicai obtained are
different. Why is that? Provide your argument below, and make sure to
discuss what would you add to the end of both Caicai and Weiyue's
implementations to make this test case always pass when both of them
have gotten the same result.

::: responsebox
3in
:::

*Hint: Python's assert statement allows you to write test cases for your
code. In Python, assert is a simple statement with the following
syntax:*

        assert expression

*If any of your assertions turn false, then you have a bug in your code.
Here, expression can be any valid Python expression or object. If
expression is false, then the statement throws an AssertionError.*

# BEGIN SOLUTION

# END SOLUTION

# END SUBPROB

# END PROB