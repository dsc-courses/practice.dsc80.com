# BEGIN PROB

On the website for UC San Diego Health, each provider has their own page. We've scraped the HTML from one provider's web page, which you can find at the end of this exam. We then instantiated a `BeautifulSoup` object, `soup`, from this HTML.

```html
<html lang="en">
<head>
<link href="/assets/static/heroData-BGejBwUx.css" rel="stylesheet"/>
<title>Caitlin MacMillen, DO | Primary Care, Family Medicine, Osteopathic Medicine | UC San Diego Health</title>
<meta content="width=device-width, initial-scale=1, maximum-scale=5" name="viewport"/>
<meta content="Caitlin MacMillen is a Physician in San Diego with UC San Diego Health and specializing in Osteopathic Manipulative Treatment (OMT), Women's Health, Care for All Ages, Comprehensive Care for the Individual and Family, Overall Health and Well-Being, Family Planning." name="description"/>
<meta content="32.875663,-117.2133647" name="geo.position"/>
<meta content="San Diego,CA" name="geo.placename"/>
<meta content="US-CA" name="geo.region"/>
<script>window.yextAnalyticsEnabled=false;window.enableYextAnalytics=()=>{window.yextAnalyticsEnabled=true}</script>
<script type="application/ld+json">{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Physician",
      "@id": "https://providers.ucsd.edu/details/33243/primary-care-family-medicine-osteopathic-medicine",
      "name": "Caitlin MacMillen, DO",
      "usNPI": "1518321629",
      "telephone": "(858) 657-8600",
      "isAcceptingNewPatients": false,
      "url": "https://providers.ucsd.edu/details/33243/primary-care-family-medicine-osteopathic-medicine",
      "knowsLanguage": [{"@type": "Language", "name": "English"}],
      "knowsAbout": ["Osteopathic Manipulative Treatment (OMT)", "Women's Health", "Care for All Ages", "Comprehensive Care for the Individual and Family", "Overall Health and Well-Being", "Family Planning"],
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "9333 Genesee Avenue",
        "addressLocality": "San Diego",
        "addressRegion": "California",
        "postalCode": "92121",
        "addressCountry": "US"
      },
      "aggregateRating": {"@type": "AggregateRating", "ratingValue": 4.93, "bestRating": 5, "ratingCount": 188}
    }
  ]
}</script>
<script data-entity-id="16281938" id="yext-entity-data"></script>
<script async="" src="https://siteimproveanalytics.com/js/siteanalyze_14686.js"></script>
<script crossorigin="anonymous" src="https://kit.fontawesome.com/aa9c700570.js"></script>
</head>
<body>
<div id="reactele"></div>
</body>
</html>
```

# BEGIN SUBPROB

Consider the DOM tree for this document. How many children does the root node have?

( ) 1
( ) 2
( ) 3
( ) 4
( ) 5
( ) none of these

# BEGIN SOLUTION

**Answer:** 2

The root `<html>` element has two children: `<head>` and `<body>`.

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

What does the following line of code evaluate to?

```py
len(soup.find_all("script"))
```

( ) 1
( ) 2
( ) 3
( ) 4
( ) 5
( ) none of these

# BEGIN SOLUTION

**Answer:** 4

There are four `<script>` tags in the document.

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

The latitude and longitude for the provider's office location are included in the document. Write one line of code that uses `soup.find()` (not `soup.find_all()`) to extract the latitude from `soup`, as a string (`"32.875663"`).

# BEGIN SOLUTION

**Answer:** `soup.find("meta", attrs={"name": "geo.position"}).get("content").split(",")[0]`

The latitude is stored in the `content` attribute of the `<meta name="geo.position">` tag, before the comma.

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

You'll notice that the HTML includes some JSON-formatted data. Locate the JSON object with keys `"@context"` and `"@graph"`. Fill in the blank in the code below to read this JSON object in as a Python dictionary, `dr_m`.

```py
dr_m_string = ___________
dr_m = json.loads(dr_m_string)
dr_m
```

# BEGIN SOLUTION

**Answer:** `soup.find("script", attrs={"type": "application/ld+json"}).text`

The JSON data is stored as the text content of the `<script type="application/ld+json">` tag.

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Write one line of code that extracts the postal code from `dr_m`, as a string.

# BEGIN SOLUTION

**Answer:** `dr_m["@graph"][0]["address"]["postalCode"]`

The postal code is nested inside the first element of the `"@graph"` list.

# END SOLUTION

# END SUBPROB

# END PROB
