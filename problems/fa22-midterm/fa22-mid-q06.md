# BEGIN PROB

Suppose the date of each task has been collected in a Series named \python{dates}, shown below:

```py
>>> dates
7377   2019-08-31
7378   2019-08-31
7379   2019-09-01
7380   2019-09-02
7381   2019-09-02
            ...    
9831   2022-10-28
9832   2022-10-29
9833   2022-10-29
9834   2022-10-30
9835   2022-10-30
Length: 2459, dtype: datetime64[ns]
```

You may assume that the index of `dates` contains the task identifier, and that these identifiers correspond to the same identifiers used in the index of `tasks`. Note that dates have only been collected for the last 2459 tasks.

What will happen if we try to run the following line of code?

```py
tasks['date'] = dates
```

( ) A new row will be created with index "date".
( ) A new column will be created with missing values in the `'date'` column for tasks that are not in `dates`.
( ) An exception will be raised because some tasks are missing (the size of `dates` is not the same as the size of `tasks`.)
( ) An exception will be raised because `tasks` does not have a column named `'date'`.

# BEGIN SOLN

**Answer: ** Option B

Clearly Option A and D are both wrong so let's focus our attention to Option B and C. 

While C seems like a likely candidate, setting a column to a series of different lenght won't raise an exception, rather, python will simply assign the series and have missing values for tasks that are not in `dates`.

<average>57</average>

# END SOLN

# END PROB