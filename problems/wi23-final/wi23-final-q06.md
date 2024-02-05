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

In a uniform language model, each unique token has the same chance of being sampled. Given the list of tokens, there are 5 unique tokens: ["is", "the", "college", "board", "of"]. The probability of sampling any one token is \(\frac{1}{5}\). For a sentence of 4 tokens ("the college board is"), the probability is \(\frac{1}{5^4}\) because each token is independently sampled. Thus, \(a = 5\) and \(b = 4\).

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

Recall, a unigram language model is one in which the chance that a token is sampled is equal to its observed frequency in the list of tokens. Suppose we instantiate a unigram language model on `tokens`. The probability $P(\text{the college board is})$ is of the form $\frac{1}{c^d}$, where $c$ and $d$ are both positive integers.

What are $c$ and $d$?

# BEGIN SOLN

**Answer: ** (c, d) = (2, 9) or (8, 3)

In a unigram language model, the probability of sampling a token is proportional to its frequency in the token list. The frequencies are: "is" = 1, "the" = 3, "college" = 2, "board" = 2, "of" = 1. The sentence "the college board is" has probabilities \(\frac{3}{8}\), \(\frac{2}{8}\), \(\frac{2}{8}\), \(\frac{1}{8}\) for each word respectively, when considering the total number of tokens (8). The combined probability is \(\frac{3}{8} \times \frac{2}{8} \times \frac{2}{8} \times \frac{1}{8} = \frac{6}{512} = \frac{1}{2^9}\) or, simplifying, \(\frac{1}{8^3}\) since \(512 = 8^3\). Therefore, \(c = 2\) and \(d = 9\) or \(c = 8\) and \(d = 3\), depending on how you represent the fraction.

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

A bigram model looks at the probability of a word given the previous word. Sentence 4, "the college board of college", likely has higher probabilities for its bigrams ("the college", "college board", "board of", "of college") based on the original list of tokens, which contains all these pairs. This reasoning assumes that the given pairs appear more frequently or are more probable in sequence than the pairs in other sentences.

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

In the context of TF-IDF, if a word appears in every sentence, its inverse document frequency (IDF) part would be \(\log(\frac{5}{5}) = 0\), making the TF-IDF score 0 for that word across all documents. Since "the" appears in all five sentences, its IDF is zero, leading to a column of zeros in the TF-IDF matrix for "the".

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

The word "college" likely has the highest TF-IDF in Sentence 4 because it appears less frequently across all sentences and is relatively more important (i.e., has a higher term frequency) in Sentence 4 than in other sentences where it appears. TF-IDF rewards words that are unique to a document but penalizes those that are common across all documents.

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

As an alternative to TF-IDF, Yuxin proposes the DF-ITF, or "document frequency-inverse term frequency". The DF-ITF of term $t$ in document $d$ is defined below:

$$\text{df-itf}(t, d) = \frac{\text{\# of documents in which $t$ appears}}{\text{total \# of documents}} \cdot \log \left( \frac{\text{total \# of words in $d$}}{\text{\# of occurrences of $t$ in $d$}} \right)$$

Fill in the blank: The term $t$ in document $d$ that best summarizes document $d$ is the term with \_\_\_\_.

( ) the largest DF-ITF in document $d$
( ) the smallest DF-ITF in document $d$

# BEGIN SOLN

**Answer: ** the smallest

The DF-ITF score is lower for terms that are more unique (appear in fewer documents) and have a higher count in the document they appear in. A smaller DF-ITF indicates that a term is both important within a specific document and distinctive across the corpus. Therefore, the term with the smallest DF-ITF in a document is considered the best summary for that document, as it balances document-specific significance with corpus-wide uniqueness.

# END SOLN

# END SUBPROB

# END PROB
