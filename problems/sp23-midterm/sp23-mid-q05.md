# BEGIN PROB

# BEGIN SUBPROB

You want to see if there is any relationship between the day of week
corresponding to the start times of the gaming sessions and the total
gameplay duration. Consider the following implementation with "groupby".

    games['Start dayofweek'] = pd.to_datetime(games['Start Time'])\
    .dt.dayofweek

    games.groupby('Start dayofweek').mean()['Total Duration']

Is there any opportunity for us to make the code execute faster? If yes,
how would you change the code? Please write the new implementation.

::: responsebox
1in
:::

# BEGIN SOLUTION

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

The "Break Duration" column has missing values. You ran the following
two cells.

![image](midterm_images/q5_part1.png){width="6in"}

Given the above information, what is the most likely missingness
mechanism?:\
( ) Missing at Random

( ) Not Missing at Random

( ) Missing by Design

( ) Missing Completely at Random

# BEGIN SOLUTION

# END SOLUTION

# END SUBPROB

# END PROB