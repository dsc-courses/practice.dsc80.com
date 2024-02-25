# BEGN PROB
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
Assume that the web page is parsed into a BeautifulSoup called `soup`.
Fill in each of the expressions below to evaluate to the desired string. Pay careful attention to the indexes after each call to `find_all()`!
# BEGIN SUBPROB
"Lecture 1: 5/5 stars!"

`soup.find_all(____)[0].text`
# BEGIN SOLN
**Answer**: `soup.find_all('p')[0].text`

"Lecture 1: 5/5 stars!" is surrounded by `<p>` tags, and `find_all` will get every instance of these tags as a list. Since "Lecture 1: 5/5 stars!" is the first instance, we can get it from the index of the list, `[0]`. Then we grab just the text from `.text`.

<average>87</average>

# END SOLN
# END SUBPROB

# BEGIN SUBPROB
"Lecture 2: 6/5 stars!!"

`soup.find_all(____)[3].text`
# BEGN SOLN
**Answer**: `soup.find_all('div')[3].text`

"Lecture 2: 6/5 stars!!" appears as the text surrounded by the fourth `<div>` tag, and since we are grabbing index `[3]` we need to `find_all('div')`. Then `.text` grabs the text portion.

<average>82</average>

# END SOLN
# END SUBPROB

# BEGIN SUBPROB
"Lecture 3: 10/5 stars!!!!"

`soup.find_all(____)[1].text`
# BEGIN SOLN
**Answer**: `soup.find_all(class_='lecture')[1].text`

We need to return a list with "Lecture 3: 10/5 stars!!!!" as the second index since we access it with `[1]`. We see that we have two instances of lecture attributes, with `class="lecture notes"` and `class="lecture"`. We can use the `class_` parameter to match only with specific class attributes, and the string we pass in will look if the class contains the string, not specific matches. Therefore `class_='lecture'` will match with both of the cases listed above, and the second one, at index `[1]`, is the one we want.

<average>74</average>

# END SOLN
# END SUBPROB
# END PROB