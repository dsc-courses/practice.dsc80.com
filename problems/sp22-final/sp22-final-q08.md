# BEGIN PROB

The DataFrame below contains a corpus of four song titles, labeled from
0 to 3.

::: center
![image](final-images/love_songs.png){width="50%"}
:::

# BEGIN SUBPROB

(1.5 pts) What is the TF-IDF of the word `"hate"` in Song 0's title? Use
base 2 in your logarithm, and give your answer as a simplified fraction.

# BEGIN SOLN

There are 12 words in Song 0's title, and 2 of them are `"hate"`, so the
term frequency of `"hate"` in Song 0's title is
$\frac{2}{12} = \frac{1}{6}$.

There are 4 documents total, and 2 of them contain `"hate"` (Song 0's
title and Song 3's title), so the inverse document frequency of `"hate"`
in the corpus is $\log_2 \left( \frac{4}{2} \right) = \log_2 (2) = 1$.

Then, the TF-IDF of `"hate"` in Song 0's title is

$$\text{TF-IDF} = \frac{1}{6} \cdot 1 = \frac{1}{6}$$

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

(1.5 pts) Which word in Song 0's title has the highest TF-IDF?

( ) `"i"`
( ) `"hate"`
( ) `"you"`
( ) `"love"`
( ) `"that"`
( ) Two or more words are tied for the highest TF-IDF in Song 0's title

# BEGIN SOLN

It was not necessary to compute the TF-IDFs of all words in Song 0's
title to determine the answer. $\text{tfidf}(t, d)$ is high when $t$
occurs often in $d$ but rarely overall. That is the case with `"i"` ---
it is the most common word in Song 0's title (with 4 appearances), but
it does not appear in any other document. As such, it must be the word
with the highest TF-IDF in Song 0's title.

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

(1.5 pts) Let $\text{tfidf}(t, d)$ be the TF-IDF of term $t$ in document
$d$, and let $\text{bow}(t, d)$ be the number of occurrences of term $t$
in document $d$.

**Select all** correct answers below.

[ ] If $\text{tfidf}(t, d) = 0$, then $\text{bow}(t, d) = 0$.
[ ] If $\text{bow}(t, d) = 0$, then $\text{tfidf}(t, d) = 0$.
[ ] Neither of the above statements are necessarily true.

# BEGIN SOLN

Recall that $\text{tfidf}(t, d) = \text{tf}(t, d) \cdot \text{idf}(t)$,
and note that $\text{tf}(t, d)$ is just
$\frac{1}{\text{# words in $d$}} \cdot \text{bow}(t, d)$. Thus,
$\text{tfidf}(t, d)$ is 0 is if either $\text{bow}(t, d) = 0$ or
$\text{idf}(t) = 0$.

So, if $\text{bow}(t, d) = 0$, then $\text{tf}(t, d) = 0$ and
$\text{tfidf}(t, d) = 0$, so the second option is true. However, if
$\text{tfidf}(t, d) = 0$, it could be the case that
$\text{bow}(t, d) > 0$ and $\text{idf}(t) = 0$ (which happens when term
$t$ is in every document), so the first option is not necessarily true.

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

(1.5 pts) Below, we've encoded the corpus from the previous page using
the bag-of-words model.

::: center
![image](final-images/bag-words.png){width="70%"}
:::

Note that in the above DataFrame, each row has been normalized to have a
length of 1 (i.e. $|\vec{v}| = 1$ for all four row vectors).

Which song's title has the highest cosine similarity with Song 0's
title?

( ) Song 1
( ) Song 2
( ) Song 3

# BEGIN SOLN

Recall, the cosine similarity between two vectors $\vec{a}, \vec{b}$ is
computed as

$$\cos \theta = \frac{\vec{a} \cdot \vec{b}}{| \vec{a} | | \vec{b}|}$$

We are told that each row vector is already normalized to have a length
of 1, so to compute the similarity between two songs' titles, we can
compute dot products directly.

-   Song 0 and Song 1: $0.47 \cdot 0.76$

-   Song 0 and Song 2: $0.47 \cdot 0.58 + 0.71 \cdot 0.58$

-   Song 0 and Song 3: $0.47 \cdot 0.71$

Without using a calculator (which students did not have access to during
the exam), it is clear that the dot product between Song 0's title and
Song 2's title is the highest, hence Song 2's title is the most similar
to Song 0's.

# END SOLN

# END SUBPROB

# END PROB