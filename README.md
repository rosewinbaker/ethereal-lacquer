# ethereal-lacquer

I love to support indie and boutique nail polishes and sometimes find it diffcult to keep track of in-stock options, as many tend to sell out quickly and remain listed on the product pages.

This Selenium script pulls polish data from the Ethereal Lacquer website, saves polish data to a .json file which is then used to populate a web page with all available, in-stock options easily visible and accessible.

From this:

![Photo of Ethereal Lacquer with mostly sold-out listing](./original.JPG)

To this:

![Photo of script results displayed in web browser](./result.JPG)

### Requirements 

* Selenium

* Python 3.x.x

* Webdriver for your browser of choice. I am using Chromedriver for Chrome browser.


### How to Run

1. Clone this repository
1. Make sure you have the appropriate webdriver for your browser of choice in the main project directory. 
1. Run el.py
    1. This should create an updated polishes.json file with all current polish data. 
1. Open polishes.html to see all of the available polishes, with links to original website purchase link, all on one page.
1. Go support that small business and enjoy your beautiful nails.