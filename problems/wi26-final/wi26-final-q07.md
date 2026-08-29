# BEGIN PROB

Suppose we derive a numerical feature `"AppointmentTimeSeconds"` which measures the `"AppointmentTime"` in seconds since midnight. Then we use linear regression to fit a prediction rule of the form:

$$\text{predicted `"WaitTime"'} = w_0 + w_1 \cdot \text{`"Age"`} + w_2 \cdot \text{`"NumProviders"`} + w_3 \cdot \text{`"AppointmentTimeSeconds"`}$$

Consider each of the following changes to the model above, and determine which coefficients in the fit model **may change**. Select all coefficients that may change. Note that we are changing the original model each time, not stacking changes on top of one another.

# BEGIN SUBPROB

Change `"AppointmentTimeSeconds"` to `"AppointmentTimeMinutes"`, which is measured in minutes since midnight.

[ ] $w_0$
[ ] $w_1$
[ ] $w_2$
[ ] $w_3$

# BEGIN SOLUTION

**Answer:** $w_0$ and $w_3$

Scaling `"AppointmentTimeSeconds"` to minutes scales that feature by a factor of 60, which changes $w_3$ (and typically $w_0$ to preserve predictions). $w_1$ and $w_2$ are unchanged because their features are unaffected.

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Add a new feature, which is $3 \cdot \text{`"Age"`} + \text{`"NumProviders"`}$.

[ ] $w_0$
[ ] $w_1$
[ ] $w_2$
[ ] $w_3$

# BEGIN SOLUTION

**Answer:** $w_0$, $w_1$, $w_2$, and $w_3$

Adding a new feature that is a linear combination of existing features introduces multicollinearity, so all coefficients may change.

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Add a new feature, which is `"Age"/"NumProviders"`.

[ ] $w_0$
[ ] $w_1$
[ ] $w_2$
[ ] $w_3$

# BEGIN SOLUTION

**Answer:** $w_0$, $w_1$, $w_2$, and $w_3$

Adding a nonlinear combination of existing features can change the optimal fit for all coefficients.

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Remove the intercept term $w_0$.

[ ] $w_1$
[ ] $w_2$
[ ] $w_3$

# BEGIN SOLUTION

**Answer:** $w_1$, $w_2$, and $w_3$

Removing the intercept forces the regression through the origin, which generally changes all remaining slope coefficients.

# END SOLUTION

# END SUBPROB

# END PROB
