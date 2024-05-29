# BEGIN PROB

Consider the corpus of length 13 below, made up of 6 As, 4 Bs, 1 C, and 2 Rs (and no other tokens). Here, each individual character is treated as its own token.

$$\text{ABABRACABABRA}$$

Let $P$ be a function that computes the probability of the input sequence using a bigram model trained on the above corpus. For example, $P$(BR) is the probability of the sequence BR, using a bigram language model trained on the above corpus.

# BEGIN SUBPROB

What is $P$(ABRA)? Give your answer as a simplified fraction.

# BEGIN SOLUTION

**Answer:** $\frac{12}{65}$

Using a bigram model, we find the probability of the first token, then for each remaining token, find its probability given just the previous token. The probability $P(\text{X} | \text{Y})$ is simply the proportion of times that token X is the next token after the previous token Y. So, for this corpus and input sequence, we have:

$$P(\text{A}) = \frac{6}{13}$$

$$P(\text{B} | \text{A}) = \frac{4}{5}$$

$$P(\text{R} | \text{B}) = \frac{2}{4} = \frac{1}{2}$$

$$P(\text{A} | \text{R}) = \frac{2}{2} = 1$$

So, we just have to multiply these probabilities together, and we get $\frac{12}{65}$.

Note that the denominator for $P(\text{B} | \text{A})$ is 5, not 6, even though there are 6 occurrences of the letter A. This is because the final one occurs at the end of the sentence, and we're not using a stop token or anything else designating the end of the sequence. So there are only 5 instances of "A" where we have a subsequent token, which is how we make our probability model.

<average>47</average>

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Suppose $n$ is a positive integer. Let $[AB]^{n}$ be the result of repeating the sequence AB $n$ times. For example, $[AB]^{4}$ is ABABABAB and $[AB]^{5}$ is ABABABABAB.

Then, it is always the case that:

$$P([AB]^{n}) = 2p (\frac{c}{d})^{k}$$

where:

- $p = P$(ABRA) is your answer to part (a)
- $c$ and $d$ are positive integers that don't depend on $n$, and $\frac{c}{d}$ is a simplified fraction
- $k$ is a positive number that does depend on $n$

1. What is $c$? Give your answer as a positive integer. Remember, your answer should *not* depend on $n$, meaning that it should have no variables in it.
2. What is $d$? Give your answer as a positive integer. Remember, your answer should *not* depend on $n$, meaning that it should have no variables in it.
3. What is $k$?

( ) 2 
( ) $\frac{n}{2} - 1$
( ) $\frac{n}{2}$
( ) $n - 1$
( ) $n$
( ) $n + 1$

*Hint: Start by finding P(AB), P(ABAB), and P(ABABAB).*

# BEGIN SOLUTION

**Answer:**

1. $c = 2$
2. $d = 5$
3. $k = n-1$

From our work on the previous question, we can see that $2p$ is equal to $P(\text{A}) \cdot P(\text{B} | \text{A})$, or in other words, the probability of the sequence AB.

The probability of sequence ABAB will be the probability of sequence AB, times $P(\text{A} | \text{B}) \cdot P(\text{B} | \text{A})$. More generally, we can see that after the first pair of tokens AB (which has a different probability since the first token is the first in the sequence, and therefore isn't conditioned on B), each repetition of AB multiplies a probability of $P(\text{A} | \text{B}) \cdot P(\text{B} | \text{A})$. 

Therefore, our resulting fraction $\frac{c}{d}$ is simply this probability $P(\text{A} | \text{B}) \cdot P(\text{B} | \text{A})$.  $P(\text{A} | \text{B})$ is $\frac{1}{2}$, and we already found that $P(\text{B} | \text{A})$ is $\frac{4}{5}$, so the resulting fraction is $\frac{2}{5}$. So $c$ = 2, and $d$ = 5.

This fraction is multiplied once for each repetition of AB *after the first one* (which has a different probability, represented by $2p$), and so the exponent should be $n-1$.

<average>66</average>

# END SOLUTION

# END SUBPROB

# END PROB

