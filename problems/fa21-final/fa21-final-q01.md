# BEGIN PROB

This table below contains energy usage information for every building owned and managed by the New York City Department of Citywide Administrative Services (DCAS). DCAS is the arm of the New York City municipal government which handles ownership and management of the city's office facilities and real estate inventory. The organization voluntarily publicly discloses self-measured information about the energy use of its buildings.

<center><img src='../assets/images/fa21-final/table.png' width=30%></center>

Assume that the table has been read into the variable named `df`. The result of `df.info()` is shown below:

<center><img src='../assets/images/fa21-final/info.png' width=30%></center>

# BEGIN SUBPROB

Write a piece of code that computes the name of the borough whose median building energy usage is the highest.

Note: your code will be graded manually, and it is not expected to be perfect. Be careful to not spend too much time trying to make your code perfect!

# BEGIN SOLN
**Answer: ** `df.groupby('Borough')['Energy'].median().idxmax()`

The idea is to perform a groupby and get the median within each group and then somehow get the group with the largest median.

<average>91</average>

# END SOLN

# BEGIN SUBPROB

Write a line of code to normalize the building addresses. To normalize an address, replace all spaces with underscores, change "Street" to "St", change "Avenue" to "Av", and convert to lower case. Your code should evaluate to a series containing the normalized addresses.

# BEGIN SOLN
**Answer: ** `df['Building Addresss'].apply(lambda x: x.replace(' ', '_').replace('Avenue', 'Av').replace('Street', 'St').lower())`

<average>90</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

From the table above, it looks like it is common for city buildings to have addresses that start with the number '1'; e.g., "100 Centre Street". Write a piece of code that plots a histogram showing the number of times each number appears as the first number in an address.

# BEGIN SOLN
**Answer: ** `df['Building Addresss'].apply(lambda x: int(x[0])).plot(kind = 'hist')`

The apply part of the code gets the first number of each address, and then plots the resulting Series as a histogram.

<average>90</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

Suppose the following code is run:

```py
from sklearn.preprocessing import OneHotEncoder
oh = OneHotEncoder()
oh.fit_transform(df[['Borough']]).mean(axis=0)
```

What will be the result?

( ) An array of size 5 containing the proportion of buildings in each of the five boroughs.
( ) An array with as many entries as there are buildings containing 0.2 in each spot.
( ) An array of size 5 containing all zeros.
( ) An array of size 5 containing one 1 and the rest zeros.

# BEGIN SOLN
**Answer: ** Option A

One-Hot-Encoding will create 5 columns representing each 'Borough'. For each building, a 1 will be filled in the column of the 'Borough' in which the building belongs to, and 0 for the other 4 columns. Thus taking the mean of each of the 5 'Borough' columns will just produce the proportion of buildings in each of the 5 boroughs, yielding Option A.

<average>90</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

Write a piece of code (perhaps more than one line) that computes the proportion of addresses in each borough that end with either `St` or `Street`.

# BEGIN SOLN
**Answer: ** 

```py
def match(x):
    return (x.endswith('St')) | (x.endswith('Street'))

df['Building Address'] = df['Building Address'].apply(lambda x: match(x))
df.groupby('Borough')['Building Address'].mean()
```
<average>79</average>

# END SOLN

# END SUBPROB

# END PROB