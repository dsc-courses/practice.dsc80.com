# BEGIN PROB

Consider the following list of tokens.

"`py
tokens = ["is", "the", "college", "board", "the", "board", "of", "college"]
"`

# BEGIN SUBPROB
Recall, a uniform language model is one in which each **unique** token has the same chance of being sampled. Suppose we instantiate a uniform language model on `tokens`. The probability of the sentence """the college board is" --- that is, $P(\text{the college board is})$ --- is of the form $\frac{1}{a^b}$, where $a$ and $b$ are both positive integers.

What are $a$ and $b$?

# BEGIN SOLN
**Answer: ** a = 5, b = 4

# END SOLN

# END SUBPROB

# BEGIN SUBPROB
Recall, a unigram language model is one in which the chance that a token is sampled is equal to its observed frequency in the list of tokens. Suppose we instantiate a unigram language model on `tokens`. The probability $P(\text{the college board is})$ is of the form $\frac{1}{c^d}$, where $c$ and $d$ are both positive integers.

What are $c$ and $d$?

# BEGIN SOLN
**Answer: ** (c, d) = (2, 9) or (8, 3)

# END SOLN

# END SUBPROB

For the remainder of this question, consider the following five sentences.

-     "of the college board the"

-     "the board the board the"

-     "board the college board of"

-     "the college board of college"

-     "board the college board is"

# BEGIN SUBPROB
Recall, a bigram language model is an $N$-gram model with $N=2$. Suppose we instantiate a bigram language model on `tokens`. Which of the following sentences of length 5 is the **most** likely to be sampled?

( ) Sentence 1
( ) Sentence 2
( ) Sentence 3
( ) Sentence 4
( ) Sentence 5
    
# BEGIN SOLN
**Answer: ** Sentence 4

# END SOLN

# END SUBPROB

For your convenience, we repeat the same five sentences again below.

-     "of the college board the"

-     "the board the board the"

-     "board the college board of"

-     "the college board of college"

-     "board the college board is"

Suppose we create a TF-IDF matrix, in which there is one row for each sentence and one column for each unique word. The value in row $i$ and column $j$ is the TF-IDF of word $j$ in sentence $i$. Note that since there are 5 sentences and 5 unique words across all sentences, the TF-IDF matrix has 25 total values.

# BEGIN SUBPROB

Is there a column in the TF-IDF matrix in which all values are 0?

( ) Yes
( ) No

# BEGIN SOLN
**Answer: ** Yes

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

In which of the following sentences is "college" the word with the highest TF-IDF?

( ) Sentence 1
( ) Sentence 2
( ) Sentence 3
( ) Sentence 4
( ) Sentence 5
    
# BEGIN SOLN
**Answer: ** Sentence 4

# END SOLN

# END SUBPROB

# BEGIN SUBPROB
As an alternative to TF-IDF, Yuxin proposes the DF-ITF, or "document frequency-inverse term frequency". The DF-ITF of term $t$ in document $d$ is defined below:

$$\text{df-itf}(t, d) = \frac{\text{\# of documents in which $t$ appears}}{\text{total \# of documents}} \cdot \log \left( \frac{\text{total \# of words in $d$}}{\text{\# of occurrences of $t$ in $d$}} \right)$$

Fill in the blank: The term $t$ in document $d$ that best summarizes document $d$ is the term with ____.

( ) the largest DF-ITF in document $d$
( ) the smallest DF-ITF in document $d$

# BEGIN SOLN
**Answer: ** the smallest

# END SOLN

# END SUBPROB

# END PROB