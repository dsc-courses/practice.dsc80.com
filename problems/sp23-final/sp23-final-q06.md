# BEGIN PROB

In this question, we will work with a publicly available forest fire dataset. A preview of the `forest` DataFrame is provided below, along with a description of the column names.

`forest` Dataframe:
<center><img  src='../assets/images/sp23-final/q6.png'  width=40%> </center>

`"month"` - month of the year: jan to dec
`"day"` - day of the week: mon to sun
`"temp"` - temperature in Celsius degrees: 2.2 to 33.30
`"RH"` - relative humidity in percentage: 15.0 to 100
`"wind"` - wind speed in km/h: 0.40 to 9.40
`"rain"` - outside rain in mm/m2 : 0.0 to 6.4
`"area"` - the burned area of the forest in logarithmic scale
`"is_julaugsep"` - whether the forest fire event happened in the months of July, August, or September.

# BEGIN SUBPROB

Alex wants to explore if there is any statistically significant relationship between the burned area of the forest `"area"` and the `"is_julaugsep"` variable. At first, he plots the two probability distributions (as shown in the figure below):

<center><img  src='../assets/images/sp23-final/q6_density.png'  width=40%> </center>

Alex decides to perform a permutation test with the following hypotheses.

-  **Null Hypothesis**: The burned area for forest fire events in the July-Aug-Sep months are drawn from the same distribution as the burned area for forest fire events in the rest of the year. Any observed differences are due to random chance.

-  **Alternative Hypothesis**: The forest fire events in the July-Aug-Sep months has lower average burned area than the forest fire events in the rest of the year.

Which one of the following is the best test statistic in this case?

( ) Total Variation Distance (TVD) between the distributions
( ) Kolmogorov-Smirnov (K-S) distance between the distributions
( ) The signed difference between the mean burned area of Non-July-Aug-Sep months, minus the mean burned area of July-Aug-Sep months
( ) The unsigned (absolute) difference between the mean burned area of Non-July-Aug-Sep months, minus the mean burned area of July-Aug-Sep months

# BEGIN SOLN
**Answer:** C - The signed difference between the mean burned area of Non-July-Aug-Sep months, minus the mean burned area of July-Aug-Sep months.

Since the two distributions here are numerical (burned areas is numerical), and the shapes of the distributions 
are similar (based on the the probability density plot), we should use the signed difference in means as the test statistic.

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

Hasan noticed some missing data in the `"temp"` column. After talking to Prof. Ana who lead the data collection efforts, Hasan came to know that the temperature sensor had to be taken down and re-calibrated in some of the high temperature days which resulted in missing values. what can be said about the missingness in the `"temp"` column?

( ) Missing Completely at Random
( ) Not Missing at Random
( ) Missing at Random
( ) Missing by Design

# BEGIN SOLN
**Answer:** Not Missing at Random

The `"temp"` column is missing if its own value is too high. Since missingness depends on itself, it is NMAR.

# END SOLN

# END SUBPROB
 
# BEGIN SUBPROB

Now, Hasan wants to fill in the missing values in the `"temp"` column. Which data imputation strategy is most appropriate here?

( ) Data imputation by random sampling where we randomly sample one value from the observed values in the `"temp"` column for each missing values in the same column
( ) Mean imputation where we replace the missing value by mean of the observed values in `"temp"` column
( ) Conditional mean imputation based on `"is_julaugsep"` column
( ) Data imputation can not be performed based on the `forest` dataframe

# BEGIN SOLN
**Answer:** D - Data imputation can not be performed based on the `forest` dataframe.

Since the missing value depends on itself (NMAR), there is no other data in `forest` that can be used for imputation.

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

Mark, at first, trains a linear regression model with `"temp"` and `"RH"` columns to predict `"area"`. Later, Mark identifies that dew point temperature `"Td"` is an informative feature for predicting `"area"`. He adds a new column to the `forest` Dataframe called `"Td"` where Td can be expressed by the following equation: $Td = temp - \frac{100-RH}{5}$. Lastly, Mark trains a second linear regression model with `"temp"`, `"RH"`, `"Td"` columns in order to predict `"area"`. Based on this, what can be said about the second model?

[ ] The accuracy of the second model is likely to be lower than the first one.
[ ] The coefficient of the second model can not be interpreted.
[ ] The performance (e.g., rmse or R2 value) of the second model will be the same as the first one.
[ ] The first linear regression model suffers from 'Multicollinearity'

# BEGIN SOLN
**Answer:** Options 2 and 3.

Because the variable `Td` is derived form a linear combination of the features 
`temp` and `RH`, the second model will have multicollinearity. This means that 
although the performance of the second model will be the same as that of the first, 
the coefficients of the second model cannot be interpreted, unlike in the first model.

Therefore the correct answers are options 2 and 3.

# END SOLN

# END SUBPROB

# END PROB