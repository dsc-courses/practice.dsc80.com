# BEGIN PROB

You are scraping a web page using `requests`. Your code has been working fine and returns the desired result, but suddenly you find that your code takes much longer to finish (if it finishes at all). It does not raise
an exception.

What is the most likely cause of the issue?

( ) The page has a very large GIF that hasn't stopped playing.
( ) You have made too many requests to the server in a short amount of time
( ) The page contains a Unicode character that `requests` cannot parse
( ) The page has suddenly changed and has caused `requests` to enter an infinite loop.

# BEGIN SOLN
**Answer: ** Option B

- Option A: We can pretty confidentely (I hope) rule this option out since whether or not a GIF has stopped playing or not shouldn't affect our web scraping.
- Option B: This answer is right because a server will time you out (and potentially block you) if you make too many requests to the server.
- Option C: This shouldn't cause your code to never finish, rather, it's more likely that the request module just doesn't process said Unicode character correctly or it throws an error.
- Option D: Again, this shouldn't cause your code to never finish, rather, the request module will just parse the older version of the website at the time you called it.

# END SOLN

# END PROB