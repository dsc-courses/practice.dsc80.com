# BEGIN PROB

# BEGIN SUBPROB

Rahul is trying to scrape the website of an online bookstore 'The Book Club'.
  
```html
<HTML>
<H1>The Book Club</H1>
<BODY BGCOLOR="FFFFFF">
Email us at <a href="mailto:support@thebookclub.com">
support@thebookclub.com</a>.

<div>
	<ol class="row">
	<li class="book_list">
	
		<article class="product_pod">
			<div class="image_container">
					<img src="pic1.jpeg" alt="A Light in the Attic" 
					class="thumbnail">
			</div>
			
			<p class="star-rating Three"></p>
			
			<h3>
			<a href="cat/index.html" title="A Light in the Attic">
			A Light in the Attic
			</a>
			</h3>
		
			<div class="product_price">
				<p class="price_color">£51.77</p>
				
				<p class="instock availability">
					<i class="icon-ok"></i>
					In stock
				</p>
		
			</div>
		</article>
	</li>
	</ol>

</div>
</BODY>
</HTML>
```

Which is the equivalent Document Object Model (DOM) tree of this HTML file?

<center><img  src='../assets/images/sp23-final/q4.png'  width=40%></center>

( ) Tree A
( ) Tree B
( ) Tree C
( ) Tree D

# BEGIN SOLN
**Answer:** Tree D

Following tree D in the image from top to bottom, we can follow the nesting
of tags in the HTML file to verify that the DOM tree D matches the syntax of 
the HTML file.

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

Rahul wants to extract the `‘instock availability’` status of the book titled 'A Light in the Attic'. Which of the following expressions will evaluate to `"In Stock"`? Assume that Rahul has already parsed the HTML into a BeautifulSoup object stored in the variable named `soup`.

Code Snippet A
```py
    soup.find('p',attrs = {'class': 'instock availability'})\
    .get('icon-ok').strip()
```

Code Snippet B
```py
    soup.find('p',attrs = {'class': 'instock availability'}).text.strip()
```

Code Snippet C
```py
    soup.find('p',attrs = {'class': 'instock availability'}).find('i')\
    .text.strip()
```

Code Snippet D
```py
    soup.find('div', attrs = {'class':'product_price'})\
    .find('p',attrs = {'class': 'instock availability'})\
    .find('i').text.strip()
```

# BEGIN SOLN
**Answer:** Code Snippet B

Code Snippet B is the only option that finds the tag `p` with the attribute 
`class` being equal to `instock availability` and then getting the text contained 
in that tag, which is equal to `‘instock availability’`.

Option A will cause an error because of `.get('icon-ok')` since `'icon-ok'` is
not the name of the attribute, but is instead the value of the `class` attribute.

Option C and D will both get the text of the `i` tag, which is `''` and is 
therefore incorrect.

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

Rahul also wants to extract the number of stars that the book titled 'A Light in the Attic' received. If you look at the HTML file, you will notice that the book received a star rating of three. Which code snippet will evaluate to `"Three"`?

Code Snippet A
```py
    soup.find('article').get('class').strip()
```

Code Snippet B
```py
    soup.find('p').text.split(' ')
```

Code Snippet C
```py
    soup.find('p').get('class')[1]
```

None of the above

# BEGIN SOLN
**Answer:** Code Snippet C

Code Snippet C finds the first occurence of the tag `p`, gets the contents of 
its `class` attribute as a list, and returns the last element, which is the rating `'Three'` as desired.

Option A will error because `.get('class')` returns `['product_pod']` and strip cannot be used on a list, 
but also the content of the list does not bring us closer to the desired result.

Option B gets the text contained within the first `p` tag as a list, which is `['']`.

# END SOLN

# END SUBPROB

# END PROB