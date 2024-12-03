# BEGIN PROB

The two plots below show the total number of boots (top) and sandals (bottom) purchased per month in the `df` table. Assume that there is one data point per month.

<center><img src="../../assets/images/sp24-final/boot.png" style="width: 100%; height: auto;"></center>

<center><img src="../../assets/images/sp24-final/sandal.png" style="width: 100%; height: auto;"></center>


For each of the following regression models, use the visualizations shown above to select the value that is **closest** to the fitted model weights. If it is not possible to determine the model weight, select "Not enough info". For the models below:

- The notation `boot` refers to the number of boots sold.
- The notation `sandal` refers to the number of sandals sold.
- `summer=1` is a column with value 1 if the month is between March (03) and August (08), inclusive.
- `winter=1` is a column with value 1 if the month is between September (09) and February (02), inclusive.


# BEGIN SUBPROB

`boot` = w_0

w_0:

( ) 0  
( ) 50  
( ) 100  
( ) Not enough info

# BEGIN SOLN

**Answer:** 50

# END SOLN

# END SUBPROB



# BEGIN SUBPROB

`boot` = $w_0 + w_1 \cdot \text{sandal}$

w_0:

( ) -100  
( ) -1  
( ) 0  
( ) 1  
( ) 100  
( ) Not enough info

w_1:

( ) -100  
( ) -1  
( ) 1  
( ) 100  
( ) Not enough info

# BEGIN SOLN

**Answer:** 

w_0: 100

w_1: -1

# END SOLN

# END SUBPROB



# BEGIN SUBPROB

`boot` = $w_0 + w_1 \cdot (\text{summer=1})$

w_0:

( ) -100  
( ) -1  
( ) 0  
( ) 1  
( ) 100  
( ) Not enough info

w_1:

( ) -80  
( ) -1  
( ) 0  
( ) 1  
( ) 80  
( ) Not enough info

# BEGIN SOLN

**Answer:**

w_0: 100

w_1: -80

# END SOLN

# END SUBPROB



# BEGIN SUBPROB

`sandal` = $w_0 + w_1 \cdot (\text{summer=1})$

w_0:

( ) -20  
( ) -1  
( ) 0  
( ) 1  
( ) 20  
( ) Not enough info

w_1:

( ) -80  
( ) -1  
( ) 0  
( ) 1  
( ) 80  
( ) Not enough info

# BEGIN SOLN

**Answer:**

w_0: 20

w_1: 80

# END SOLN

# END SUBPROB



# BEGIN SUBPROB

`sandal` = $w_0 + w_1 \cdot (\text{summer=1}) + w_2 \cdot (\text{winter=1})$

w_0:

( ) -20  
( ) -1  
( ) 0  
( ) 1  
( ) 20  
( ) Not enough info

w_1:

( ) -80  
( ) -1  
( ) 0  
( ) 1  
( ) 80  
( ) Not enough info

w_2:

( ) -80  
( ) -1  
( ) 0  
( ) 1  
( ) 80  
( ) Not enough info

# BEGIN SOLN

**Answer:**

w_0: Not enough info

w_1: Not enough info

w_2: Not enough info

# END SOLN

# END SUBPROB

# END PROB