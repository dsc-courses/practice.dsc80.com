# BEGIN PROB

# BEGIN SUBPROB
Consider the following four sentences:

 - "this is one"
 - "this is two"
 - "this is the third"
 - "and this is the fourth"

Suppose these sentences are encoded into a "bag of words" feature representation. The result is a dataframe with four rows (one for each sentence). How many columns are in this dataframe? Your answer should be in the form of a number.

# BEGIN SOLN
**Answer: ** 8

Recall that bag of word creates a new column for each unique word. Thus the problem boils down to "how many unique words are there in the following four sentences", which we count 8: "this", "is", "one", "two", "the", "third", "and", "fourth".

<average>98</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB
Again consider the same four sentences shown above.

What is the TF-IDF score for the word "this" in the first sentence? Use base-2 logarithm.

Your answer should be in the form of a number.

# BEGIN SOLN
**Answer: ** 0

Recall that TF is calculated as the number of terms that appear in that sentence divided by the total number of terms in the sentence. In this case the TF value of "this" in the first sentence is $\frac{1}{3}$.

IDF is calculated as the log of the number of sentences divided by the number of sentences in which that term appears in. In this case, the IDF value of "this" in the first sentence is $\log_{2}(\frac{4}{4}) = 0$.

Thus the TF-IDF is just $\frac{1}{3} * 0 = 0$

<average>97</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

Again consider the same four sentences shown above.

What is the TF-IDF score for the word "and" in the last sentence? Use base-2 logarithm.

Your answer should be in the form of a number.

# BEGIN SOLN
**Answer: ** 0.4

Recall that TF is calculated as the number of terms that appear in that sentence divided by the total number of terms in the sentence. In this case the TF value of "and" in the last sentence is $\frac{1}{5}$.

IDF is calculated as the log of the number of sentences divided by the number of sentences in which that term appears in. In this case, the IDF value of "and" in the last sentence is $\log_{2}(\frac{4}{1}) = 2$.

Thus the TF-IDF is just $\frac{1}{5} * 2 = 0.4$

<average>89</average>

# END SOLN

# END SUBPROB

# END PROB