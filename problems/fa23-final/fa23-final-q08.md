# BEGIN PROB
Consider the following corpus:

| **Document number** | Content                           |
|-----------------|-----------------------------------|
| **1**               | yesterday rainy today sunny     |
| **2**               | yesterday sunny today sunny     |
| **3**               | today rainy yesterday today     |
| **4**               | yesterday yesterday today today |

# BEGIN SUBPROB
Using a bag-of-words representation, which two documents have the largest dot product? Show your work, then write your final answer in the blanks below.

Documents ____ and ____
# BEGIN SOLN
**Answer**: Documents 3 and 4

The bag-of-words representation for the documents is:

| **Document number** | yesterday | rainy | today | sunny |
|----------|-----------|-------|-------|-------|
| **1**        | 1         | 1     | 1     | 1     |
| **2**        | 1         | 0     | 1     | 2     |
| **3**        | 1         | 1     | 2     | 0     |
| **4**        | 2         | 0     | 2     | 0     |

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

[ ] yesterday
[ ] rainy
[ ] today
[ ] sunny

# BEGIN SOLN

**Answer**: yesterday and today

Remember,

$$\text{tf-idf}(t, d) = \text{tf}(t, d) \cdot \text{idf}(t)$$

where $\text{tf}(d, t)$, the term frequency of term $t$ in document $d$, is the proportion of terms in $d$ that are equal to $t$, and $\text{idf}(t) = \log \left( \frac{\text{number of documents}}{\text{number of documents containing $t$}} \right)$.

In order for $\text{tf-idf}(t, d)$ to be 0, either $t$ must not be in document $d$ (meaning $\text{tf}(t, d) = 0$), or $t$ is in every document (meaning $\text{idf}(t) = \log(\frac{n}{n}) = \log(1) = 0$). In this case, we're looking for words that have a $\text{tf-idf}$ of 0 across all documents, which means we're looking for words that have a $\text{idf}(t)$ of 0, meaning they're in every document. The words that are in every document are yesterday and today.

<average>94</average>

# END SOLN
# END SUBPROB
# END PROB