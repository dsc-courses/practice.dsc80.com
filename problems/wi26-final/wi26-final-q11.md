# BEGIN PROB

Suppose we train a unigram, bigram, and trigram model on the following
corpus.

    corpus = "Patient is ill. Patient is in pain. Ill patient will recover 
              in time."

We tokenized the corpus as follows before training our models.

    corpus.lower().split()

Now, we'd like to determine the probability of generating the sentence
below, according to each model.

    "Patient is in time."

For each part, give your answer as a simplified fraction (preferred) or
a product of simplified fractions.

# BEGIN SUBPROB

Determine the probability of the sentence above, according to the
unigram model.

# BEGIN SOLUTION

**Answer:** $\frac{3}{13} \cdot \frac{2}{13} \cdot \frac{2}{13} \cdot \frac{1}{13}$

After tokenization, the corpus has 13 tokens: `"patient"` appears 3 times, `"is"` and `"in"` each appear 2 times, and `"time."` appears once. Under a unigram model, we multiply the probability of each token independently:

$$P(\text{patient}) \cdot P(\text{is}) \cdot P(\text{in}) \cdot P(\text{time.}) = \frac{3}{13} \cdot \frac{2}{13} \cdot \frac{2}{13} \cdot \frac{1}{13}$$

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Determine the probability of the sentence above, according to the bigram
model.

# BEGIN SOLUTION

**Answer:** $\frac{1}{26}$

For a bigram model, we use the unigram probability of the first token and then multiply conditional probabilities for each subsequent token. From the corpus:

- $P(\text{patient}) = \frac{3}{13}$
- $P(\text{is} \mid \text{patient}) = \frac{2}{3}$ (2 of 3 times `"patient"` is followed by `"is"`)
- $P(\text{in} \mid \text{is}) = \frac{1}{2}$ (1 of 2 times `"is"` is followed by `"in"`)
- $P(\text{time.} \mid \text{in}) = \frac{1}{2}$ (1 of 2 times `"in"` is followed by `"time."`)

Multiplying gives $\frac{3}{13} \cdot \frac{2}{3} \cdot \frac{1}{2} \cdot \frac{1}{2} = \frac{1}{26}$.

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Determine the probability of the sentence above, according to the
trigram model.

# BEGIN SOLUTION

**Answer:** $0$

A trigram model conditions each token on the previous two tokens. The sentence `"patient is in time."` requires the trigram `("is", "in", "time.")`, but in the training corpus `"is"` followed by `"in"` is always followed by `"pain."`, never `"time."`. Since this trigram never appears in the corpus, its probability is 0, so the probability of the entire sentence is 0.

# END SOLUTION

# END SUBPROB

# END PROB
