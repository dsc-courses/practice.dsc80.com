# BEGIN PROB

Suppose it is known that the person who collected this data set often neglected
to enter an urgency for tasks that they knew would take less than 5 minutes, and that
this factor was the most important in the missingness in the \col{urgency} column.

What is the most likely type of missingness for the missing values in the \col{urgency}
column?

\byversion{
    \begin{choices}
        \choice Missing by Design
        \choice Missing Completely at Random
        \choice Not Missing at Random
        \correctchoice Missing at Random
    \end{choices}
}{
    \begin{choices}
        \correctchoice Missing at Random
        \choice Not Missing at Random
        \choice Missing Completely at Random
        \choice Missing by Design
    \end{choices}
}

This question is designed to have a single most likely answer. However, you can \emph{optionally} provide
a justification for your answer below.
If your answer above is correct, you will get full credit even if you do not
provide justification. However, if your answer above is wrong, you may receive
some credit if you provide justification and it is reasonable.

# BEGIN SOLN

Because the most important factor in the missingness of values in the \col{urgency} column
is the value in another column, this is MAR.

You might argue that this is NMAR, since tasks which take less than 5 minutes are likely to be
less urgent, so there is an association between the uknown urgency and its missingness. However,
the main factor is the time required, and so this should be MAR. That is, if we already
know the time taken, learning the missing urgency does not provide much more information
about the missingness of the urgency.
To put it more formally, the probability
of missingness conditioned upon the time taken and the uknown urgency is not significantly different
from the probability of missingness conditioned only on the time taken.

78

# END SOLN


# END PROB