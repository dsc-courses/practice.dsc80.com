# BEGIN PROB

# BEGIN SUBPROB

Rahul is trying to scrape the website of an online bookstore 'The Book
Club'.

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

Which is the equivalent Document Object Model (DOM) tree of this HTML
file?

![image](final_images/question4_options.pdf){width="6.2in"}

( ) Tree A

( ) Tree B

( ) Tree C

( ) Tree D

# BEGIN SOLUTION

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Rahul wants to extract the `‘instock availability’` status of the book
titled 'A Light in the Attic'. Which of the following expressions will
evaluate to `"In Stock"`? Assume that Rahul has already parsed the HTML
into a BeautifulSoup object stored in the variable named `soup`.\
( ) Code Snippet A

        soup.find('p',attrs = {'class': 'instock availability'})\
            .get('icon-ok').strip()

( ) Code Snippet B

        soup.find('p',attrs = {'class': 'instock availability'}).text.strip()

( ) Code Snippet C

        soup.find('p',attrs = {'class': 'instock availability'}).find('i')\
            .text.strip()

( ) Code Snippet D

        soup.find('div', attrs = {'class':'product_price'})\
            .find('p',attrs = {'class': 'instock availability'})\
            .find('i').text.strip()

# BEGIN SOLUTION

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Rahul also wants to extract the number of stars that the book titled 'A
Light in the Attic' received. If you look at the HTML file, you will
notice that the book received a star rating of three. Which code snippet
will evaluate to `"Three"`?\
( ) Code Snippet A

        soup.find('article').get('class').strip()

( ) Code Snippet B

        soup.find('p').text.split(' ')

( ) Code Snippet C

        soup.find('p').get('class')[1]

( ) None of the above

# BEGIN SOLUTION

# END SOLUTION

# END SUBPROB

# END PROB