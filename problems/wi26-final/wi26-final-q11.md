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

**Answer:** '3/13 \* 2/13 \* 2/13 \* 1/13'

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Determine the probability of the sentence above, according to the bigram
model.

# BEGIN SOLUTION

**Answer:** '1/26'

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Determine the probability of the sentence above, according to the
trigram model.

# BEGIN SOLUTION

**Answer:** '0'

# END SOLUTION

# END SUBPROB

# END PROB