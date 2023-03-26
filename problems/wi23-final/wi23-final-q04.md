# BEGIN PROB
To prepare for the verbal component of the SAT, Nicole decides to read research papers on data science. While reading these papers, she notices that there are many citations interspersed that refer to other research papers, and she'd like to read the cited papers as well.

In the papers that Nicole is reading, citations are formatted in the *verbost numeric* style. An excerpt from one such paper is stored in the string `s` below.

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

# END SOLN

# END SUBPROB

# END PROB