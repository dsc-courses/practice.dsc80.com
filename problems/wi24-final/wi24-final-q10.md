# BEGIN PROB

Harshi is trying to build a decision tree that predicts whether or not a hotel has a swimming pool.

Suppose $+$ represents the “has pool” class and $\circ$ represents the “no pool” class. One of the nodes in Harshi’s decision tree has 12 points, with the following distribution of classes.

$$++++\circ\circ\circ\circ\circ\circ\circ\,\circ$$

Consider the following three splits of the node above.

Split 1:

- Yes: $++\circ\circ\circ\,\circ$
- No: $++\circ\circ\circ\,\circ$

Split 2:

- Yes: $++\circ\circ\circ\circ\circ\circ\circ$
- No: $++\circ$

Split 3:

- Yes: $\circ$
- No: $++++\circ\circ\circ\circ\circ\circ\circ$

# BEGIN SUBPROB

Which of the six nodes above have the same entropy as the original node? Select all that apply.

[ ] Split 1’s “Yes” node 
[ ] Split 1’s “No” node
[ ] Split 2’s “Yes” node
[ ] Split 2’s “No” node
[ ] Split 3’s “Yes” node
[ ] Split 3’s “No” node

# BEGIN SOLUTION

**Answer:** Split 1’s “Yes” node, Split 1’s “No” node, and Split 2’s “No” node

The definition of entropy for a node is:

$$\text{entropy} = - \sum_C p_C \log_2 p_C$$

where $C$ is each label class, and $p_C$ is the proportion of points in the node in class $C$.

We can note that in binary classification, two nodes will have the same entropy if they have the same relative distribution of classes, or if the distributions of classes are complements of each other. (For example, a node with 75% positives and 25% negatives has the same entropy as a node with 25% positives and 75% negatives.) So, in this problem, we need only find nodes with the same proportions as the original node, which has 4 positives ($\frac{1}{3}$) and 8 negatives ($\frac{2}{3}$).

<average>88</average>

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Which of the six nodes above have the lowest entropy? If there are multiple correct answers, select them all.

[ ] Split 1’s “Yes” node 
[ ] Split 1’s “No” node
[ ] Split 2’s “Yes” node
[ ] Split 2’s “No” node
[ ] Split 3’s “Yes” node
[ ] Split 3’s “No” node

# BEGIN SOLUTION

**Answer:** Split 3’s “Yes” node

The lowest possible entropy for a distribution occurs when it takes on only one value. In the definition of entropy, $\log_2 p_C$ will be 0 when $p_C$ is 1, so entropy will be zero when all points are of the same class. This only occurs in one of the given nodes, Split 3’s “Yes” node.

<average>93</average>

# END SOLUTION

# END SUBPROB

# END PROB