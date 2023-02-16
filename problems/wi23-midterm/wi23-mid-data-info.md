**Welcome to the Midterm Exam for DSC 80 in Winter 2023!**

Throughout this exam, we will work with the DataFrame `tv`, which contains information about various TV shows available to watch on streaming services. For each TV show, we have:

-  `"Title" (object)`: The title of the TV show.
-  `"Year" (int)`: The year in which the TV show was first released. (For instance, the show _How I Met Your Mother_ ran from 2005 to 2014; there is only one row for _How I Met Your Mother_ in `tv`, and its `"Year"` value is 2005.)
-  `"Age" (object)`: The age category for the TV show. If not missing, `"Age"` is one of `"all"`, `"7+"`, `"13+"`, `"16+"`, or `"18+"`. (For instance, `"all"` means that the show is appropriate for all audiences, while `"18+"} means that the show contains mature content and viewers should be at least 18 years old.)
-  `"IMDb" (float)`: The TV show's rating on IMDb (between 0 and 10).
-  `"Rotten Tomatoes" (int)`: The TV show's rating on Rotten Tomatoes (between 0 and 100).
-  `"Netflix" (int)`: 1 if the show is available for streaming on Netflix and 0 otherwise. The `"Hulu"`, `"Prime Video"`, and `"Disney+"` columns work the same way.

The first few rows of `tv` are shown below (though `tv` has many more rows than are pictured here).

<center><img src='../assets/images/wi23-midterm/data-info-wi23-mt.png' width=65%></center>

Assume that we have already run all of the necessary imports.

**Throughout this exam, we will refer to `tv` repeatedly.**
