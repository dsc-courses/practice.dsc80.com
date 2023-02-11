# BEGIN PROB

The code below creates a pivot table.

```py
pt = tasks.pivot_table(
    index='urgency', columns='category', values='completed', aggfunc='sum'
)
```

Which of the below snippets of code will produce the same result as `pt.loc[3.0, 'consulting']`? Select all that apply.

Snippet 1*:
```py
tasks[
    (tasks['category'] == 'consulting')
    &
    (tasks['urgency'] == 3.0)
]['completed'].sum()
```

Snippet 2*:
```py
tasks[tasks['urgency'] == 3]
.groupby('category')['completed']
.sum().loc['consulting']
```

Snippet 3:
```py
tasks.groupby('urgency')['completed']
.sum().loc[3.0, 'consulting']
```

Snippet 4*:
```py
tasks.groupby(['urgency', 'category'])['completed']
.sum().loc[(3.0, 'consulting')]
```

Snippet 5
```py
tasks.groupby('completed').sum().loc[(3.0, 'consulting')]
```

[ ] Snippet 1 
[ ] Snippet 2
[ ] Snippet 3
[ ] Snippet 4
[ ] Snippet 5

# BEGIN SOLN

**Answer: ** Option A, B and D

First let's consider what `pt.loc[3.0, 'consulting']` produces. Well `pt` is a table with urgency as its `'index'` and `'category'` as its columns. Each entry in the table is the number of completed task for each `'index'`, `'category'` pairing. Hence `pt.loc[3.0, 'consulting']` produces the number of completed tasks that are urgency level 3 and category consulting.

Snippet 1: This snippet works because it first querries for all tasks that are urgency 3 as well as category consulting. Then it calculates the number of completed tasks, which is what we wanted.

Snippet 2: This snippet works becuase it first querries for all the tasks that are urgency 3, then groups by category and aggregates the number of completed tasks for each category, and finally returns the number of completed tasks for the consulting category.

Snippet 3: This will not work because we are grouping by urgency and then selecting only the completed column to aggregate. (we are not grouping the categories in any way which is what we want to do in addition to grouping by urgency).

Snippet 4: This will work because we're grouping by both urgency and category, and aggregating the completed column by sum. This is just a different of writing the pivot_table.

Snippet 5: This will clearly not work because grouping by completed won't help us here.

<average>76</average>

# END SOLN

# END PROB