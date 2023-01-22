# BEGIN PROB

Consider the following HTML document, which represents a webpage
containing the top few songs with the most streams on Spotify today in
Canada.

    <head>
        <title>3*Canada-2022-06-04</title>
    <head>
    <body>
        <h1>Spotify Top 3 - Canada</h1>
        <table>
            <tr class='heading'>
                <th>Rank</th>
                <th>Artist(s)</th> 
                <th>Song</th>
            </tr>
            <tr class=1>
                <td>1</td>
                <td>Harry Styles</td> 
                <td>As It Was</td>
            </tr>
            <tr class=2>
                <td>2</td>
                <td>Jack Harlow</td> 
                <td>First Class</td>
            </tr>
            <tr class=3>
                <td>3</td>
                <td>Kendrick Lamar</td> 
                <td>N95</td>
            </tr>
        </table>
    </body>

Suppose we define `soup` to be a `BeautifulSoup` object that is
instantiated using the document above.

# BEGIN SUBPROB

(1.5 pts) How many leaf nodes are there in the DOM tree of the previous
document --- that is, how many nodes have no children?

# BEGIN SOLN

There's 1 `<title>`, 1 `<h1>`, 3 `<th>`s, and 9 `<td>`s, adding up to
14.

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

(1.5 pts) What does the following line of code evaluate to?

    len(soup.find_all("td"))

# BEGIN SOLN

As mentioned in the solution to the part above, there are 9 `<td>`
nodes, and `soup.find_all` finds them all.

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

What does the following line of code evaluate to?

    soup.find("tr").get("class")

# BEGIN SOLN

`soup.find("tr")` finds the first occurrence of a `<tr>` node, and
`get("class")` accesses the value of its `"class"` attribute.

Note that technically the answer is `["heading"]`, but `"heading"`
received full credit too.

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

Complete the implementation of the function `top_nth`, which takes in a
positive integer `n` and returns the **name of the $n$-th ranked song**
in the HTML document. For instance, $\texttt{top\_nth}(2)$ should
evaluate to `"First Class"` (`n=1` corresponds to the top song).

**Note:** Your implementation should work in the case that the page
contains more than 3 songs.

    def top_nth(n):
        return soup.find("tr", attrs=__(a)__).find_all("td")__(b)__

What goes in blank (a)?

What goes in blank (b)?

# BEGIN SOLN

The logic is to find the `<tr>` node with the correct class attribute,
then access the text of the node's last `<td>` child (since that's where
the song titles are stored).

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

Suppose we run the line of code `r = requests.get(url)`, where `url` is
a string containing a URL to some online data source.

**True or False:** If `r.status_code` is `200`, then `r.text` must be a
string containing the HTML source code of the site at `url`.

( ) True
( ) False

# BEGIN SOLN

The response could be JSON, it is not necessarily HTML.

# END SOLN

# END SUBPROB

# END PROB