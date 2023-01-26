# BEGIN PROB

The code below creates a pivot table.

\begin{minted}[autogobble]{python}
    pt = tasks.pivot_table(
        index='urgency', columns='category', values='completed', aggfunc='sum'
    )
\end{minted}

Which of the below pieces of code will produce the same result as \python{pt.loc[3.0, 'consulting']}?
\textbf{Mark all which apply.}

\byversion{
    \begin{choices}
        \correctchoice \inputminted[firstline=1,lastline=5]{python}{\thisdir/code.py}
        \correctchoice \inputminted[firstline=7,lastline=11]{python}{\thisdir/code.py}
        \choice \inputminted[firstline=13,lastline=13]{python}{\thisdir/code.py}
        \correctchoice \inputminted[firstline=15,lastline=18]{python}{\thisdir/code.py}
        \choice \python{tasks.groupby('completed').sum().loc[(3.0, 'consulting')]}
    \end{choices}
}{
    \begin{choices}
        \choice \python{tasks.groupby('completed').sum().loc[(3.0, 'consulting')]}
        \correctchoice \inputminted[firstline=1,lastline=5]{python}{\thisdir/code.py}
        \choice \inputminted[firstline=13,lastline=13]{python}{\thisdir/code.py}
        \correctchoice \inputminted[firstline=15,lastline=18]{python}{\thisdir/code.py}
        \correctchoice \inputminted[firstline=7,lastline=11]{python}{\thisdir/code.py}
    \end{choices}
}


76
# END PROB