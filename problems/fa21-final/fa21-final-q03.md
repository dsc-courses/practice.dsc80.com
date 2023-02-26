# BEGIN PROB

# BEGIN SUBPROB

You are creating a new programming language called IDK. In this language, all variable names must satisfy the following constraints:

- They must start with `Um`, `Umm`, `Ummm`, etc. That is, a capital `U` followed by one or more `m`'s.
- Following this may be any string of one or more letters. The first letter must be capitalized.
- The variable name must end with a single question mark.
- Numbers or other special characters are not allowed.

Examples of valid variable names: `UmmmX?`, `UmTest?`, `UmmmmPendingQueue?`
Examples of invalid variable names: `ummX?`, `Um?`, `Ummhello?`, `UmTest`

Write a regular expression pattern string `pat` to validate variable names in this new language. Your pattern should work when `re.match(pat, s)` is called.

# BEGIN SOLN

**Answer: ** `'U(m+)[A-Z]([A-z]*)(\?)'`

Starting our regular expression, it's not too difficult to see that we need a `'U'` followed by `(m+)` which will match with a singular capital `'U'` followed by at least one lowercase `'m'`. Next it is required that we follow that up with any string of letters, where the first letter is capitalized. we do this with `'[A-Z]([A-z]*)'`, where `'[A-Z]'` will match with any capital letter and `'([A-z]*)'` will match with lowercase and uppercase letters 0 or more times. Finally we end the regex with `'\?'` which matches with a question mark.

<average>87</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

Which of the following strings will be matched by the regex pattern `\$\s*\d{1,3}(\.\d{2})?`?  Note that it should match the complete string given. Mark all that apply.

[ ] $ 100
[ ] $10.12
[ ] $1340.89
[ ] $1456.8
[ ] $478.23
[ ] $.99

# BEGIN SOLN

**Answer: ** Option A, Option B and Option E

Let's dissect what the regex in the question actually means. First, the `'\$'` simply matches with any question mark. Next, `'\s*'` matches with whitespace characters 0 or more times, and `'\d{1,3}'` will match with any digits 1-3 times inclusive. Finally, `'(\.\d{2})?'` will match with any expression consisting of a period and any two digits following that period 0 or 1 times (due to the `'?'` mark). With those rules in mind, it's not too difficult to check that Options A, B and E work.

Options C, D and F don't work because none of those expressions have 1-3 digits before the period.

<average>83</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

"borough", "brough", and "burgh" are all common suffixes among English towns. Write a single regular expression pattern string `pat` that will match any town name ending with one of these suffixes. Your pattern should work when `re.match(pat, s)` is called.

# BEGIN SOLN

**Answer: ** `'(.*)((borough$)|(brough$)|(burgh$))'`

We will assume that the question wants us to create a regex that matches with any string that ends with the strings described in the problem. First, `'(.*)'` will match with anything 0 or more times at the start of the expression. Then `'((borough$)|(brough$)|(burgh$))'` will match with any of the described strings in the problem , since `'$'` indicates the end of string and `'|'` is just `or` in regex.

<average>82</average>

# END SOLN

# END SUBPROB

# END PROB