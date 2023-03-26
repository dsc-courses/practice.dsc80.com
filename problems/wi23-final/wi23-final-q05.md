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
        <scorerow kind="verbal">
            Verbal: <scorenum>680</scorenum>
        </scorerow>
        <scorerow kind="math">
            Math: <scorenum>800</scorenum>
        </scorerow>
    </scorelist>
</sat>
```

# BEGIN SUBPROB
Which of the following expressions evaluate to `"verbal"}? Select all that apply.

[ ] `soup.find("scorerow").get("kind")`
[ ] `soup.find("sat").get("ready")`
[ ] `soup.find("scorerow").text.split(":")[0].lower()`
[ ] `[s.get("kind") for s in soup.find_all("scorerow")][-2]`
[ ] `soup.find("scorelist", attrs={"listtype":"scores"}).get("kind")`
[ ] None of the above

# BEGIN SOLN
**Answer: ** Option 1, Option 3, Option 4

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

-   Desired value: `84` 

```py
    tree = soup.find(_____)
```
`"scorerow"`

-   Desired value: `183`

```py
    tree = soup.find(__a__)
```

-   Desired value: `1480`

```py
    tree = soup.find(__b__)
```

-   Desired value: `899`

```py
    tree = soup.find_all(__c__)
```

# BEGIN SOLN
**Answer: ** a: `"scorelist"`, b: `"scorelist", attrs={"listtype":"scores"}`, c: `"scorerow", attrs={"kind":"math"}`

# END SOLN

# END SUBPROB

# END PROB