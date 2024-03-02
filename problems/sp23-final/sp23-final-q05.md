# BEGIN PROB

# BEGIN SUBPROB

Which are examples of nested data formats? Select all that apply.

[ ] XML [ ] CSV [ ] JSON [ ] HTML

# BEGIN SOLUTION

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

To measure the similarity between two word vectors $\vec{a}$ and
$\vec{b}$, we compute their normalized dot product, also known as their
cosine similarity.

$\text{Cosine Similarity} = \cos \theta = \boxed{\frac{\vec{a} \cdot \vec{b}}{|\vec{a}| | \vec{b}|}}$

Which equation describes the cosine distance metric?

( ) $\cos \theta - 1$

( ) $1- \cos \theta$

( ) $\cos \theta \cdot |\vec{a}| | \vec{b}|$

( ) $(\cos \theta)^{-1}$

# BEGIN SOLUTION

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Chen downloaded 4 independent reviews of a new vacuum cleaner from
Amazon (as shown in the 4 sentences below).

        Sentence 1: 'if i could give this vacuum zero stars i would'
        Sentence 2: 'i will not order again this vacuum is garbage'
        Sentence 3: 'Love Love Love i love this product'
        Sentence 4: 'this little vacuum is so much fun to use i love it'

*X* is the 'Term frequency-Inverse Document Frequency (TF-IDF)' of the
word 'vacuum' in sentence 1.

Chen replaces sentence 3 with the following new sentence/review.

        New Sentence 3: 'Love Love Love i love this vacuum'

*Y* is the 'TF-IDF' of the word 'vacuum' in sentence 1 after the
sentence 3 is replaced by the new sentence 3.\
Given the above information, which of the following statements is true?

( ) $X=Y$

( ) $X>Y>0$

( ) $X>0$ and $Y=0$

( ) $X>0$ and $Y>X$

# BEGIN SOLUTION

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Consider the five expressions in the following Series, sentences.

    sentences = pd.Series([
        'buffalo monkey giraffe buffalo buffalo buffalo',
        'buffalo giraffe',
        'giraffe monkey',
        'deer monkey',
        'buffalo'
    ])

We convert all the expressions in the sentences series to a bag of words
representation with the following words (also known as dictionary):

        {buffalo, monkey, giraffe, deer}

Which expression will achieve the highest similarity with
`sentences.iloc[0]` if we use the **un-normalized dot product** between
the bag of words (i.e., $\vec{a} \cdot \vec{b}$) as the similarity
metric?

( ) 'buffalo giraffe'

( ) 'giraffe monkey'

( ) 'deer monkey'

( ) 'buffalo'

Which expression will achieve the highest similarity with
sentences.iloc\[0\] if we use **cosine similarity** between the bag of
words as the similarity metric?

*Hint: $\sqrt{18}=3\sqrt{2}$, $\frac{2}{\sqrt{2}}=\sqrt{2}$,
$4\sqrt{2}=5.65$*

( ) 'buffalo giraffe'

( ) 'giraffe monkey'

( ) 'deer monkey'

( ) 'buffalo'

# BEGIN SOLUTION

# END SOLUTION

# END SUBPROB

# END PROB