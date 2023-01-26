# BEGIN PROB

Define a `'personal'` task to be one whose category is not `'work'` or `'consulting'`.

Write a piece of code which adds a new column named `'personal'` to `'tasks'`. An entry of the column should be `True` if the task is a `'personal'` task, and `False` otherwise.

# BEGIN SOLN
**Answer: ** `tasks['personal'] = ~tasks['categorical'].isin(['work', 'consulting'])`

or

`tasks['personal'] = (tasks['Category'] != 'work') & (tasks['Category'] != 'consulting')`

Note that there are many different ways of doing this problem. The main idea however, is to check whether the category of each task was considered `'personal'` or not, and assign the appropriate boolean to the `'personal'` column of the given task.

<average>97</average>

# END SOLN

# END PROB