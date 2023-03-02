# BEGIN PROB

For this problem, consider the following data set of product reviews.

<center><img src='../assets/images/fa21-final/reviews.png' width=50%></center>
        

# BEGIN SUBPROB

What is the Inverse Document Frequency (IDF) of the word "are" in the `review` column? Use base-10 log in your computations.

# BEGIN SOLN

**Answer: ** 0

The IDF is computed by the logarithm of the quotient of total number of documents divided by number of documents with the said term in it. Since there are 6 documents and all 6 have the word "are" in it, we the IDF is just $\log{(\frac{6}{6})}$ which is just 0.

<average>97</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

Calculate the TF-IDF score of "keyboard" in the last review. Use the base-10 logarithm in your calculation.

# BEGIN SOLN

**Answer: ** 0.119

TF is just the number of times a term appears in a document divided by the number of terms in a document. Thus the TF score of "keyboard" in the last review is just $\frac{1}{4}$

The IDF score is just $log{(\frac{6}{2})}$, since there are 2 documents with "keyboard" in it and documents total.

Thus multiplying $\frac{1}{4} \times \log{(\frac{6}{2})}$ yields 0.119.

<average>81</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

The music store wants to predict rating using other features in the dataset. Before that, we have to deal with the categorical variables - `music_level`, and `product_name`.
How should you encode the `music_level` variable for the modeling?

( ) One-hot encoding
( ) Bag of words
( ) Ordinal encoding
( ) Tf-Idf

# BEGIN SOLN

**Answer: ** Option C

In ordinal encoding, each unique category is assigned an integer value. Thus it would make sense to encode `music_level` with Ordinal encoding since there an inherent order to `music_level`. i.e. 'Grade IV' would be "higher" than 'Grade I' in `music_level`. 

Bag of words doesn't work since we're not necessarily trying to encode multi-worded strings, and TF-IDF simply doesn't make sense for encoding. One-hot encoding doesn't work as well in this case since `music_level` is an ordinal categorical variable.

<average>100</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

How should you encode the `product_name` variable for the modeling?

( ) One-hot encoding
( ) Bag of words
( ) Ordinal encoding
( ) Tf-Idf

<average>98</average>

# BEGIN SOLN

**Answer: ** Option A

Since `product_name` is a nominal categorical variable, it would make sense to encode it using `One-hot encoding`. Ordinal encoding wouldn't work this time since `product_name` is not an ordinal categorical variable. We could eliminate the rest of the options from similar reasoning as the question above.

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

True or False: the TF-IDF score of a term depends on the document containing it.

( ) True
( ) False

# BEGIN SOLN

**Answer: ** True

TF is calculated by the number of times a term appears in a document divided by the number of terms in the document, which depends on the document itself. So if TF depends on the document itself, so does the TF-IDF score.

<average>97</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

Suppose you perform a one-hot encoding of a Series containing the following music genres:

```py
[
   "hip hop",
   "country",
   "polka",
   "country",
   "pop",
   "pop",
   "hip hop"
]
```

Assume that the encoding is created using `OneHotEncoder(drop='first')` transformer from `sklearn.preprocessing` (note the `drop='first'`) keyword.

How many columns will the one-hot encoding table have?

# BEGIN SOLN

**Answer: ** 3

Normal One-hot encoding will yield 4 columns, one for each of the following categories: "hip-hop", "country", "polka", and "pop". However, `drop='first'` will drop the first column after One-hot encoding which will yield 4 - 1 = 3 columns. 

<average>80</average>

# END SOLN

# END SUBPROB

# END PROB