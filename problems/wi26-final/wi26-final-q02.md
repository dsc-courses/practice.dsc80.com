# BEGIN PROB

Doctors love having letters after their names! These letters usually represent degrees, titles, or certifications. We'll refer to them collectively as **credentials**. In the `"Provider"` column of `med`, each provider has at least one credential. Credentials appear after the name and are separated by commas. For example, the preview of `med` shows that Dr. Takashi Hirase has two credentials (MD and MPH).

# BEGIN SUBPROB

Write **one line** of code that evaluates to a Series containing the number of credentials for each provider in the `"Provider"` column of `med`. You **must** use `.split()` and you may **not** define any lambda functions.

# BEGIN SOLUTION

**Answer:** `med["Provider"].str.split(", ").apply(len) - 1`

Each credential after the provider's name is preceded by `", "`. Splitting on `", "` gives one more piece than the number of credentials (the provider's name is the first piece). Subtracting 1 gives the credential count. For example, `"Takashi Hirase, MD, MPH"` splits into 3 pieces, so there are 2 credentials.

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Write a different **single line** of code that evaluates to the same Series. This time, you may **not** use `.split()` and you may **not** define any lambda functions.

# BEGIN SOLUTION

**Answer:** `med["Provider"].str.count(", ")`

Each credential beyond the first adds exactly one `", "` to the string, so counting occurrences of `", "` gives the number of credentials directly.

# END SOLUTION

# END SUBPROB

Finally, we'll add this Series to `med` as a new column called `"Credentials"`. This column is included in `med` for the rest of the exam.

# END PROB
