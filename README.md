# Goodreads Library Book Scraper 
------------
Installation 
------------

To install this app first clone the repostitory.
In bash,run the following command:

>git clone https://github.com/alisajid4041/goodreads_scraper

Next,navigate to the project directory:
> cd goodreads_scraper

Finally,run the app
>python3 scraper.py

------------
   USAGE
------------
Once this app is running, users will be prompted with two options.
1) List all Genres
2) Quit

-------------
  FEATURES
-------------
The app will then help users in seeing books from their genre of choice
The user will be prompted with an option to list all genres. Once clicked, they will be shown a list of genres such as Art, Comics etc.
When users submit their genre of choice, in little time they will be displayed a number of books from that genre.
They will be displayed, from their genre of choice, the name of the book, the authors' name and the books' ISBN if it has one.
----------------
PROJECT STRUCTURE
-----------------
The project consists of 1 file only named scraper.py.
In that python file, their are 4 functions. The menu() function simply displays the interactive window. Then there are three other functions that generate the list of genres, generate the books from that genre and rerieve each books specfic ISBN if applicable.
My program used imports such as BeautifulSoap, requests and JSON.

---------------
PROJECT DETAILS
---------------

This project was made by Ali Sajid, using python3 on Pycharm/VSCode and using libraries BeautifulSoap,requests,JSON
A simple python scraper of the www.goodreads.com to display books froma a genre of users choice.
