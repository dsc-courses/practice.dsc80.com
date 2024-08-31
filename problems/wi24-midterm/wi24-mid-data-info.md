In this exam, we'll work with the DataFrame `dogs`, which contains one row for every registered pet dog in Zurich, Switzerland in 2017.

The first few rows of `dogs` are shown below, but `dogs` has many more rows than are shown.

<center><img src="../../assets/images/wi24-midterm/df.png" width=750></center>

<br>

- `"owner_id" (int)`: A unique ID for each owner. Note that, for example, there are two rows in the preview for `4215`, meaning that owner has at least 2 dogs. **Assume that if an `"owner_id"` appears in `dogs` multiple times, the corresponding `"owner_age"`, `"owner_sex"`, and `"district"` are always the same.**
- `"owner_age" (str)`: The age group of the owner; either `"11-20"`, `"21-30"`, ..., or `"91-100"` (9 possibilities in total).
- `"owner_sex" (str)`: The birth sex of the owner; either `"m"` (male) or `"f"` (female).
- `"district" (int)`: The city district the owner lives in; a positive integer between `1` and `12` (inclusive).
- `"primary_breed" (str)`: The primary breed of the dog.
- `"secondary_breed" (str)`: The secondary breed of the dog. If this column is not null, the dog is a "mixed breed" dog; otherwise, the dog is a "purebred" dog.
- `"dog_sex" (str)`: The birth sex of the dog; either `"m"` (male) or `"f"` (female).
- `"birth_year" (int)`: The birth year of the dog.

**Throughout the exam, assume we have already run `import pandas as pd` and `import numpy as np`.**