# BEGIN PROB
Consider the following Code Snippet:

`re.findall(r'__(a)__', 'my cat is hungry, concatenate!, catastrophe! What a cat!')`

# BEGIN SUBPROB

Which regular expression in **\_\_(a)\_\_** will generate the following output?
`Output: ['my', 'a']`

( ) `\b([a-z]*)cat\b`
( ) `\b[a-z]*\scat\b`
( ) `([a-z]*)\scat\b`
( ) `\b([a-z]*\scat)\b`

# BEGIN SOLN
**Answer:** C - `([a-z]*)\scat\b`

# END SOLN

# END SUBPROB

# BEGIN SUBPROB
Which regular expression in **\_\_(a)\_\_** will generate the following output?

`Output: ['concatenate']`

( ) `\b.*cat.*\b`
( ) `[a-z]*cat[a-z]*`
( ) `[a-z]+cat[a-z]+`
( ) `\b[a-z]*cat[a-z]*\b`

# BEGIN SOLN
**Answer:** C - `[a-z]+cat[a-z]+`

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

Which regular expression in **\_\_(a)\_\_** will generate the following output?

`Output: ['cat', 'concatenate', 'catastrophe', 'cat']`

( ) `.*cat.*`
( ) `\b.*cat.*\b`
( ) `\b[a-z]*cat[a-z]*\b`
( ) `\b[a-z]+cat[a-z]+\b`

# BEGIN SOLN
**Answer:** C - `\b[a-z]*cat[a-z]*\b`

# END SOLN

# END SUBPROB

# END PROB