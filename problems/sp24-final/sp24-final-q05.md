# BEGIN PROB

Suppose you define a DataFrame `t` as follows:

```python
t = (survey.merge(df, on='id', suffixes=('', '2'))
     .assign(is_ca=t['state'] == 'California',
             is_boot=t['cat'] == 'BOOT',
             is_tool=t['cat'] == 'TOOLS'))
```

The first few rows of `t` are shown below:

<center><img src="../../assets/images/sp24-final/t.png" style="width: 100%; height: auto;"></center>



For each pivot table below, state whether it is **possible** to observe Simpson's paradox without any extra information about the data.


# BEGIN SUBPROB

Pivot table:

```python
t.pivot_table(
    index='is_ca',
    columns='is_boot',
    values='cost',
    aggfunc='count',
)
```

( ) Yes  
( ) No  
( ) Need more information to determine

# BEGIN SOLN

**Answer:** No

# END SOLN

# END SUBPROB



# BEGIN SUBPROB

Pivot table:

```python
t.pivot_table(
    index='is_ca',
    columns='is_tool',
    values='cost',
    aggfunc='mean',
)
```

( ) Yes  
( ) No  
( ) Need more information to determine

# BEGIN SOLN

**Answer:** Yes

# END SOLN

# END SUBPROB


# END PROB