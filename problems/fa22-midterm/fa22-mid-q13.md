# BEGIN PROB

What is the most likely type of missingness for the missing values in the \col{client} column of \python{tasks}?

Hint: look at the description of the \col{client} column at the beginning of the exam for information
on when missing values appear.

\byversion{
    \begin{choices}
        \correctchoice Missing by Design
        \choice Missing Completely at Random
        \choice Not Missing at Random
        \choice Missing at Random
    \end{choices}
}{
    \begin{choices}
        \choice Missing at Random
        \choice Not Missing at Random
        \choice Missing Completely at Random
        \correctchoice Missing by Design
    \end{choices}
}

This question is designed to have a single most likely answer. However, you can \emph{optionally} provide
a justification for your answer below.
If your answer above is correct, you will get full credit even if you do not
provide justification. However, if your answer above is wrong, you may receive
some credit if you provide justification and it is reasonable.

# BEGIN SOLN

\col{client} is missing if and only if the category is not 
``consulting''. This means that
we can exactly predict when a value is missing in \col{client}. This is the definition of
missing by design.

61
# END SOLN

# END PROB