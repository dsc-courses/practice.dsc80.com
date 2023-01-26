# BEGIN PROB

Suppose the date of each task has been collected in a Series named \python{dates}, shown below:

\begin{minted}[autogobble]{python}
    >>> dates
    7377   2019-08-31
    7378   2019-08-31
    7379   2019-09-01
    7380   2019-09-02
    7381   2019-09-02
                ...    
    9831   2022-10-28
    9832   2022-10-29
    9833   2022-10-29
    9834   2022-10-30
    9835   2022-10-30
    Length: 2459, dtype: datetime64[ns]
\end{minted}

You may assume that the index of \python{dates} contains the task identifier, and that these identifiers
correspond to the same identifiers used in the index of \python{tasks}.
Note that dates have only been collected for the last 2459 tasks.

What will happen if we try to run the following line of code?

\python{tasks['date'] = dates}

\byversion{
    \begin{choices}
        \choice A new row will be created with index "date".
        \correctchoice A new column will be created with missing values in the ``date'' column for tasks that
        are not in \python{dates}.
        \choice An exception will be raised because some tasks are missing (the size of \python{dates}
        is not the same as the size of \python{tasks}.)
        \choice An exception will be raised because \python{tasks} does not have a column named ``date''.
    \end{choices}
}{
    \begin{choices}
        \choice An exception will be raised because some tasks are missing (the size of \python{dates}
        is not the same as the size of \python{tasks}.)
        \choice An exception will be raised because \python{tasks} does not have a column named ``date''.
        \correctchoice A new column will be created with missing values in the ``date'' column for tasks that
        are not in \python{dates}.
        \choice A new row will be created with index "date".
    \end{choices}
}


57
# END PROB