# BEGIN PROB

Gabriel decides to look at reviews for the Catamaran Resort Hotel and Spa. TripAdvisor has 96 reviews for the hotel; of those 96, Gabriel’s favorite review was:

```
    "close to the beach but far from the beach beach"
```

# BEGIN SUBPROB

What is the TF of `"beach"` in Gabriel’s favorite review? Give your answer as a simplified fraction.

# BEGIN SOLUTION

**Answer:** $\frac{3}{10}$

The answer is simply the proportion of words in the sentence that are the word `"beach"`. There are 10 words in the sentence, 3 of which are `"beach"`.

<average>97</average>

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

The TF-IDF of `"beach"` in Gabriel’s favorite review is $\frac{9}{10}$, when using a base-2 logarithm to compute the IDF. How many of the reviews on TripAdvisor for this hotel contain the term `"beach"`?

( ) 3
( ) 6
( ) 8
( ) 12
( ) 16
( ) 24
( ) 32

# BEGIN SOLUTION

**Answer:** 12

The TF-IDF is the product of the TF and IDF terms. So if the TF-IDF of this document is $\frac{9}{10}$, and the TF is $\frac{3}{10}$, as established in the last part, the IDF of the term `"beach"` is 3. The IDF for a word is the log of the inverse of the proportion of documents in which the word appears. So, since we know there are 96 total documents.

$$3 = log_{2}(\frac{96}{\text{\# documents containing "beach"}})$$

$$2^{3} = \frac{96}{\text{\# documents containing "beach"}}$$

$$\boxed{12} = {\text{\# documents containing "beach"}}$$

<average>76</average>

# END SOLUTION

# END SUBPROB

# END PROB