# BEGIN PROB

Consider the following list of tokens.

```py
tokens = ["is", "the", "college", "board", "the", "board", "of", "college"]
```

# BEGIN SUBPROB

Recall, a uniform language model is one in which each **unique** token has the same chance of being sampled. Suppose we instantiate a uniform language model on `tokens`. The probability of the sentence "the college board is" --- that is, $P(\text{the college board is})$ --- is of the form $\frac{1}{a^b}$, where $a$ and $b$ are both positive integers.

What are $a$ and $b$?

# BEGIN SOLN

**Answer: ** a = 5, b = 4

In a uniform language model, each unique token has the same chance of being sampled. Given the list of tokens, there are 5 unique tokens: ["is", "the", "college", "board", "of"]. The probability of sampling any one token is $\frac{1}{5}$. For a sentence of 4 tokens ("the college board is"), the probability is $\frac{1}{5^4}$ because each token is independently sampled. Thus, $a = 5$ and $b = 4$.

<average>70</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

Recall, a unigram language model is one in which the chance that a token is sampled is equal to its observed frequency in the list of tokens. Suppose we instantiate a unigram language model on `tokens`. The probability $P(\text{the college board is})$ is of the form $\frac{1}{c^d}$, where $c$ and $d$ are both positive integers.

What are $c$ and $d$?

# BEGIN SOLN

**Answer: ** (c, d) = (2, 9) or (8, 3)

In a unigram language model, the probability of sampling a token is proportional to its frequency in the token list. The frequencies are: "is" = 1, "the" = 2, "college" = 2, "board" = 2, "of" = 1. The sentence "the college board is" has probabilities $\frac{2}{8}$, $\frac{2}{8}$, $\frac{2}{8}$, $\frac{1}{8}$ for each word respectively, when considering the total number of tokens (8). The combined probability is $\frac{2}{8} \cdot \frac{2}{8} \cdot \frac{2}{8} \cdot \frac{1}{8} = \frac{8}{512} = \frac{1}{2^9}$ or, simplifying, $\frac{1}{8^3}$ since $512 = 8^3$. Therefore, $c = 2$ and $d = 9$ or $c = 8$ and $d = 3$, depending on how you represent the fraction.

<average>68</average>

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

Remember, our corpus was:

```py
["is", "the", "college", "board", "the", "board", "of", "college"]
```

In order for a sentence to be sampled, it must be made up of bigrams that appeared in the corpus. This automatically rules out Sentence 1, because `"of the"` never appears in the corpus and Sentence 5, because `"board is"` never appears in the corpus.

Then, let's compute the probabilities of the other three sentences:

Sentence 2:

$$\begin{align*} P(\text{the board the board the}) &= P(\text{the}) \cdot P(\text{board | the}) \cdot P(\text{the | board}) \cdot P(\text{board | the}) \cdot P(\text{the | board}) \\ &= \frac{2}{8} \cdot \frac{1}{2} \cdot \frac{1}{2} \cdot \frac{1}{2} \cdot \frac{1}{2} \\ &= \frac{1}{64}
\end{align*}$$

Sentence 3:

$$\begin{align*} P(\text{board the college board of}) &= P(\text{board}) \cdot P(\text{the | board}) \cdot P(\text{college | the}) \cdot P(\text{board | college}) \cdot P(\text{of | board}) \\ 
&= \frac{2}{8} \cdot \frac{1}{2} \cdot \frac{1}{2} \cdot \frac{1}{2} \cdot \frac{1}{2} \\ &= \frac{1}{64}\end{align*}$$

Sentence 4:

$$\begin{align*} P(\text{the college board of college}) &= P(\text{the}) \cdot P(\text{college | the}) \cdot P(\text{board | college}) \cdot P(\text{of | board}) \cdot P(\text{college | of}) \\
&= \frac{2}{8} \cdot \frac{1}{2} \cdot 1 \cdot \frac{1}{2} \cdot 1 \\ &= \frac{1}{16} \end{align*}$$

Thus, Sentence 4 is most likely to be sampled.

<average>72</average>

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

Recall,

$$\text{tf-idf}(t, d) = \text{term frequency}(t, d) \cdot \text{inverse document frequency}(t)$$

In the context of TF-IDF, if a word appears in every sentence, its inverse document frequency (IDF) would be $\log(\frac{5}{5}) = 0$. Since a word's TF-IDF in a document is its TF (term frequency) in that document multiplied by its IDF, if the word's IDF is 0, it's TF-IDF is also 0. Since "the" appears in all five sentences, its IDF is zero, leading to a column of zeros in the TF-IDF matrix for "the".

<average>49</average>

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

Remember, the IDF of a word is the same for all documents, since $\text{idf}(t) = \log \left( \frac{\text{number of documents}}{number of documents containing $t$} \right)$. This means that the sentence where "college" is the word with the highest TF-IDF is the same as the sentence where "college" is the word with the highest TF, or term frequency. Sentence 4 is the only sentence where "college" appears twice; in all other sentences, "college" appears at most once. (Since all of these sentences have the same length, we know that if "college" appears more times in Sentence 4 than it does in other sentences, then "college"'s term frequency in Sentence 4, $\frac{2}{5}$, is also larger than in any other sentence.) As such, the answer is Sentence 4.

<average>95</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

As an alternative to TF-IDF, Yuxin proposes the DF-ITF, or "document frequency-inverse term frequency". The DF-ITF of term $t$ in document $d$ is defined below:

$$\text{df-itf}(t, d) = \frac{\text{\# of documents in which $t$ appears}}{\text{total \# of documents}} \cdot \log \left( \frac{\text{total \# of words in $d$}}{\text{\# of occurrences of $t$ in $d$}} \right)$$

Fill in the blank: The term $t$ in document $d$ that best summarizes document $d$ is the term with \_\_\_\_.

( ) the largest DF-ITF in document $d$
( ) the smallest DF-ITF in document $d$

# BEGIN SOLN

**Answer: ** the smallest DF-IDF in document $d$

The key idea behind TF-IDF, as we learned in class, is that $t$ is a good summary of $d$ if $t$ occurs commonly in $d$ but rarely across all documents.

When $t$ occurs often in $d$, then $\frac{\text{\# of occurrences of $t$ in $d$}}{\text{total \# of words in $d$}}$ is large, which means $\frac{\text{total \# of words in $d$}}{\text{\# of occurrences of $t$ in $d$}}$ and hence $\log \left( \frac{\text{total \# of words in $d$}}{\text{\# of occurrences of $t$ in $d$}} \right)$ is small.

Similarly, if $t$ is rare across all documents, then $\frac{\text{\# of documents in which $t$ appears}}{\text{total \# of documents}}$ is small.

Putting the above two pieces together, we have that $\text{df-itf}(t, d)$ is small when $t$ occurs commonly in $d$ but rarely overall, which means that the term $t$ that best summarizes $d$ is the term with the smallest DF-IDF in $d$.

<average>90</average>

# END SOLN

# END SUBPROB

# END PROB
