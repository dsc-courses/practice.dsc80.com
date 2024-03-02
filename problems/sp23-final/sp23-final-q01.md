# BEGIN PROB

Consider the following Code Snippet:

    re.findall(r'--(a)--', 
               'my cat is hungry, concatenate!, catastrophe! What a cat!')

# BEGIN SUBPROB

Which regular expression in **(a)** will generate the following output?

    Output: ['my', 'a'] 

( )

    \b([a-z]*)cat\b

( )

    \b[a-z]*\scat\b

( )

    ([a-z]*)\scat\b

( )

    \b([a-z]*\scat)\b

# BEGIN SOLUTION

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Which regular expression in **(a)** will generate the following output?

    Output: ['concatenate']

( )

    \b.*cat.*\b

( )

    [a-z]*cat[a-z]*

( )

    [a-z]+cat[a-z]+

( )

    \b[a-z]*cat[a-z]*\b

# BEGIN SOLUTION

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Which regular expression in **(a)** will generate the following output?

    Output: ['cat', 'concatenate', 'catastrophe', 'cat']

( )

    .*cat.*

( )

    \b.*cat.*\b

( )

    \b[a-z]*cat[a-z]*\b

( )

    \b[a-z]+cat[a-z]+\b

# BEGIN SOLUTION

# END SOLUTION

# END SUBPROB

# END PROB