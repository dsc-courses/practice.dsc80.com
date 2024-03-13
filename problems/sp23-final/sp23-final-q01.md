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

This regular expression selects the sections of matches that consist of zero or 
more lowercase letters that are followed by a space and then followed by cat as 
a whole word (not with cat as a substring of a larger word), essentially 
selecting words followed by a space and the word cat. Thus this option 
correctly selects `['my', 'a']`.

Option 1 would select `['', '']` \
Option 2 would select `['my cat', 'a cat']` \
Option 4 would select `['my cat', 'a cat']` \

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

This regular expression selects matches where one or more lowercase letters are 
followed by the substring cat, and then followed by one or more lowercase 
letters, essentially selecting words with cat as a substring but not a prefix. 
Thus this option correctly selects `['concatenate']`.

Option 1 would select `['my cat is hungry, concatenate!, catastrophe! What a cat']` \
Option 2 would select `['cat', 'concatenate', 'catastrophe', 'cat']` \
Option 4 would select `['cat', 'concatenate', 'catastrophe', 'cat']` \

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

This regular expression selects matches where a word boundary is followed by 
0 or more lowercase letters, cat, and then follwoed by 0 or more lowercase 
letters followed by a word coundary, essentially selecting words containing cat.
Thus this option correctly selects `['cat', 'concatenate', 'catastrophe', 'cat']`.

Option 1 would select `['my cat is hungry, concatenate!, catastrophe! What a cat!']` \
Option 2 would select `['my cat is hungry, concatenate!, catastrophe! What a cat!']` \
Option 4 would select `['concatenate']` \

# END SOLN

# END SUBPROB

# END PROB