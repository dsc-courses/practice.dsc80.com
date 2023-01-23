# BEGIN PROB

# BEGIN SUBPROB

Each Spotify charts webpage is specific to a particular country (as
different countries have different music tastes). Embedded in each
charts page is a "datestring\", that describes:

-   the number of songs on the page,

-   the country, and

-   the date.

For instance, `"3*Canada-2022-06-04"` is a datestring stating that the
page contains the top 3 songs in Canada on June 4th, 2022. A valid
datestring contains a number, a country name, a year, a month, and a
day, such that:

-   the number, country name, and year are each separated by a single
    dash (`"-"`), asterisk (`"*"`), or space (`" "`).

-   the year, month, and day are each separated by a single dash (`"-"`)
    only

Below, assign `exp` to a regular expression that **extracts country
names from valid datestrings**. If the datestring does not follow the
above format, it should not extract anything. Example behavior is given
below.

    >>> re.findall(exp, "3*Canada-2022-06-04")
    ["Canada"]

    >>> re.findall(exp, "144 Brazil*1998-11-26")
    ["Brazil"]

    >>> re.findall(exp, "18_USA-2009-05-16")
    []

`exp = r"^`  `$"`

# BEGIN SOLN

**Answer: ** One solution is given below.

<center><img src='../assets/images/sp22-final/regex101-1.png' width=50%></center>

Click [this link](https://regex101.com/r/K88ddE/1) to interact with the
solution on regex101.

While grading, we were not particular about students' treatment of
uppercase characters in country names.

<average>76</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

Consider the following regular expression.

    r"^\w{2,5}.\d*\/[^A-Z5]{1,}"

**Select all** strings below that **contain any match** with the regular
expression above.

[ ] `"billy4/Za"`
[ ] `"billy4/za"`
[ ] `"DAI_s2154/pacific"`
[ ] `"daisy/ZZZZZ"`
[ ] `"bi_/_lly98"`
[ ] `"!@__!14/atlantic"`

# BEGIN SOLN

**Answer: ** Option B, Option C, and Option E

Let's first dissect the regular expression into manageable groups:

-   `"^"` matches the regex to its right at the start of a given string
-   `"\w{2,5}"` matches alphanumeric characters (a-Z, 0-9 and _) 2 to 5 times inclusively. (Note the that it does indeed match with the underscore)
-   `"."` is a basic wildcard
-   `"\d*"` matches digits (0-9), at least 0 times
-   `"\/"` matches the `"/"` character
-   `"[^A-Z5]{1,}"` matches any character that isn't (A-Z or 5) at least once.

Thus using these rules, it's not hard to verify that Options B, C and E are matches.

<average>85</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

Consider the following string and regular expressions:

    song_str = "doja cat you right"

    exp_1 = r"\b\w+\b" # \b stands for word boundary
    exp_2 = r" \w+"
    exp_3 = r" \w+ "

1.  What does `len(re.findall(exp_1, song_str))` evaluate to?

2.  What does `len(re.findall(exp_2, song_str))` evaluate to?

3.  What does `len(re.findall(exp_3, song_str))` evaluate to?

# BEGIN SOLN

**Answer: ** See below

    1. `"\b"` matches "word boundaries\", which are any locations that separate words. As such, there are 4 matches --- `["doja", "cat", "you", "right"]`. Thus the answer is 4.

    2. The 3 matches are `[" cat", " you", " right"]`. Thus the answer is 3.

    3. This was quite tricky! The key is remembering that `re.findall` only finds **non-overlapping matches** (if you look at the solutions to the above two parts, none of the matches overlapped). Reading from left to right, there is only a single non-overlapping match: `"cat"`. Sure, `" you "` also matches the pattern, but since the space after `"cat"` was already "found\" by `re.findall`, it cannot be included in any future matches. Thus the answer is 1.

<average>60</average>

# END SOLN

# END SUBPROB

# END PROB