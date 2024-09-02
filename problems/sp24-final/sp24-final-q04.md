# BEGIN PROB

You want to use regular expressions to extract out the number of ounces from the
5 product names below.

| **Index** | **Product Name**                           | **Expected Output** |
|-----------|--------------------------------------------|---------------------|
| 0         | Adult Dog Food 18-Count, 3.5 oz Pouches   | 3.5                 |
| 1         | Gardetto's Snack Mix, 1.75 Ounce           | 1.75                |
| 2         | Colgate Whitening Toothpaste, 3 oz Tube   | 3                   |
| 3         | Adult Dog Food, 13.2 oz. Cans 24 Pack     | 13.2                |
| 4         | Keratin Hair Spray 2!6 oz                 | 6                   |

The names are stored in a pandas Series called `names`. For each snippet below, select the indexes for all the product names that **will not** be matched correctly.


# BEGIN SUBPROB

Snippet:

```python
regex = r'([\d.]+) oz'
names.str.findall(regex)
```

[ ] 0  
[ ] 1  
[ ] 2  
[ ] 3  
[ ] 4  
[ ] All names will be matched correctly.

# BEGIN SOLN

**Answer:** 1

# END SOLN

# END SUBPROB



# BEGIN SUBPROB

Snippet:

```python
regex = r'(\d+?.\d+) oz|Ounce'
names.str.findall(regex)
```

[ ] 0  
[ ] 1  
[ ] 2  
[ ] 3  
[ ] 4  
[ ] All names will be matched correctly.

# BEGIN SOLN

**Answer:** 1, 2, 4

# END SOLN

# END SUBPROB


# END PROB
