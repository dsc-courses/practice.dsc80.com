# BEGIN PROB

You observe that tasks in the ``consulting'' category seem to be completed
at a higher rate than tasks in the ``work'' category. Could this be due to
chance? To check, you'll run a permutation test. Your hypotheses are:
\begin{itemize}
    \item \textbf{Null}: The true probability of completing a ``work'' task is the same as the probability of completing a ``consulting'' task.
    \item \textbf{Alternative}: The true probability of completing a ``consulting'' is higher than the probability of completing a ``work'' task.
\end{itemize}

In the box below, write code which performs a permutation test and computes a $p$-value.
The choice of an appropriate test statistic is left to you. You should check 10,000
permutations.

Note: you do not need to do anything special to account for missing values.

# BEGIN SOLN

For test statistic, we'll use the signed difference between the
proportion of ``consulting'' tasks which are completed, and the
proportion of ``work'' tasks which are completed.

\inputminted{python}{\thisdir/code.py}

82
# END SOLN

# END PROB