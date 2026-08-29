# BEGIN PROB

The function `re.match(pat, s)` checks for the regular expression `pat` only at the beginning of string `s`. For example, `re.match("o", "hello")` does not find a match, but `re.match("h", "hello")` does.

# BEGIN SUBPROB

The string `"UC San Diego Health"` has exactly two lowercase `e`'s. Write a regular expression pattern, `pat`, so that `re.match(pat, s)` finds a match if and only if `s` has exactly two lowercase `e`'s. Write clearly!

# BEGIN SOLUTION

**Answer:** `pat = r"[^e]*e[^e]*e[^e]*$"`

The pattern requires exactly two lowercase `e`'s with any non-`e` characters (or none) between and around them, and `$` anchors the match to the end of the string.

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

ICD-10-CM codes (International Classification of Diseases, Tenth Revision, Clinical Modification) are codes used in the medical field to classify diagnoses, symptoms, and causes of death. Below are a few examples of ICD-10-CM codes and their associated meanings:

- J45.909: Unspecified asthma, uncomplicated
- F32.9: Major depressive disorder, single episode, unspecified
- G20: Parkinson's disease
- H43.391: Eye floaters, right eye
- S80.01XS: Contusion of right knee, initial encounter

ICD-10-CM codes consist of 3 to 8 characters following a certain format:

- Codes begin with a capital letter followed by two digits, which together specify the broad category of the medical condition.
- This may be followed by a decimal point and additional capital letters and numbers, which give more specific details about the medical condition.

Write a regular expression pattern, `pat`, so that `re.match(pat, s)` finds a match if and only if `s` is formatted like an ICD-10-CM code.

The following are some examples of incorrectly formatted codes that should **not** be matched.

- F27.
- TX3.120
- M27.56829
- L220.9

Write clearly!

# BEGIN SOLUTION

**Answer:** `pat = r"([A-Z]\d\d(\.[A-Z0-9]{1,4})?)$"`

The code starts with one capital letter and two digits. Optionally, a decimal point is followed by 1 to 4 alphanumeric characters. The `$` anchor ensures the entire string matches.

# END SOLUTION

# END SUBPROB

# END PROB
