# BEGIN PROB

The Earth Impact Database, curated by the University of New Brunswick's Planetary and Space Science Centre, contains information on almost 200 impact craters caused by meteorites that have crashed into the Earth.
In this question, assume you have access to a dataframe named `impacts`, shown below:

<center><img src='../assets/images/fa22-final/impacts.png' width=40%></center>

A short description of each column follows:
 - `crater_name`: the name of the impact crater.
 - `state`: if the crater is in the United States, the state containing the crater is listed here; otherwise,
    it is missing.
 - `country`: the country containing the crater.
 - `target_rock`: the type of rock that the crater is in.
 - `diameter_km`: the diameter of the crater in kilometers.
 - `drilled`: whether or not the crater has been drilled to analyze its contents.

# BEGIN SUBPROB

There are many missing values in the `state` column. Upon inspection, you find that a crater is missing a state if and only if the crater is not located in the United States. Note: while we're aware that upon inspection of the actual DataFrame, that this statement is clearly not true (such as Canada and Australia), we'll assume that the statement is true for the sake of the problem.

What is the most likely type of the missingness in the `state`column?

( ) Not Missing at Random (NMAR)
( ) Missing at Random (MAR)
( ) Missing Completely at Random (MCAR)
( ) Missing by Design (MD)

# BEGIN SOLN
**Answer: ** Option 4

The answer is Missing by Design becuase we can easily predict whether or not the `state` column will be missing based on the `country` column. Namely, if the `country` column is not 'United States', then we know that the `state` column is missing.

<average>72</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

Suppose we want to test the following hypotheses:

- Null Hypothesis: the crater diameter of impacts in sedimentary rock comes from the same distribution as the crater diameter of impacts in mixed rock.
- Alternative Hypothesis: the crater diameter of impacts in sedimentary rock is significantly larger on average.

When the distributions of crater diameter are plotted, we see the following:

<center><img src='../assets/images/fa22-final/distributions.png' width=40%></center>

Which one of the following is the best test statistic in this case?

( ) Total Variation Distance (TVD) between the distributions
( ) Kolmogorov-Smirnov (K-S) distance between the distributions
( ) the signed difference between the mean crater diameter of impacts in sedimentary rock, minus the mean crater diameter of impacts in mixed rock
( ) the unsigned (absolute) difference between the mean crater diameter of impacts in sedimentary rock, minus the mean crater diameter of impacts in mixed rock

# BEGIN SOLN
**Answer: ** Option C

K-S Statistic doesn't work well on discrete quantitative variables so we could rule that out. TVD is mainly used with categorical data so we could rule that out (and it's the absolute value so it wouldn't tell us whetehr or not one group is larger than the other group). We used the signed difference between mean crater diameter because we want to see whether or not one group is larger than the other, and unsigned difference between mean crater diameter wouldn't tell us anything about that.  

<average>56</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

Suppose it is observed that some values in the \python{diameter_km} column are missing. To determine if there is an association between this missingness and the values in the `country` column, a permutation test will be performed with the null hypothesis that the distribution of countries when the diameter is missing is the same as the distribution of countries when the diameter is not missing.

Which of the following test statistics should be used?

( ) the Total Variation Distance (TVD) between the distribution of countries when the diameter is missing and the distribution of countries when the diameter is not missing
( ) the Kolmogorov-Smirnov statistic between the distribution of countries when the diameter is missing and the distribution of countries when the diameter is not missing
( ) the signed difference between the mean crater diameter of impacts  where the country is missing, minus the mean crater diameter of impacts where the country is not missing
( ) the unsigned (absolute) difference between the mean crater diameter of impacts where the country is missing, minus the mean crater diameter of impacts where the country is not missing

# BEGIN SOLN
**Answer: ** Option A

Since 'countries' is a categorical variable, TVD would work the best here.

<average>70</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

Suppose the permutation test described in the previous problem fails to reject the null hypothesis. Assuming that NMAR and MD have been ruled out already, what can be said about the missingness in `diameter_km`?

( ) it is MCAR
( ) it is MAR
( ) We cannot say for sure without first testing for an association between the missingness and the other columns besides `country`.

# BEGIN SOLN
**Answer: ** Option C

In order to test whether or not a column is MCAR or MAR, we have to test the missingness of that column against ever other column in order to be conclusive about the missingness mechanism. Thus the answer is Option C.

<average>73</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

Suppose we fill in the missing values in the `diameter_km` column by random sampling. That is, for each missing diameter, we randomly sample from the the set of observed diameters. You may assume that these samples are drawn from the uniform distribution on observed diameters, and
that they are independent.

Assume that it is known that the missingness in the `diameter_km` column is MAR. Which of the following is true about the overall mean of the `diameter_km` column after imputation?

( ) It is likely to be an unbiased estimate of the true mean.
( ) It is likely to be a biased estimate of the true mean.

# BEGIN SOLN
**Answer: ** Option B

Since the missigness mechanism for `diameter_km` is MAR, we know that the missigness depends on some other bias from another column, implying the the observed values are inherently biased. Since we're drawing from a biased sample space, we conclude that we're likely to generate a biased estimate of the true mean.

<average>81</average>

# END SOLN

# END SUBPROB

# END PROB