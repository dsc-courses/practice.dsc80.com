# BEGIN PROB

Suppose you have created a new table `by_size` which lists each penguin's size as either "small", "medium", or "large". The species is also included. The table looks like this:

<center><img src='../assets/images/fa21-midterm/sizes.png' width=25%></center>


Using the code `by_size.pivot_table(index='species', columns='size?', aggfunc='size')`, you've created the pivot table shown below:

<center><img src='../assets/images/fa21-midterm/size-pivot.png' width=30%></center>

There is a `NaN` in this pivot table. Why?

( ) some Gentoo penguins had sizes that were `NaN`
( ) some Gentoo penguins had sizes that were not strings
( ) there were too many small Gentoo penguins for the computer to represent with finite precision
( ) there were no small Gentoo penguins

# BEGIN SOLN
**Answer: ** Option D

We can think of a pivot table as a fancy reorganized group by that just lists every combination pair of 'species' and 'size'. Now the reason why'd there be a `NaN` in the pivot table is because there are no small Gentoo penguins. The reason this is `NaN`, rather than some other value (like 0) makes more sense if we consider it through the lens of a group by. In a group by, when we group by `species` and `size` and aggregate by some function, we get some value associated with each group PRESENT in the DataFrame. In group by, when a group doesn't exist, it simply doesn't show up (instead of having 0 as a value for instance). Thus the answer is D.

<average>95</average>

# END SOLN

# END PROB