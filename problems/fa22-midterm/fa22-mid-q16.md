# BEGIN PROB

Suppose it is determined that the missingness in the \col{urgency} column is Missing at Random due to an association
with the \col{category} column, and that tasks in the ``work'' category are least likely to be missing an urgency.
You can assume that tasks in the ``work'' category have higher-than-average urgencies.

Suppose the missing urgencies are imputed by randomly sampling from the observed urgencies. If the mean urgency of
tasks in the ``hobbies'' category is computed, what is likely to be true?

\byversion{
    \begin{choices}
        \choice It will be unbiased.
        \correctchoice It will be biased high (higher than the true average).
        \choice It will be biased low (lower than the true average).
    \end{choices}
}{
    \begin{choices}
        \choice It will be biased low (lower than the true average).
        \correctchoice It will be biased high (higher than the true average).
        \choice It will be unbiased.
    \end{choices}
}

80

# END PROB

