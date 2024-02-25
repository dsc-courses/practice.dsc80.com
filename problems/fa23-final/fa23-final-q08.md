# BEGIN PROB
Consider the following corpus:

| Document number | Content                           |
|-----------------|-----------------------------------|
| 1               | 'yesterday rainy today sunny'     |
| 2               | 'yesterday sunny today sunny'     |
| 3               | 'today rainy yesterday today'     |
| 4               | 'yesterday yesterday today today' |

# BEGIN SUBPROB
Using a bag-of-words representation, which two documents have the largest dot product? Show your work, then write your final answer in the blanks below.

Documents ____ and ____
# BEGIN SOLN
**Answer**: Documents 3 and 4

The bag-of-words representation for the documents is:
| Document | yesterday | rainy | today | sunny |
|----------|-----------|-------|-------|-------|
| 1        | 1         | 1     | 1     | 1     |
| 2        | 1         | 0     | 1     | 2     |
| 3        | 1         | 1     | 2     | 0     |
| 4        | 2         | 0     | 2     | 0     |
The dot product between documents $3$ and $4$ is $6$, which is the highest among all pairs of documents.

<average>84</average>

# END SOLN
# END SUBPROB

# BEGIN SUBPROB
Using a bag-of-words representation, what is the cosine similarity between documents $2$ and $3$? Show your work below, then write your final answer in the blank below.
# BEGIN SOLN
**Answer**: $\frac{1}{2}$

The dot product between documents $2$ and $3$ is: $$1 + 0 + 2 + 0 = 3$$ The magnitude of document $2$ is equal to document $3$ and is: $$\sqrt{1^2 + 0 ^2 + 1^2 + 2^2} = \sqrt{6}$$ So, the cosine similarity is $$\frac{3}{\sqrt{6}\times\sqrt{6}} = \frac{1}{2}$$

<average>70</average>

# END SOLN
# END SUBPROB

# BEGIN SUBPROB
Which words have a TF-IDF score $0$ for all four documents? Assume that we use base-2 logarithms. **Select all the words that apply.**
- yesterday
- rainy
- today
- sunny
# BEGIN SOLN
**Answer**: yesterday and today

We are looking at the TF-IDF score for each document and seeing if it is zero. Since IDF for one document would just be $1$ if the word is in the document and $0$ otherwise, we can just check the value of IDF. Since we are using base-2 logarithms, the TF-IDF score is $0$ when the IDF score is $1$. Therefore we need to find the words that appear in every document, which are yesterday and today.

<average>94</average>

# END SOLN
# END SUBPROB
# END PROB