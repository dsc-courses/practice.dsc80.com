# BEGIN PROB

 Suppose we derive a numerical feature
`"AppointmentTimeSeconds"` which measures the\
`"AppointmentTime"` in seconds since midnight. Then we use linear
regression to fit a prediction rule of the form:
$$\text{predicted }\texttt{"WaitTime"} = w_0 + w_1\cdot\texttt{"Age"} + w_2\cdot\texttt{"NumProviders"} + w_3\cdot\texttt{"AppointmentTimeSeconds"}$$

Consider each of the following changes to the model above, and determine
which coefficients in the fit model may change. **Select all**
coefficients that may change. Note that we are changing the original
model each time, not stacking changes on top of one another.

# BEGIN SUBPROB

Change `"AppointmentTimeSeconds"` to `"AppointmentTimeMinutes"`, which
is measured in minutes since midnight.

[ ] $w_0$
[ ] $w_1$
[ ] $w_2$
[ ] $w_3$

# BEGIN SOLUTION

**Answer:** $w_3$

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Remove the intercept term $w_0$.

[ ] $w_1$
[ ] $w_2$
[ ] $w_3$

# BEGIN SOLUTION

**Answer:** $w_1$, $w_2$, $w_3$

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Add a new feature, which is
$3\cdot\texttt{"Age"}+\texttt{"NumProviders"}$.

[ ] $w_0$
[ ] $w_1$
[ ] $w_2$
[ ] $w_3$

# BEGIN SOLUTION

**Answer:** $w_1$, $w_2$

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Add a new feature, which is $\texttt{"Age"}/\texttt{"NumProviders"}$.

[ ] $w_0$
[ ] $w_1$
[ ] $w_2$
[ ] $w_3$

# BEGIN SOLUTION

**Answer:** $w_0$, $w_1$, $w_2$, $w_3$

# END SOLUTION

# END SUBPROB

# END PROB