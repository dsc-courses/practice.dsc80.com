# BEGIN PROB

Let's consider admissions at UC San Diego and UC Santa Barbara for two
high schools in particular.

<center><img src='../assets/images/sp22-midterm/simpson.png' width=40%></center>

For instance, the above table tells us that 200 students from La Jolla
Private applied to UC San Diego, and 50 were admitted.

What is the largest possible integer value of $N$ such that:

-   UC Santa Barbara has a strictly higher admit rate for **both** La
    Jolla Private and Sun God Memorial High individually, but

-   UC San Diego has a strictly higher admit rate overall?

# BEGIN SOLN

**Answer: **124

Let's consider the two conditions separately.

First, UC Santa Barbara needs to have a higher admit rate for both high
schools. This is already true for La Jolla Private
($\frac{100}{300} > \frac{50}{200}$); for Sun God Memorial High, we just
need to ensure that $\frac{N}{150} > \frac{200}{300}$. This means that
$N > 100$.

Now, UC San Diego needs to have a higher admit rate overall. The UC San
Diego admit rate is
$\frac{50+200}{200+300} = \frac{250}{500} = \frac{1}{2}$, while the UC
Santa Barbara admit rate is $\frac{100 + N}{450}$. This means that we
must require that $\frac{1}{2} = \frac{225}{450} > \frac{100+N}{450}$.
This means that $225 > 100 + N$, i.e. that $N < 125$.

So there are two conditions on $N$: $N > 100$ and $N < 125$. The largest
integer $N$ that satisfies these conditions is $N=124$, which is the
final answer.

<average>72</average>

# END SOLN

# END PROB