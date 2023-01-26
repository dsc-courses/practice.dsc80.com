# BEGIN PROB

Suppose that in addition to \python{tasks}, you have the dataframe named
\python{clients}, shown below:

\begin{center}
    \includegraphics[scale=.75]{./fig/clients.png}
\end{center}

The index of the dataframe contains the names of clients that have been
consulted for, the \col{rate} column contains the pay rate (in dollars per
hour), and the \col{active} column says whether the client is actively
being consulted for. Note that the clients which appear in \python{clients}
are not exactly the same as the clients that appear in
\python{tasks["client"].value_counts()}! That is, there is a client in
\python{tasks["client"]} which is not in \python{clients}, and a client
that is in \python{clients} that does not appear in \python{tasks}.

Fill in the code below so that it produces a dataframe which has all of the
columns that appear in \python{tasks}, but with two additional columns,
\col{rate} and \col{activity}, listing the pay rate for each task and
whether the client being consulted for is still active. The number of rows
in your resulting dataframe should be equal to the number of rows in
\python{tasks} for which the value in \col{client} is in \python{clients}.

\begin{minted}[autogobble,escapeinside=||]{python}
    tasks.merge(
        clients,
        how=|\drawcodebox{2in}{3em}|,
        |\drawcodebox{4in}{3em}|,
        |\drawcodebox{4in}{3em}|
    )
\end{minted}


78
# END PROB