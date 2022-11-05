# app.py

from bs4 import BeautifulSoup

# load in from html_tasks directory

file_name = "tasks/applied.html"

# iterate this taks through each html doc in the html_tasks directory
with open(file_name, "r") as file:
    soup = BeautifulSoup(file, 'html.parser')
    
# id main contains all of the application cards

# data-testid="application-card" for each card

# searching through each element until the arrs match the application card, finding the level and searching appropriately