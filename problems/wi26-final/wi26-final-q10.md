# BEGIN PROB

Dr. Zheng and Dr. Golder are two medical doctors at UC San Diego Health. They each create a DataFrame of patients they have seen in the last year. Suppose that these DataFrames are called `dr_z` and `dr_g` and that each DataFrame includes a `"MRN"` column, which uniquely identifies patients.

Consider each of the following scenarios describing the overlap of `dr_z` and `dr_g`, and in each scenario, determine the number of rows in the DataFrame created by merging `dr_z` with `dr_g` using inner, outer, left, and right joins.

```py
dr_z.merge(dr_g, on="MRN", how=???)
```

# BEGIN SUBPROB

- `dr_z` has 100 rows, all representing distinct patients.
- `dr_g` has 80 rows, all representing distinct patients.
- 20 patients appear in both DataFrames.

1. `how = "inner"`:

2. `how = "outer"`:

3. `how = "left"`:

4. `how = "right"`:

# BEGIN SOLUTION

**Answers:** 20, 160, 100, 80

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

- `dr_z` has 50 rows, all representing distinct patients.
- `dr_g` has 15 rows, all representing distinct patients.
- All patients appearing in `dr_g` also appear in `dr_z`.

1. `how = "inner"`:

2. `how = "outer"`:

3. `how = "left"`:

4. `how = "right"`:

# BEGIN SOLUTION

**Answers:** 15, 50, 50, 15

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

- `dr_z` has 60 rows, representing 30 patients each appearing twice.
- `dr_g` has 80 rows, representing 40 patients each appearing twice.
- There are 10 patients that appear in both `dr_z` and `dr_g`.

1. `how = "inner"`:

2. `how = "outer"`:

3. `how = "left"`:

4. `how = "right"`:

# BEGIN SOLUTION

**Answers:** 40, 140, 80, 100

# END SOLUTION

# END SUBPROB

# END PROB
