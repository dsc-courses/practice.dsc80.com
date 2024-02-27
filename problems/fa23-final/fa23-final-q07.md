# BEGIN PROB
Alan set up a web page for his DSC 80 note swith the following HTML:
```
<html>
	<body>
		<div id = "hero">DSC 80 NOTES</div>
		<div class="notes">
			<div class="notes">
				<p>Lecture 1: 5/5 stars!</p>
			</div>
			<div class="lecture notes">
				<p>Lecture 2: 6/5 stars!!</p>
			</div>
		</div>
		<div class="lecture">
			<p>Lecture 3: 10/5 stars!!!!</p>
		</div>
	</body>
</html>	
```
Assume that the web page is parsed into a BeautifulSoup objected named `soup`.
Fill in each of the expressions below to evaluate to the desired string. Pay careful attention to the indexes after each call to `find_all`!
# BEGIN SUBPROB
Desired string: `"Lecture 1: 5/5 stars!"`

```py
soup.find_all(____)[0].text
```
# BEGIN SOLN
**Answer**: `soup.find_all('p')[0].text`

`"Lecture 1: 5/5 stars!"` is surrounded by `<p>` tags, and `find_all` will get every instance of these tags as a list. Since `"Lecture 1: 5/5 stars!"` is the first instance, we can get it from its index in the list, `[0]`. Then we grab just the text using `.text`.

<average>87</average>

# END SOLN
# END SUBPROB

# BEGIN SUBPROB
Desired string: `"Lecture 2: 6/5 stars!!"`

```py
soup.find_all(____)[3].text
```
# BEGIN SOLN
**Answer**: `soup.find_all('div')[3].text`

`"Lecture 2: 6/5 stars!!"` appears as the text surrounded by the fourth `<div>` tag, and since we are grabbing index `[3]` we need to `find_all('div')`. Then `.text` grabs the text portion.

<average>82</average>

# END SOLN
# END SUBPROB

# BEGIN SUBPROB
Desired string: `"Lecture 3: 10/5 stars!!!!"`

```py
soup.find_all(____)[1].text
```
# BEGIN SOLN
**Answer**: `soup.find_all('div', class_='lecture')[1].text`

We need to return a list with `"Lecture 3: 10/5 stars!!!!"` as the second index since we access it with `[1]`. We see that we have two instances of `'lecture'` attributes in `div` tags: one with `class="lecture notes"` and `class="lecture"`. Note that `class="lecture notes"` actually means that the tag has two `class` attributes, one of `"lecture"` and one of `"notes"`. The `class_='lecture'` optional argument in `find_all` will find all tags that have a `'lecture'` attribute, meaning that it'll find both the `class="lecture notes"` tag and the `class="lecture"` tag. So, `soup.find_all('div', class_='lecture')` will find the two aforementioned `<div>`s, `[1]` will find the second one (which is the one we want), and `.text` will find `"Lecture 3: 10/5 stars!!!!"`.

<average>74</average>

# END SOLN
# END SUBPROB
# END PROB