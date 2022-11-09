# simplify-scraper

developed on Python 3.9.12

looking for jobs right now. I use the simplify chrome extension to fill in and help keep track of applications. It stores the data fine, but I want to analyze my applications. It isn't possible to download data from the app's webpage. this app will be able to parse each posting and then load it into a csv.

optionally it can load the data into a SQL database. 


# dev notes

to even get the proper HTML i needed to insepct the page and manually copy it from there. it is because the page is loaded from JS.

possibly automating this with requests, but not sure about authentication

data-testid="application-card"

# future optimizations
adding each app card to the csv as they are read in. this will improve memory. it isn't a big concern because I don't expect 1000s of applications. adding these cards to a database will be good too as they are added