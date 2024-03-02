# BEGIN PROB

# BEGIN SUBPROB

Consider a DataFrame `df` containing sales data for a company with the
following columns: `"Year"`, `"Month"`, `"Product"`, `"Region"`, and
`"Revenue"`. The `"Revenue"` column represents the sales revenue for
each product in a specific region during a particular month of a year.
You want to create a pivot table to summarize the total revenue for each
product in each year. Which of the following options correctly achieve
this? Select all that apply.

[ ]

        pd.pivot_table(df, values='Revenue', index='Product', 
        columns='Year', aggfunc=np.sum)

[ ]

        pd.pivot_table(df, values='Revenue', index=['Year', 'Product'], 
        columns='Region', aggfunc=np.sum)

[ ]

        pd.pivot_table(df, values='Revenue', index=['Product', 'Year'], 
        columns='Month', aggfunc=np.sum)

[ ]

        pd.pivot_table(df, values='Revenue', index='Year', 
        columns='Product', aggfunc=np.sum)

# BEGIN SOLUTION

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Let's consider the two DataFrames: `timeuse1` and `timeuse2`. Both
DataFrames have 10 rows in it.

![image](final_images/timeuse1.png){width="2.6in"}
![image](final_images/timeuse2.png){width="3.4in"}

`timeuse1``timeuse2`\
**1** The following code uses `pd.concat` to combine the two DataFrames.

        pd.concat([timeuse1.set_index('Country'), 
                timeuse2.set_index('Country_name')], axis=1)

How many NaN values would the resulting DataFame have?

**2** The following code uses `merge()` to combine two DataFrames.

        timeuse1.merge(timeuse2, left_on='Country', 
            right_on='Country_name', how='inner')

How many NaN values would the resulting DataFame have?

**3** What would the following code evaluate to?

        timeuse1.merge(timeuse2, left_on='Country', 
            right_on='Country_name', how='outer').shape[0]

# BEGIN SOLUTION

# END SOLUTION

# END SUBPROB

# END PROB