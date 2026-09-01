# BEGIN PROB

The function `re.match(pat, s)` checks for the regular expression `pat` only at the beginning of string `s`. For example, `re.match("o", "hello")` does not find a match, but `re.match("h", "hello")` does.

# BEGIN SUBPROB

The string `"UC San Diego Health"` has exactly two lowercase `a`'s. Write a regular expression pattern, `pat`, so that `re.match(pat, s)` finds a match if and only if `s` has exactly two lowercase `a`'s. Write clearly!

# BEGIN SOLUTION

**Answer:** `pat = r"[^a]*a[^a]*a[^a]*$"`

The pattern matches strings with exactly two lowercase `a`'s from start to end:

- `[^a]*` — zero or more characters that are not lowercase `a`
- `a` — the first lowercase `a`
- `[^a]*` — zero or more non-`a` characters between the two `a`'s
- `a` — the second lowercase `a`
- `[^a]*$` — zero or more non-`a` characters until the end of the string

This allows any other characters (including uppercase letters) but requires exactly two lowercase `a`'s. For example, `"UC San Diego Health"` matches because it has two lowercase `a`'s and no others.

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

The pattern breaks down as follows:

- `[A-Z]\d\d` — one capital letter followed by exactly two digits (the required 3-character base code, e.g. `G20`)
- `(\.[A-Z0-9]{1,4})?` — optionally, a decimal point followed by 1 to 4 uppercase letters or digits (the extension, e.g. `.909` or `.01XS`)
- `$` — end of string, so nothing extra is allowed

This gives codes of length 3–8 and rejects invalid examples like `F27.` (trailing dot with no extension), `TX3.120` (two letters at the start), `M27.56829` (extension too long), and `L220.9` (three digits before the optional decimal).

# END SOLUTION

# END SUBPROB

# END PROB
