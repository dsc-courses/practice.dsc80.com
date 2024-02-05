# BEGIN PROB

After taking the SAT, Nicole wants to check the College Board's website to see her score. However, the College Board recently updated their website to use non-standard HTML tags and Nicole's browser can't render it correctly. As such, she resorts to making a GET request to the site with her scores on it to get back the source HTML and tries to parse it with BeautifulSoup.

Suppose `soup` is a BeautifulSoup object instantiated using the following HTML document.

```html
<college>Your score is ready!</college>

<sat verbal="ready" math="ready">
  Your percentiles are as follows:
  <scorelist listtype="percentiles">
    <scorerow kind="verbal" subkind="per">
      Verbal: <scorenum>84</scorenum>
    </scorerow>
    <scorerow kind="math" subkind="per">
      Math: <scorenum>99</scorenum>
    </scorerow>
  </scorelist>
  And your actual scores are as follows:
  <scorelist listtype="scores">
    <scorerow kind="verbal"> Verbal: <scorenum>680</scorenum> </scorerow>
    <scorerow kind="math"> Math: <scorenum>800</scorenum> </scorerow>
  </scorelist>
</sat>
```

# BEGIN SUBPROB

Which of the following expressions evaluate to `"verbal"`? Select all that apply.

[ ] `soup.find("scorerow").get("kind")`
[ ] `soup.find("sat").get("ready")`
[ ] `soup.find("scorerow").text.split(":")[0].lower()`
[ ] `[s.get("kind") for s in soup.find_all("scorerow")][-2]`
[ ] `soup.find("scorelist", attrs={"listtype":"scores"}).get("kind")`
[ ] None of the above

# BEGIN SOLN

**Answer: ** Option 1, Option 3, Option 4

`Option 1` expression finds the first `<scorerow>` element and retrieves its kind attribute, which is `"verbal"` for the first `<scorerow>` encountered in the HTML document.

`Option 2` finds the first `<scorerow>` tag, retrieves its text `("Verbal: 84")`, splits this text by ":", and takes the first element of the resulting list `("Verbal")`, converting it to lowercase to match `"verbal"`

`Option 3` expression creates a list of kind attributes for all `<scorerow>` elements. The second to last (-2) element in this list corresponds to the kind attribute of the first `<scorerow>` in the second `<scorelist>` tag, which is also `"verbal"`

`Option 2` attempts to get an attribute ready from the `<sat>` tag, which does not exist as an attribute.

`Option 5` tries to retrieve a kind attribute from a `<scorelist>` tag, but `<scorelist>` does not have a kind attribute.

# END SOLN

# END SUBPROB

# BEGIN SUBPROB(6 pts) Consider the following function.

```py
def summer(tree):
    if isinstance(tree, list):
        total = 0
        for subtree in tree:
            for s in subtree.find_all("scorenum"):
                total += int(s.text)
        return total
    else:
        return sum([int(s.text) for s in tree.find_all("scorenum")])
```

For each of the following values, fill in the blanks to assign `tree` such that `summer(tree)` evaluates to the desired value. The first example has been done for you.

- Desired value: `84`

```py
    tree = soup.find(_____)
```

`"scorerow"`

- Desired value: `183`

```py
    tree = soup.find(__a__)
```

- Desired value: `1480`

```py
    tree = soup.find(__b__)
```

- Desired value: `899`

```py
    tree = soup.find_all(__c__)
```

# BEGIN SOLN

**Answer: ** a: `"scorelist"`, b: `"scorelist", attrs={"listtype":"scores"}`, c: `"scorerow", attrs={"kind":"math"}`

`soup.find("scorelist")` selects the first `<scorelist>` tag, which includes both verbal and math percentiles `(84 and 99)`. The function `summer(tree)` sums these values to get `183`.

This selects the `<scorelist>` tag with `listtype="scores"`, which contains the actual scores of verbal `(680)` and math `(800)`. The function sums these to get `1480`.

This selects all `<scorerow> `elements with `kind="math"`, capturing both the percentile `(99)` and the actual score `(800)`. Since tree is now a list, `summer(tree)` iterates through each `<scorerow>` in the list, summing their `<scorenum>` values to reach `899`.

# END SOLN

# END SUBPROB

# END PROB
