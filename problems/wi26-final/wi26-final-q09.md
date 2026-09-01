# BEGIN PROB

Suppose we have access to another DataFrame that contains billing information. The rows are the same as in `med`, but there are only three columns, `"MRN"`, `"AppointmentTime"`, and `"Billed"`. The `"Billed"` column contains the amount that the patient was billed for their medical services at the time of the appointment.

# BEGIN SUBPROB

Suppose patients are billed for services at the time of their appointment, unless the services are very complex (such as a surgical procedure). For complex procedures, the `"Billed"` column is left empty, and patients are charged for services at a later date. In this scenario, what is the most likely missingness mechanism of the `"Billed"` column?

( ) missing by design (MD)
( ) missing not at random (MNAR)
( ) missing at random (MAR)
( ) missing completely at random (MCAR)

# BEGIN SOLUTION

**Answer:** missing not at random (MNAR)

Whether `"Billed"` is missing depends on the complexity of the procedure — information that is not recorded in the dataset. Since the missingness is related to an unobserved variable (procedure complexity), it is **MNAR**.

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Now suppose we merge the billing DataFrame with `med` on `"MRN"` and `"AppointmentTime"`.

We want to do a permutation test at the 0.05 significance level to decide if the missingness mechanism of the `"Billed"` column is more likely MCAR or MAR dependent on `"Department"`. Which of the following test statistics could be used for this permutation test? Select all that apply.

[ ] difference of means
[ ] absolute difference of means
[ ] total variation distance (TVD)
[ ] K-S statistic
[ ] none of these

# BEGIN SOLUTION

**Answer:** total variation distance (TVD)

To compare MCAR vs. MAR dependent on `"Department"`, we can compare the distribution of `"Department"` (or an indicator for missingness) across groups. **TVD** measures how different two distributions are and is appropriate for this kind of permutation test on categorical data, as discussed in the imputation and hypothesis testing lectures.

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Suppose the p-value comes out to 0.03. What can we conclude? Select all that apply.

[ ] The missingness mechanism is more likely MCAR than MAR.
[ ] The missingness mechanism is more likely MAR than MCAR.
[ ] The missingness mechanism is not MD.
[ ] The missingness mechanism is not MNAR.
[ ] None of the above is a valid conclusion.

# BEGIN SOLUTION

**Answer:** The missingness mechanism is more likely MAR than MCAR.

At the 0.05 significance level, a p-value of 0.03 provides evidence against the null hypothesis that missingness is MCAR. That suggests missingness is **more likely MAR than MCAR**. We cannot conclude anything about MD or MNAR from this test alone.

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Suppose additionally that on March 1, 2026, UC San Diego Health experienced a technical outage and all the billing data for that day was lost. Which imputation strategy is most appropriate if we want to make sure the mean and standard deviation don't change much as a result of the imputation?

( ) mean imputation
( ) probabilistic imputation
( ) mean imputation, conditional on `"Department"`
( ) probabilistic imputation, conditional on `"Department"`

# BEGIN SOLUTION

**Answer:** probabilistic imputation, conditional on `"Department"`

**Probabilistic imputation** samples from a distribution rather than filling every missing value with a single number, which better preserves variation in the data. Doing it **conditional on `"Department"`** accounts for differences in billing across departments. Plain mean imputation would collapse variance and distort the standard deviation.

# END SOLUTION

# END SUBPROB

# END PROB
