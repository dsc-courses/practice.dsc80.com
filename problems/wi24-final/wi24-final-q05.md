# BEGIN PROB

Dylan finds a messy text file containing room availability and pricing information at his favorite local hotel, the Manchester Grand Hyatt.

# BEGIN SUBPROB

Availability strings are formatted like so:

```
    avail = """Standard: Available, This23: Available,
    Suite: Available, Economy: Not Available,
    Rooms are Available, Deluxe: Available"""
```

Fill in the blank below so that `exp1` is a regular expression such that if `s` is an availability string in the format above, `re.findall(exp1, s)` will return a list of all of the available room categories in `s`. Example behavior is given below.

```py
    >>> re.findall(exp1, avail)
    ["Standard", "Suite", "Deluxe"] # Categories don't include numbers
```

Note that your answer needs to work on other availability strings; you should not hard-code `"Standard"`, `"Suite"`, or `"Deluxe"`.

```
exp1 = r"_____________"
```

# BEGIN SOLUTION

**Answer:** `([A-Za-z]+): Available`

In the above availability strings, we're looking for a one-or-more-length sequence of letters (not numbers, as mentioned in the problem), followed by a colon and the word "Available." However, since we only want to return the room type, and not the colon or the word "Available," we use a capturing group (the parentheses) to just return the word before the colon.

<average>57</average>

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Consider the string `prices`, defined below.

```py
    one = "Standard room: $120, $2.Deluxe room: $200.75"
    two = "Other: 402.99, Suite: $350.25"
    prices = one + ", " + two
```

1. What does `re.findall(r"\$\d+\.\d{2}$", prices)` evaluate to?

( ) `["$200.75", "$402.99", "$350.25"]`
( ) `["200.75", "402.99", "350.25"]`
( ) `["$120", "$200.75", "$350.25"]`
( ) `["$350.25"]`
( ) `["$200.75", "$350.25"]`

2. What does `re.findall(r"\$?(\d+\.\d{2})", prices)` evaluate to?

( ) `["$200.75", "$402.99", "$350.25"]`
( ) `["200.75", "402.99", "350.25"]`
( ) `["$120", "$200.75", "$350.25"]`
( ) `["$350.25"]`
( ) `["$200.75", "$350.25"]`

# BEGIN SOLUTION

**Answers:**

1. `["$350.25"]`
2. `["200.75", "402.99", "350.25"]`

In the first part, the string that the pattern matches is a dollar sign (`$`), one or more digits (`\d+`), a period (`\.`), two digits (`\d{2}`), followed by the end of the string (`$`). Since the string we're passing into `re.findall` is `prices`, which is the concatenation of `one + ", " + two`, the only option that matches is the last price displayed, `"$350.25"`. (If we had not specified the match ending with the end of the string, `"$200.75"` would also have been a match.)

In the second part, the beginning of the pattern is `"\$?"`, which means to match *zero or one* instance of the dollar sign character. In most cases, this means that if there is a dollar sign before the remainder of the pattern, it will be included in the match, but if not, the rest of the pattern will still match. However, the capturing group around the remainder of the pattern means that in either case, only the remainder of the pattern after the dollar sign is captured. (So, in this particular example, the `\$?` has no effect on the output.) 

The rest of the pattern is structured similarly to the previous part, except now, the pattern does not require the end of the string after the price, so we're just selecting sequences of digits followed by a period and two more digits, which is how we get our solution.

<average>65</average>

# END SOLUTION

# END SUBPROB

# END PROB