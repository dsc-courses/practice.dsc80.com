# BEGIN PROB

In the next 6 questions, you will be asked to determine which strings are matched by various regular expression patterns when `re.search` is used. For these questions, remember that `re.search(pattern, s)` matches `s` if the pattern can be found anywhere in `s` (not necessarily at the beginning). For example, `re.search("name", "my name is justin")` matches, while `re.search("foo", "my name is justin")` does not.

# BEGIN SUBPROB
Which of the below strings are matched by `re.search` using the pattern `'a+'`?
Select all that apply.

[ ] `"aa bb cc"`
[ ] `"aaa bbb ccc"`
[ ] `"abaaba"`
[ ] `"abacaba"`

# BEGIN SOLN
**Answer: Option A, B, C and D

The regex pattern `'a+'` searches for any string that contains at least one substring consisting of the character `a` one or more times. Clearly all of these strings contain a substring og the character `a` one or more times.

<average>98</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

Which of the below strings are matched by `re.search` using the pattern `'a+ b+'`?
Select all that apply.

[ ] `"aa bb cc"`
[ ] `"aaa bbb ccc"`
[ ] `"abaaba"`
[ ] `"abacaba"`

# BEGIN SOLN
**Answer: Option A and B

The regex pattern `'a+ b+'` searches for any string that contains at least one substring consisting of the character `a` one or more times followed by a space followed by the character `b` one or more times. The only strings that have this pattern are Options A and B.

<average>95</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

Which of the below strings are matched by `re.search` using the pattern `'\baa\b'`

Recall that the `r` at the front of the pattern string above makes it a "raw" string; this is used so that `\b` is not interpreted by Python as a special backspace character.

Select all that apply.

[ ] `"aa bb cc"`
[ ] `"aaa bbb ccc"`
[ ] `"abaaba"`
[ ] `"abacaba"`

# BEGIN SOLN
**Answer: Option A

The regex pattern `'\b'` matches for the boundary of a word (so like the start and end of a word which could seperated by spaces). Thus the regex pattern searches for the substring `'aa'` that is its own standalone word. The only string that has this pattern is Option A.

<average>75</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

Which of the below strings are matched by `re.search` using the pattern `'(aba){2,}'`?
Select all that apply.

[ ] `"aa bb cc"`
[ ] `"aaa bbb ccc"`
[ ] `"abaaba"`
[ ] `"abacaba"`

# BEGIN SOLN
**Answer: Option C

The regex pattern `'(aba){2,}'` searches the substring consisting of `aba` 2 or more times. The only string that has this pattern is Option C.

<average>97</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB
Which of the below strings are matched by `re.search` using the pattern `'a..a'`?
Select all that apply.

[ ] `"aa bb cc"`
[ ] `"aaa bbb ccc"`
[ ] `"abaaba"`
[ ] `"abacaba"`

# BEGIN SOLN
**Answer: Option C

The regex pattern `'a..a'` searches the substring consisting of `a` followed by any two characters followed by `a`. The only string that has this pattern is Option C.

<average>99</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

Which of the below strings are matched by `re.search` using the pattern `'.*'`?
Select all that apply.

[ ] `"aa bb cc"`
[ ] `"aaa bbb ccc"`
[ ] `"abaaba"`
[ ] `"abacaba"`

# BEGIN SOLN
**Answer: Option A, B, C and D

The regex pattern `'.*'` searches the substring consisting of any character 0 or more times. Clearly all of the strings contain that pattern.

<average>100</average>

# END SOLN

# END SUBPROB

# END PROB
