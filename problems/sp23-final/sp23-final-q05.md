# BEGIN PROB

# BEGIN SUBPROB

Which are examples of nested data formats? Select all that apply.

[ ] XML
[ ] CSV
[ ] JSON
[ ] HTML

# BEGIN SOLN
**Answer:** XML, JSON, HTML

CSV is not a nested data format, but is in a flat format, representing data in a 2d structure.
  
# END SOLN

# END SUBPROB

# BEGIN SUBPROB

To measure the similarity between two word vectors $\vec{a}$ and $\vec{b}$, we compute their normalized dot product, also known as their cosine similarity.

$$
\text{Cosine Similarity} = \cos  \theta = \boxed{\frac{\vec{a} \cdot  \vec{b}}{|\vec{a}| | \vec{b}|}}
$$

Which equation describes the cosine distance metric?

( ) $\cos  \theta - 1$
( ) $1- \cos  \theta$
( ) $\cos  \theta  \cdot |\vec{a}| | \vec{b}|$
( ) $(\cos  \theta)^{-1}$

# BEGIN SOLN
**Answer:** $1 - cos(\theta)$

Cosine similarity ranges from 0 to 1, and therefore cosine dissimilarity (or distance)
must be the difference between 1 and the cosine similarity (consider that cosine similarity of 
0 should mean distance of 1, and vice versa). Therefore cosine distance is $1 - cos(\theta)$.

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

Chen downloaded 4 independent reviews of a new vacuum cleaner from Amazon (as shown in the 4 sentences below).

```
	Sentence 1: 'if i could give this vacuum zero stars i would'
	Sentence 2: 'i will not order again this vacuum is garbage'
	Sentence 3: 'Love Love Love i love this product'
	Sentence 4: 'this little vacuum is so much fun to use i love it'
```

*X* is the 'Term frequency-Inverse Document Frequency (TF-IDF)' of the word 'vacuum' in sentence 1.

Chen replaces sentence 3 with the following new sentence/review.

```
	New Sentence 3: 'Love Love Love i love this vacuum'
```

*Y* is the 'TF-IDF' of the word 'vacuum' in sentence 1 after the sentence 3 is replaced by the new sentence 3.

Given the above information, which of the following statements is true?

( ) $X=Y$
( ) $X>Y>0$
( ) $X>0$ and $Y=0$
( ) $X>0$ and $Y>X$

# BEGIN SOLN
**Answer:** $X > 0$ & $Y = 0$

To find X: \
TF = $\frac{1}{10}$ \
IDF = $log_2\frac{4}{3}$ \
TF-IDF $\approx$ 0.415 \
So X > 0  

To find Y: \
TF = $\frac{1}{10}$ \
IDF = $log_2\frac{4}{4}$ \
TF-IDF = 0 \
So Y = 0  

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

Consider the five expressions in the following Series, sentences.

```py
sentences = pd.Series([
	'buffalo monkey giraffe buffalo buffalo buffalo',
	'buffalo giraffe',
	'giraffe monkey',
	'deer monkey',
	'buffalo'
])
```

We convert all the expressions in the sentences series to a bag of words representation with the following words (also known as dictionary):

```py
{buffalo, monkey, giraffe, deer}
```

Which expression will achieve the highest similarity with

`sentences.iloc[0]` if we use the **un-normalized dot product** between the bag of words (i.e., $\vec{a} \cdot  \vec{b}$) as the similarity metric?

( ) `'buffalo giraffe'`
( ) `'giraffe monkey'`
( ) `'deer monkey'`
( ) `'buffalo'`

# BEGIN SOLN
**Answer:** 'buffalo giraffe'

Bag of words for `sentences.iloc[0]` ('buffalo monkey giraffe buffalo buffalo buffalo') is 
(4, 1, 1, 0)

Bag of words and products for the expressions are: 

'buffalo giraffe': \
bow: (1, 0, 1, 0) \
product: 5

'giraffe monkey': \
bow: (0, 1, 1, 0) \
product: 2

'deer monkey': \
bow: (0, 1, 0, 1) \
product: 1

'buffalo': \
bow: (1, 0, 0, 0) \
product: 4

So 'buffalo giraffe' maximizes the similarity metric.


# END SOLN

# END SUBPROB

# BEGIN SUBPROB

Which expression will achieve the highest similarity with

`sentences.iloc[0]` if we use **cosine similarity** between the bag of words as the similarity metric?
*Hint:* $\sqrt{18}=3\sqrt{2}$, $\frac{2}{\sqrt{2}}=\sqrt{2}$, $4\sqrt{2}=5.65$*

( ) `'buffalo giraffe'`
( ) `'giraffe monkey'`
( ) `'deer monkey'`
( ) `'buffalo'`

# BEGIN SOLN
**Answer:** 'buffalo'

Bag of words for `sentences.iloc[0]` ('buffalo monkey giraffe buffalo buffalo buffalo') is 
(4, 1, 1, 0), so the norm is $\sqrt{18} = 3\sqrt{2}$

Calculating the cosine similarity for each expression:

'buffalo giraffe': \
bow: (1, 0, 1, 0) \
similarity: $\frac{5}{6}$

'giraffe monkey': \
bow: (0, 1, 1, 0) \
similarity: $\frac{1}{3}$

'deer monkey': \
bow: (0, 1, 0, 1) \
similarity: $\frac{1}{6}$

'buffalo': \
bow: (1, 0, 0, 0) \
similarity: $\frac{2\sqrt{2}}{3}$

So 'buffalo' maximizes the similarity metric.

# END SOLN

# END SUBPROB

# END PROB