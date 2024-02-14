The DataFrame `sat` contains one row for **most** combinations of `"Year"` and `"State"`, where `"Year"` ranges between `2005` and `2015` and `"State"` is one of the 50 states (not including the District of Columbia).

The other columns are as follows:

-   `"# Students"` contains the number of students who took the SAT in that state in that year.

-   `"Math"` contains the mean math section score among all students who took the SAT in that state in that year. This ranges from 200 to 800.

-   `"Verbal"` contains the mean verbal section score among all students who took the SAT in that state in that year. This ranges from 200 to 800. (This is now known as the "Critical Reading" section.)


The first few rows of `sat` are shown below  (though `sat` has many more rows than are pictured here).

<center><img src='../assets/images/wi23-final/df.png' width=40%></center>

For instance, the first row of `sat` tells us that 41227 students took the SAT in Washington in 2014, and among those students, the mean math score was 519 and the mean verbal score was 510.

Assume:

-   `sat` does not contain any duplicate rows --- that is, there is only one row for every unique combination of `"Year"` and `"State"` that is in `sat`.

-   `sat` does not contain any null values.

-   We have already run all of the necessary imports.
