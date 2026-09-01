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

**Answer:** $w_3$

Changing the unit from seconds to minutes scales the appointment-time feature by a factor of 60. To produce the same predictions, $w_3$ must change (it becomes 60 times smaller). The other features are unchanged, so $w_0$, $w_1$, and $w_2$ do not need to change.

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Remove the intercept term $w_0$.

[ ] $w_1$
[ ] $w_2$
[ ] $w_3$

# BEGIN SOLUTION

**Answer:** $w_1$, $w_2$, and $w_3$

Removing the intercept forces the regression through the origin. The optimal slope coefficients generally all change when the intercept is removed, because the model can no longer shift predictions up or down independently of the features.

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Add a new feature, which is $3 \cdot \text{`"Age"`} + \text{`"NumProviders"`}$.

[ ] $w_0$
[ ] $w_1$
[ ] $w_2$
[ ] $w_3$

# BEGIN SOLUTION

**Answer:** $w_1$ and $w_2$

The new feature is a linear combination of `"Age"` and `"NumProviders"`, which introduces multicollinearity. There are many equivalent ways to distribute the effect across the old and new features, so $w_1$ and $w_2$ may change. $w_0$ and $w_3$ are not necessarily affected.

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

Adding a nonlinear combination of existing features changes the shape of the relationship the model can capture, so all coefficients in the fit model may change.

# END SOLUTION

# END SUBPROB

# END PROB
