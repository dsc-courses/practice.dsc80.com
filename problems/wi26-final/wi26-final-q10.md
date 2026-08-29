# BEGIN PROB

Dr. Zheng and Dr. Golder are two medical doctors at UC San Diego Health. They each create a DataFrame of patients they have seen in the last year. Suppose that these DataFrames are called `dr_z` and `dr_g` and that each DataFrame includes a `"MRN"` column, which uniquely identifies patients.

Consider each of the following scenarios describing the overlap of `dr_z` and `dr_g`, and in each scenario, determine the number of rows in the DataFrame created by merging `dr_z` with `dr_g` using inner, outer, left, and right joins.

```py
dr_z.merge(dr_g, on="MRN", how=???)
```

# BEGIN SUBPROB

- `dr_z` has 90 rows, all representing distinct patients.
- `dr_g` has 70 rows, all representing distinct patients.
- 30 patients appear in both DataFrames.

1. `how = "inner"`:

2. `how = "outer"`:

3. `how = "left"`:

4. `how = "right"`:

# BEGIN SOLUTION

**Answers:**

1. 30
2. 130
3. 90
4. 70

Inner keeps only shared patients (30). Outer keeps all patients from both (90 + 70 − 30 = 130). Left keeps all 90 from `dr_z`. Right keeps all 70 from `dr_g`.

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

- `dr_z` has 20 rows, all representing distinct patients.
- `dr_g` has 65 rows, all representing distinct patients.
- All patients appearing in `dr_z` also appear in `dr_g`.

1. `how = "inner"`:

2. `how = "outer"`:

3. `how = "left"`:

4. `how = "right"`:

# BEGIN SOLUTION

**Answers:**

1. 20
2. 65
3. 20
4. 65

Every `dr_z` patient is in `dr_g`, so inner and left both have 20 rows. Outer and right include all 65 patients in `dr_g`.

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

**Answers:**

1. 40
2. 140
3. 80
4. 100

With duplicate rows, each shared patient contributes $2 \times 2 = 4$ rows to an inner join ($10 \times 4 = 40$). An outer join gives $60 + 80 - 40 = 140$ rows. A left join keeps all 60 `dr_z` rows (20 shared-patient rows each match 2 `dr_g` rows for 40 total, plus 40 `dr_z`-only rows). A right join keeps all 80 `dr_g` rows (20 shared-patient rows each match 2 `dr_z` rows for 40 total, plus 60 `dr_g`-only rows).

# END SOLUTION

# END SUBPROB

# END PROB
