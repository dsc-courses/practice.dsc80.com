# BEGIN PROB

For this problem, consider the HTML document shown below:

```html
<html>
    <head>
        <title>Data Science Courses</title>
    </head>
    
    <body>
        <h1>Welcome to the World of Data Science!</h1>
        
        <h2>Current Courses</h2>
        
        <div class="course_list">
        
            <img alt="Course Banner", src="courses.png">
            <p>
                Here are the courses available to take:
            </p>
            <ul>
                <li>Machine Learning</li>
                <li>Design of Experiments</li>
                <li>Driving Business Value with DS</li>
            </ul> 

            <p>
                For last quarter's classes, see <a href="./2021-sp.html">here</a>.
            </p>
            
        </div>
        
        <h2>News</h2>
        
        <div class="news">
            <p class="news">
                New course on <b>Visualization</b> is launched.
                See <a href="https://http.cat/301.png" target="_blank">here</a>
            </p>
        </div>
        
    </body>
</html>
```

# BEGIN SUBPROB

How many children does the `div` node with class `course_list` contain in the Document Object Model (DOM)?

# BEGIN SOLN
**Answer: ** 4 children

Looking at the code, we could see that the `div` with class `course_list` has 4 children, namely: a `img` node, `p` node, `ul` node and `p` node.

<average>78</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

Suppose the HTML document has been parsed using `doc = bs4.BeautifulSoup(html)`. Write a line of code to get the `h1` header text in the form of a string.

# BEGIN SOLN
**Answer: ** `doc.find('h1').text`

Since there's only one `h1` element in the html code, we could simply do `doc.find('h1')` to get the `h1` element. Then simply adding `.text` will get the text of the `h1` element in the form of a string.

<average>93</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

Suppose the HTML document has been parsed using `doc = bs4.BeautifulSoup(html)`. Write a piece of code that scrapes the course names from the HTML. The value returned by your code should be a list of strings.


# BEGIN SOLN
**Answer: ** `[x.text for x in doc.find_all('li')]`

Doing `doc.find_all('li')` will find all `li` elements and return it is the form of a list. Simply performing some basic list comprehension combined `.text` to get the text of each `li` element will yield the desired result.

<average>93</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

There are two links in the document. Which of the following will return the URL of the link contained in the `div` with class `news`? Mark all that apply.

[ ] `doc.find_all('a')[1].attrs['href']`
[ ] `doc.find('a')[1].attrs['href']`
[ ] `doc.find(a, class='news').attrs['href']`
[ ] `doc.find('div', attrs={'class': 'news'}).find('a').attrs['href']`
[ ] `doc.find('href', attrs={'class': 'news'})`

# BEGIN SOLN
**Answer: ** Option A and Option D

- Option A: This option works because `doc.find_all('a')` will return a list of all the `a` elements in the order that it appears in the HTML document, and since the `a` with class `news` is the second `a` element appearing in the HTML doc, we do `[1]` to select it (as we would in any other list). Finally, we return the URL of the `a` element by getting the `'href'` attribute using `.attrs['href']`
- Option B: This does not work because `.find` will only find the first instance of `a`, which is not the one we're looking for.
- Option C: This does not work because there are no quotations around the `a`.
- Option D: This option works becuase `doc.find('div', attrs={'class': 'news'})` will first find the `div` element with `class='news'`, and then find the `a` element within that element and get the `href` attribute of that, which is what we want.
- Option E: This does not work because there is no `href` element in the HTML document.

<average>90</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

What is the purpose of the `alt` attribute in the `img` tag?

( ) It provides an alternative image that will be shown to some users at random
( ) It creates a link with text present in `alt`
( ) It provides the text to be shown below the image as a caption
( ) It provides text that should be shown in the case that the image cannot be displayed

# BEGIN SOLN
**Answer: ** Option D

^pretty self-explanatory.

<average>98</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

You are scraping a web page using the `requests` module. Your code works fine and returns the desired result, but suddenly you find that when you run your code it starts but never finishes -- it does not raise an error or return anything. What is the most likely cause of the issue?

( ) The page has a very large GIF that hasn't stopped playing
( ) You have made too many requests to the server in too short of a time, and you are being "timed out"
( ) The page contains a Unicode character that `requests` cannot parse
( ) The page has suddenly changed and has caused `requests` to enter an infinite loop

# BEGIN SOLN
**Answer: ** Option B

- Option A: We can pretty confidentely (I hope) rule this option out since whether or not a GIF has stopped playing or not shouldn't affect our web scraping.
- Option B: This answer is right because a server will time you out (and potentially block you) if you make too many requests to the server.
- Option C: This shouldn't cause your code to never finish, rather, it's more likely that the request module just doesn't process said Unicode character correctly or it throws an error.
- Option D: Again, this shouldn't cause your code to never finish, rather, the request module will just parse the older version of the website at the time you called it.

<average>78</average>

# END SOLN

# END SUBPROB

# END PROB