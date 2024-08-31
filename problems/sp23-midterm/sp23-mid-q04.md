# BEGIN PROB

# BEGIN SUBPROB

Find the average sleep duration for people who use "Gaming PC" as their
gaming platform in the `demo` DataFrame. If the `Gamer ID` in the `demo`
is not in the `health` DataFrame, use `NaN` as the average sleep
duration. Fill in the blanks below so that the code evaluates to a
DataFrame containing the `Gamer ID` and corresponding
`Average Sleep Duration`.

    demo[--(a)--].merge(

        health, left_on = "Gamer ID", --(b)--
        
    )[['Gamer ID', 'Average Sleep Duration']]

(1.5 pts) What goes in (a)?

::: responsebox
0.5in
:::

(1.5 pts) What goes in (b)?

::: responsebox
0.5in
:::

# BEGIN SOLUTION

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

![image](midterm_images/question3_b_demo.png){width="2.3in"}
![image](midterm_images/question3_b_health.png){width="3.8in"}

(demo)(health)\
Given the above information, if we perform the following code:\

        health_demo = pd.concat([health, demo], axis = 1)

How many `NaN` values will be in `health_demo`?

# BEGIN SOLUTION

# END SOLUTION

# END SUBPROB

# END PROB