# BEGIN PROB

Suppose `site` is a `BeautifulSoup` object instantiated on the HTML document below.

```html
<html>
    <div align="center">
        <h3>Luxury Hotels in Bali from May 2-6, 2024 for Ethan</h3>
        <div class="chain" name="Hilton">
            <h3 style="color: blue">Hilton Properties in Bali</h3>
        </div>
        <div class="chain" name="Marriott">
            <h3 style="color: red">Marriott Properties in Bali</h3>
        </div>
        <div __(i)__>
            __(ii)__
        </div>
    </div>
</html>
```

# BEGIN SUBPROB

What does `len(site.find_all("div"))` evaluate to? Give your answer as an integer. For this part only, assume that both blank (i) and blank (ii) are left blank.

# BEGIN SOLUTION

**Answer:** 4

The answer simply requires counting the number of `div` elements, making sure not to double-count opening and closing tags.

<average>82</average>

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Fill in the blank so that `chain_color` takes in the name of a hotel chain and returns the color used to display the hotel chain in site. For example, `chain_color("Hilton")` should return `"blue"` and `chain_color("Marriott")` should return `"red"`.

```py
chain_color = lambda chain: site.____.split()[-1]
```

# BEGIN SOLUTION

**Answer:** `find("div", attrs={"name": chain}).find("h3").get("style")`

The solution finds all `div` elements whose `name` attribute is equal to the function input `chain` (which is how the chains are defined in the HTML document). Then, the colors are stored as part of the `style` attribute in an `h3` tag within that `div`, so we find the first -- and in this document, only -- `h3` tag within the `div` and get its `style` attribute. This returns a string like `color: red`, from which the given code `.split()[-1]` returns the last word, which is the correct color.

<average>67</average>

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Fill in blanks (i) and (ii) in `site` so that the following all evaluate to True:

- `len(site.find all("div", class ="chain")) == 2`
- `chain_color("Hyatt") == "purple"`
- `site.find all("div")[-1].text == ""`

1. What goes in blank (i)?
2. What goes in blank (ii)?

# BEGIN SOLUTION

**Answers:**

1. `name = "Hyatt"`
2. `<h3 style="color: purple"></h3>`

In order to make all of the three given statements true, we need to make it such that there are 2 `div` elements with class `chain`, the `chain_color` function returns `purple` for `Hyatt`, and the last `div` tag in the document has no text.

We do this by defining a `div` similar to the previous two, but without the `chain` class (because there are already 2 in the document). In order for `chain_color("Hyatt")` to return `purple`, we add `"Hyatt"` as a `name` attribute in the `div`, and add an `h3` tag within that `div` with `style="color: purple"`. However, since the last statement requires the last `div` in the document has no text, and the `div` we're currently making will be the final one, we don't include any text in the `h3` tag. (Note that because the `chain_color` function doesn't use the hotel name in the text to find a given chain's name, but rather the name attribute in the enclosing `div` tag.)

<average>90</average>

# END SOLUTION

# END SUBPROB

# END PROB


