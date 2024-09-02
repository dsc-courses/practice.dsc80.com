# BEGIN PROB

Suppose you are trying to scrape album names from a website. The website has an
HTML table structured as follows:

```html
<table><thead>
  <tr>
    <th>Name</th> <th>Price</th> <th>Number of Reviews</th>
  </tr></thead>
<tbody>
  <tr class="row">
    <td>Radical Optimism</td> <td>25</td> <td>10000</td>
  </tr>
  <tr class="row">
    <td>Hit Me Hard and Soft</td> <td>30</td> <td>12000</td>
  </tr>
  <tr class="row">
    <td>SOS</td> <td>18</td> <td>30000</td>
  </tr>
  <!-- 997 <tr> elements omitted -->
</tbody>
</table>
```

Notice that the `<tbody>` tag contains 1000 `<tr>` elements, but only
the first three are shown above. Suppose that you've read the HTML table above
into a BeautifulSoup object called `soup`. Fill in the code below so that
the `albums` variable contains a list of all the album names with
(strictly) more than 15,000 reviews.

```python
albums = []
for tag in soup.find_all(___(a)___):
    reviews = int(___(b)___)
    if reviews > 15000:
        album = ___(c)___
        albums.append(album)
```

# BEGIN SUBPROB

What should go in blank (a)?

# BEGIN SOLN

**Answer:** `class_="row"`

# END SOLN

# END SUBPROB



# BEGIN SUBPROB

What should go in blank (b)?

# BEGIN SOLN

**Answer:** `tag.find_all('td')[2].text`

# END SOLN

# END SUBPROB



# BEGIN SUBPROB

What should go in blank (c)?

# BEGIN SOLN

**Answer:** `tag.find('td').text`

# END SOLN

# END SUBPROB

# END PROB