import json
import unittest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class LoginForm(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver')
        self.driver.implicitly_wait(20)

    def test_EL(self):
        try:
            # Load the page url
            print('Loading Url')
            self.driver.get('https://www.ethereallacquer.com/collections/all?sort_by=title-ascending')
            # self.driver.maximize_window()
            self.driver.implicitly_wait(20)

            # Find the total number of pages
            upper_range = self.driver.find_element_by_xpath('/html/body/main/div/div/div/div/div[3]/ul/li[6]/a').text

            range_counter = 0
            polishes = []

            # Iterate through all the pages, inserting range_counter variable to create the page URL
            while range_counter < int(upper_range):
            # while range_counter <= 2:
                url = "https://www.ethereallacquer.com/collections/all?page=" + str(range_counter+1) + "&sort_by=title-ascending"
                print(url)
                self.driver.get(url)

                # Find the container div with all of the polish listings
                container = self.driver.find_element_by_xpath('/html/body/main/div/div/div/div/div[2]')

                # Within that container, identify listings that are sold out, on sale, or regular stock
                listings = container.find_elements_by_class_name("grid__item")
                for item in listings:
                    print(item.text)
                    text = item.text.split("\n")
                    print
                    if "SOLD OUT" in text[0]:
                        # print("Sold out: " + text[1])
                        # name = text[1]
                        status = "sold_out"
                    elif "SALE" in text[0] and "SOLD OUT" not in text:
                        # print("On sale: " + text[1])
                        # name = text[1]
                        status = "on_sale"
                    else:
                        print("Neither sold out nor on sale: " + text[0])
                        # name = text[0]
                        status = "regular"

                    price_regular = ""
                    price_sale = ""

                    # Save price data
                    i = 0
                    while (i<len(text)):
                        if "Regular price" in text[i]:
                            # print("REGULAR PRICE: ")
                            # print(text[i+1])
                            price_regular = text[i+1]
                        if "Sale price" in text[i]:
                            # print("SALE PRICE: ")
                            # print(text[i+1])
                            price_sale = text[i+1]
                        i += 1
                    # print(text[1])

                    # Save link, image, url, and name data for each listing 
                    link = item.find_element_by_class_name('grid-link').get_attribute('href')
                    image = item.find_element_by_class_name('product__img').get_attribute('src')
                    slug = link.split("/")[-1]
                    name = (slug.replace("-", " ")).title()
                    print(link)                    
                    # print(image)
                    print(" ---- ")

                    # Add polish data to polishes[] array
                    polishes.append({
                        "name":name,
                        "status":status,
                        "price_regular":price_regular,
                        "price_sale":price_sale,
                        "href": link,
                        "img": image,
                        "page": range_counter+1
                    })

                    # Save polish data to json, which you can view directly or use to build webpage with all results
                    with open('polishes.json', 'w') as fp:
                            json.dump(polishes, fp)

                range_counter += 1


        except AssertionError as e:
            print(e)
            raise

    def tearDown(self):
        print("Done with session %s" % self.driver.session_id)
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()