# BEGIN PROB

Valentina has over 1000 students. When a student signs up for
Valentina's college counseling, they must provide a variety of
information about themselves and their parents. Valentina keeps track of
all of this information in a table, with one row per student. (Note that
this is **not** the `students` DataFrame from earlier in the exam.)

# BEGIN SUBPROB

Valentina asks each her students for the university that their parents
attended for undergrad. The `"father’s university"` column of
Valentina's table contains missing values. Valentina believes that
values in this column are missing because not all students' fathers
attended university.

According to Valentina's interpretation, what is the missingness
mechanism of `"father’s university"`?

( ) Missing by design
( ) Not missing at random
( ) Missing at random
( ) Missing completely at random

# BEGIN SOLN

**Answer: **Not missing at random

Per Valentina's interpretation, the reason for the missingness in the
`"father’s university"` column is that not all fathers attended
university, and hence they opted not to fill out the survey. Here, the
likelihood that values are missing depends on the values themselves, so
the data are NMAR.

<average>81</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

The `"mother’s phone number"` column of Valentina's table contains
missing values. Valentina knows for a fact that all of her students'
mothers have phone numbers. She looks at her dataset and draws the
following visualization, relating the missingness of
`"mother’s phone number"` to `"district"` (the school district that the
student's family lives in):

<center><img src='../assets/images/sp22-midterm/missingness.png' width=50%></center>

Given just the above information, what is the missingness mechanism of
`"mother’s phone number"`?

( ) Missing by design
( ) Not missing at random
( ) Missing at random
( ) Missing completely at random

# BEGIN SOLN

**Answer: ** Missing at random

Here, the distribution of `"district"` is different when
`"mother’s phone number"` is missing and when `"mother’s phone number"`
is present (the two distributions plotted look quite different. As such,
we conclude that the missingness of `"mother’s phone number"` depends on
`"district"`, and hence the data are MAR.

<average>88</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

UC Hicago, a new private campus of the UC, has an annual tuition of
\$80,000. UC Hicago states that if an admitted student's parents'
combined income is under \$80,000, they will provide that student a
scholarship for the difference.

Valentina keeps track of each student's parents' incomes along with the
scholarship that UC Hicago promises them in a table. The first few rows
of her table are shown below.

<center><img src='../assets/images/sp22-midterm/scholarship.png' width=50%></center>

Given just the above information, what is the missingness mechanism of
`"scholarship"`?

( ) Missing by design
( ) Not missing at random
( ) Missing at random
( ) Missing completely at random

# BEGIN SOLN

**Answer: ** Missing by design

Here, the data are missing by design because you can 100% of the time
predict whether a `"scholarship"` will be missing by looking at the
`"mother’s income"` and `"father’s income"` columns. If the sum of
`"mother’s income"` and `"father’s income"` is at least \$80,000,
`"scholarship"` will be missing; otherwise, it will not be missing.

<average>88</average>

# END SOLN

# END SUBPROB

# END PROB