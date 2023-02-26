# BEGIN PROB

Ethan is an avid Star Wars fan, and the only streaming service he has an
account on is Disney+. (He had a Netflix account, but then Netflix
cracked down on password sharing.)

Fill in the blanks below so that `star_disney_prop` evaluates to the
proportion of TV shows in `tv` with `"Star Wars"` in the title that are
available to stream on Disney+.

```py
star_only = __(a)__
star_disney_prop = __(b)__ / star_only.shape[0]
```

What goes in the blanks?

# BEGIN SOLN

**Answers**:

- Blank (a): `tv[tv["Title"].str.contains("Star Wars")]`
- Blank (b): `star_only["Disney+"].sum()`

We're asked to find the proportion of TV shows with `"Star Wars"` in the title that are available to stream on Disney+. This is a fraction, where:

- The numerator is the number of TV shows that have `"Star Wars"` in the title **and** are available to stream on Disney+.
- The denominator is the number of TV shows that have `"Star Wars"` in the title.

The key is recognizing that `star_only` must be a DataFrame that contains all the rows in which the `"Title"` contains `"Star Wars"`; to create this DataFrame in blank (a), we use `tv[tv["Title"].str.contains("Star Wars")]`. Then, the denominator is already provided for us, and all we need to fill in is the numerator. There are a few possibilities, though they all include `star_only`:

- `star_only["Disney+"].sum()`
- `(star_only["Disney+"] == 1).sum()`
- `star_only[star_only["Disney+"] == 1].shape[0]`

**Common misconception**: Many students calculated the wrong proportion: they calculated the proportion of shows available to stream on Disney+ that have `"Star Wars"` in the title. We asked for the proportion of shows with `"Star Wars"` in the title that are available to stream on Disney+; "proportion of $X$ that $Y$" is always $\frac{\# X \text{ and } Y}{\# X}$.

<average>84</average>

# END SOLN

# END PROB