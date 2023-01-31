Welcome to the Midterm Exam for DSC 80 in Fall 2022!

Throughout this exam, we will be using to the following dataframe `tasks`.

<center><img src='../assets/images/fa22-midterm/tasks.png' width=35%></center>

Each row of this dataframe is a recorded task. The columns are as follows:

 - `'category'`: The category that the task falls into. E.g., `'work'`.
 - `'completed'`: Whether the task has been completed (`True`) or not (`False`).
 - `'minutes'`: The number of minutes that the task took to complete. Is always missing when the task was not completed, but can still be missing even if the task *was* completed.
 - `'urgency'`: A rating of the task's importance on a scale from 1 to 3, with 3 being the most important. Some values are missing.
 - `'client'`: Some of the tasks were performed as part of a consulting gig. If so, the client that the task was performed for is listed in this column. Missing values in this column are represented by the string `'n/a'`. You can assume that the client is missing if and only if the category is *not* consulting.

The table's index contains unique task identifiers, which are simply numbers. E.g., the first row's task identifier is simply ``0''.

To find out more about the data set, you have run `tasks.info(}` and performed `.value_counts()` on most columns. Here are the results:

```py
>>> tasks.info()
<class 'pandas.core.frame.DataFrame'>
Int64Index: 9836 entries, 0 to 9835
Data columns (total 5 columns):
 #   Column     Non-Null Count  Dtype  
---  ------     --------------  -----  
 0   category   9836 non-null   object 
 1   completed  9836 non-null   bool   
 2   minutes    6442 non-null   float64
 3   urgency    8864 non-null   float64
 4   client     1145 non-null   object 
dtypes: bool(1), float64(2), object(2)
memory usage: 393.8+ KB

>>> tasks["category"].value_counts(normalize=True)
work            0.562424
relationship    0.136539
consulting      0.116409
hobbies         0.091094
health          0.046157
finance         0.036702
learning        0.010675
Name: category, dtype: float64

>>> tasks["completed"].value_counts(normalize=True)
True     0.654941
False    0.345059
Name: completed, dtype: float64

>>> tasks["urgency"].value_counts(normalize=True)
2.0    0.502595
1.0    0.392825
3.0    0.104580
Name: urgency, dtype: float64

>>> tasks["client"].value_counts(normalize=True)
The Government of Luxembourg    0.224454
San Diego Financial Analysts    0.200873
ABC LLC                         0.196507
SDUSD                           0.191266
NASA                            0.186900
Name: client, dtype: float64
```