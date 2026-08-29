# BEGIN PROB

Suppose we train a unigram, bigram, and trigram model on the following corpus.

```py
corpus = "Patient is ill. Patient is in pain. Ill patient will recover in time."
```

We tokenized the corpus as follows before training our models.

```py
corpus.lower().split()
```

Now, we'd like to determine the probability of generating the sentence below, according to each model.

`"Patient is in time."`

For each part, give your answer as a simplified fraction (preferred) or a product of simplified fractions.

# BEGIN SUBPROB

Determine the probability of the sentence above, according to the unigram model.

# BEGIN SOLUTION

**Answer:** $\frac{3}{13} \cdot \frac{2}{13} \cdot \frac{2}{13} \cdot \frac{1}{13}$

After lowercasing and splitting, the corpus has 13 tokens: three `"patient"`, two `"is"`, two `"in"`, and one each of the remaining tokens. The unigram model multiplies the marginal probabilities of each word in the sentence.

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Determine the probability of the sentence above, according to the bigram model.

# BEGIN SOLUTION

**Answer:** $\frac{1}{26}$

Under the bigram model, multiply the probability of the first token by each subsequent conditional probability. This product simplifies to $\frac{1}{26}$.

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Determine the probability of the sentence above, according to the trigram model.

# BEGIN SOLUTION

**Answer:** $0$

The trigram `"is in time."` (or another required trigram in the sentence) never appears in the training corpus, so the trigram model assigns probability 0 to the sentence.

# END SOLUTION

# END SUBPROB

# END PROB
