# BEGIN PROB

Fill in the code below so that it computes a Series containing, for each
category, the proportion of completed tasks which took more than 30 minutes to complete. That is, out of all tasks which were completed in a given category, what percentage took more than 30 minutes?

\begin{minted}[autogobble,escapeinside=||]{python}
    def proportion_more_than_30(df):
        |\drawcodebox{5in}{1in}|

    result = (
        tasks.groupby('category')[['completed', 'minutes']]
        .|\drawcodebox{2in}{3em}|(proportion_more_than_30)
    )
\end{minted}

\begin{soln}
    \inputminted{python}{\thisdir/code.py}
\end{soln}

73

# END PROB