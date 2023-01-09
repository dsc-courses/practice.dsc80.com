# BEGIN PROB

Fill in the blank so that the result evaluates to a Series indexed by
`"Email"` that contains a **list** of the universities that each student
**was admitted to**. If a student wasn't admitted to any universities,
they should have an empty list.

```py
    students.groupby("Email").apply(_____)
```

What goes in the blank?

# BEGIN SOLN

**Answer: ** `lambda df: df.loc[df["Admit"] == "Y", "University"].tolist()`

<average>53</average>

# END SOLN

# END PROB