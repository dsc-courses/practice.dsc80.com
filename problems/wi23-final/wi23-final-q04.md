# BEGIN PROB

To prepare for the verbal component of the SAT, Nicole decides to read research papers on data science. While reading these papers, she notices that there are many citations interspersed that refer to other research papers, and she'd like to read the cited papers as well.

In the papers that Nicole is reading, citations are formatted in the _verbost numeric_ style. An excerpt from one such paper is stored in the string `s` below.

```py
s = '''
In DSC 10 [3], you learned about babypandas, a strict subset
of pandas [15][4]. It was designed [5] to provide programming
beginners [3][91] just enough syntax to be able to perform
meaningful tabular data analysis [8] without getting lost in
100s of details.
'''
```

We decide to help Nicole extract citation numbers from papers. Consider the following four extracted lists.

```py
list1 = ['10', '100']
list2 = ['3', '15', '4', '5', '3', '91', '8']
list3 = ['10', '3', '15', '4', '5', '3', '91', '8', '100']
list4 = ['[3]', '[15]', '[4]', '[5]', '[3]', '[91]', '[8]']
list5 = ['1', '0', '3', '1', '5', '4', '5', '3',
         '9', '1', '8', '1', '0', '0']
```

For each expression below, select the list it evaluates to, or select "None of the above."

# BEGIN SUBPROB

`re.findall(r'\d+', s)`

( ) list1
( ) list2
( ) list3
( ) list4
( ) list5
( ) None of the above

# BEGIN SOLN

**Answer: ** list3

This regex pattern `\d+` matches one or more digits anywhere in the string. It doesn't concern itself with the context of the digits, whether they are inside brackets or not. As a result, it extracts all sequences of digits in s, including '10', '3', '15', '4', '5', '3', '91', '8', and '100', which together form list3. This is because \d+ greedily matches all contiguous digits, capturing both the citation numbers and any other numbers present in the text.

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

`re.findall(r'[\d+]', s)`

( ) list1
( ) list2
( ) list3
( ) list4
( ) list5
( ) None of the above

# BEGIN SOLN

**Answer: ** list5

his pattern `[\d+]` is slightly misleading because the square brackets are used to define a character class, and the plus sign inside is treated as a literal character, not as a quantifier. However, since there are no plus signs in s, this detail does not affect the outcome. The character class \d matches any digit, so this pattern effectively matches individual digits throughout the string, resulting in list5. This list contains every single digit found in s, separated as individual string elements.

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

`re.findall(r'\[(\d+)\]', s)`

( ) list1
( ) list2
( ) list3
( ) list4
( ) list5
( ) None of the above

# BEGIN SOLN

**Answer: ** list2

This pattern is specifically designed to match digits that are enclosed in square brackets. The `\[(\d+)\]` pattern looks for a sequence of one or more digits `\d+` inside square brackets `[]`. The parentheses capture the digits as a group, excluding the brackets from the result. Therefore, it extracts just the citation numbers as they appear in s, matching list2 exactly. This method is precise for extracting citation numbers from a text formatted in the verbose numeric style.

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

`re.findall(r'(\[\d+\])', s)`

( ) list1
( ) list2
( ) list3
( ) list4
( ) list5
( ) None of the above

# BEGIN SOLN

**Answer: ** list4

Similar to the previous explanation but with a key difference: the entire pattern of digits within square brackets is captured, including the brackets themselves. The pattern `\[\d+\]` specifically searches for sequences of digits surrounded by square brackets, and the parentheses around the entire pattern ensure that the match includes the brackets. This results in list4, which contains all the citation markers found in s, preserving the brackets to clearly denote them as citations.

# END SOLN

# END SUBPROB

# END PROB
