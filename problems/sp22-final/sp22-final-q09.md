# BEGIN PROB

Recall from Project 4, a trigram is an N-Gram with $N=3$. Below, we
instantiate a trigram language model with a list of 12 tokens.

    # \x02 means start of paragraph, \x03 means end of paragraph
    tokens = ["\x02", "hi", "my", "name", "is", "what", 
              "my", "name", "is", "who", "my", "\x03"]

    lm = NGramLM(3, tokens)

What does `lm.probability(("name", "is", "what", "my"))` evaluate to? In
other words, what is $P(\text{name is what my})$? **Show your work in
the box below, and give your final answer as a simplified fraction in
the box at the bottom of the page.**

*Hint: Do not perform any unnecessary computation --- only compute the
conditional probabilities that are needed to evaluate
$P(\text{name is what my})$.*

# BEGIN SOLN

**Answer: ** $\frac{1}{12}$

Since we are using a trigram model, to compute the conditional
probability of a token, we must condition on the prior two tokens. For
the first and second tokens, `"name"` and `"is"`, there aren't two prior
tokens to condition on, so we instead look at unigrams and bigrams
instead.

First, we decompose $P(\text{name is what my})$:

$$\begin{aligned}
P(\text{name is what my}) &= P(\text{name}) \cdot P(\text{is $|$ name}) \cdot P(\text{what $|$ name is}) \cdot P(\text{my $|$ is what}) \end{aligned}$$

-   $P(\text{name})$ is $\frac{2}{12}$, since there are 12 total tokens
    and 2 of them are equal to `"name"`.

-   $P(\text{is $|$ name})$ is $\frac{2}{2} = 1$, because of the 2 times
    `"name"` appears, `"is"` always follows it.

-   $P(\text{what $|$ name is})$ is $\frac{1}{2}$, because of the 2
    times `"name is"` appears, `"what"` follows it once (`"who"` follows
    it the other time).

-   $P(\text{my $|$ is what})$ is $\frac{1}{1} = 1$, because `"is what"`
    only appeared once, and `"my"` appeared right after it.

Thus: $$\begin{aligned}
P(\text{name is what my}) &= P(\text{name}) \cdot P(\text{is $|$ name}) \cdot P(\text{what $|$ name is}) \cdot P(\text{my $|$ is what}) \\ &= \frac{2}{12} \cdot 1 \cdot \frac{1}{2} \cdot 1 \\ &= \frac{1}{12}  \end{aligned}$$

<average>57</average>

# END SOLN

# END PROB