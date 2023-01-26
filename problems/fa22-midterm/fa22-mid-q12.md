# BEGIN PROB

Suppose you are performing a permutation test to check the following hypotheses:

\begin{itemize}
    \item \textbf{Null}: The time required to complete tasks in the ``hobbies'' category is drawn from
        the same distribution as the time required to complete tasks in the ``finance'' category.
    \item \textbf{Alternative}: The time required to complete tasks in the ``hobbies'' category is drawn from
        a different distribution as the time required to complete tasks in the ``finance'' category.
\end{itemize}

When you plot a histogram for the distribution of times taken to complete tasks in each categories,
you see the below:

\begin{center}
    \includegraphics[width=3.5in]{./fig/minutes-hobbies_and_finance.pdf}
\end{center}

What is the \emph{best} test statistic for this test?

\byversion{
    \begin{choices}
        \correctchoice the Kolmogorov-Smirnov statistic
        \choice the Total Variation Distance
        \choice the \emph{signed} difference between the mean time taken for ``finance'' tasks, minus
        the mean time taken for ``hobbies'' tasks.
        \choice the maximum time taken for ``finance'' tasks, minus the maximum time taken for
        ``hobbies'' tasks
    \end{choices}
}{
    \begin{choices}
        \choice the Total Variation Distance
        \correctchoice the Kolmogorov-Smirnov statistic
        \choice the maximum time taken for ``finance'' tasks, minus the maximum time taken for
        ``hobbies'' tasks
        \choice the \emph{signed} difference between the mean time taken for ``finance'' tasks, minus
        the mean time taken for ``hobbies'' tasks.
    \end{choices}
}

81

# END PROB