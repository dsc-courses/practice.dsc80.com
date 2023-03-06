# BEGIN PROB

Questions 11-13 below reference the following HTML.

```html
<html>
    <head>
        <title>ZOMBO</title>
    </head>

    <body>
        <h1>Welcome to Zombo.com</h1>
        <div id="greeting">
            <ul>
                <li>This is Zombo.com, welcome!</li>
                <li>This is Zombo.com</li>
                <li>Welcome to Zombo.com</li>
                <li>You can do anything at Zombo.com -- anything at all!</li>
                <li>The only limit is yourself.</li>
            </ul>
        </div>
        <div id="footnotes" class="faded">
            <h3>Footnotes</h3>

            <ol id="footnotes">
                <li>Please consider <a href="paypal.html">donating!</a></li>
                <li>Made in California with <a href="https://reactj.org">React.</a><li>
            </ol>
        </div>
    </body>
</html>
```


# BEGIN SUBPROB
Consider the node representing the `body` tag in the Document Object Model (DOM) tree of the above HTML. How many children does this node have?

# BEGIN SOLN
**Answer: ** 3

We could count the number of children of the body tag by looking at the indentations to see that the body tag has three children: 1 <h1> element and 2 <div> elements. 

<average>89</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB
The page shown above contains five `greetings`, each one a list item in an unordered list. The first `greeting` is `This is Zombo.com, welcome!`, and the last is `The only limit is yourself.`.

Suppose we have parsed the HTML into a `BeautifulSoup` object stored in the variable named `soup`.

Which of the following pieces of code will produce a list of `BeautifulSoup` objects, each one representing a single greeting list item? Mark all which apply.

[ ] `soup.find('div').find_all('li')`
[ ] `soup.find_all('li', id='greeting')`
[ ] `soup.find('div', id='greeting').find_all('li')`
[ ] `soup.find_all('ul/li')`

# BEGIN SOLN
**Answer: ** Option A and Option C

Option A works because `find('div')` will navigate to the first `div` element, and `find_all('li')` will get all the `li` elements in the form of a list, which is what we wanted. Looking at Option C, we could see that it does basically the exact same thing so that option is correct as well. Option B wouldn't work because the `li` elements don't have an attribute 'greetings', and Option D doesn't work because there are no `ul/li` elements.

<average>85</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB
Suppose you perform an HTTP request to a web API using the `requests` module. The response succeeds, and you get the following (truncated) content back:

```py
>>> resp = requests.get("https://pokeapi.co/api/v2/pokemon/squirtle")
>>> resp.content
b'{"abilities":[{"ability":{"name":"torrent","url":"https://pokeapi.co"...
```

What type of data has been returned?

( ) HTML
( ) JSON
( ) XML
( ) PNG

# BEGIN SOLN
**Answer: ** JSON

From the format of the contents, we could pretty clearly see that it is not an HTML file, nor is it a PNG file (which is type of image file). Now an XML file also doesn't look like that, rather it looks more like an HTML file with different kinds of tags. By process of elimination, the answer is JSON.

Alternatively, we could recall that JSON files are in the format of dictionaries of attrivute/value pairs, which is what we see in the contents.

<average>94</average>

# END SOLN

# END SUBPROB

# END PROB