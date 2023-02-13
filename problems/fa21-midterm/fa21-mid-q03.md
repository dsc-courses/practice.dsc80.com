# BEGIN PROB

The code below produces a new table. How many **rows** will the table have? (See the data set description above for useful information).

```py
df.groupby('Species')['Culmen Length (mm)'].aggregate([np.mean, np.median])
```
# BEGIN SOLN
**Answer: ** 3

We're grouping the dataset by `"Species"`, so our resulting table will have 3 rows since there are 3 unique species in the dataset. Note that aggregating by multiple functions won't affect the number of rows in the output dataset, rather it will change the number of columns in the resulting table.

<average>94</average>

# END SOLN

# END PROB