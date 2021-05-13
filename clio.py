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
            self.driver.get('https://clionadhcosmetics.com/collections/stained-glass-collection?page=1')
            # self.driver.maximize_window()
            self.driver.implicitly_wait(20)

            # Find the total number of pages
            upper_range = self.driver.find_element_by_xpath('/html/body/main/div/div/div/div[2]/div/div/div/ul/li[6]/a').text

            range_counter = 0
            # polishes = []
            shadows = []

            # Iterate through all the pages, inserting range_counter variable to create the page URL
            # while range_counter < int(upper_range):
            while range_counter <= 1:
                url = "https://clionadhcosmetics.com/collections/stained-glass-collection?page=" + str(range_counter+1)
                print(url)
                self.driver.get(url)

                # Find the container div with all of the polish listings
                container = self.driver.find_element_by_xpath('/html/body/main/div/div/div/div[1]/div[2]')

                # Within that container, identify listings that are sold out, on sale, or regular stock
                listings = container.find_elements_by_class_name("grid-item")
                for item in listings:
                    print(item.text)
                    text = item.text.split("\n")
                    name = text[-5]
                    price_regular = text[-2]
                    print("Regular price: " + price_regular)
                    print("\n")

                    name = text[-5]
                    if "SOLD OUT" in text[0]:
                        # print("Sold out: " + text[1])
                        # name = text[1]
                        status = "sold_out"
                    # # elif "SALE" in text[0] and "SOLD OUT" not in text:
                    # #     # print("On sale: " + text[1])
                    # #     # name = text[1]
                    # #     status = "on_sale"
                    else:
                        # print("Neither sold out nor on sale: " + text[0])
                        # name = text[0]
                        status = "regular"


                    # price_sale = ""

                    # # Save price data
                    # i = 0
                    # while (i<len(text)):
                    #     if "Regular price" in text[i]:
                    #         # print("REGULAR PRICE: ")
                    #         # print(text[i+1])
                    #         price_regular = text[i+1]
                    #     if "Sale price" in text[i]:
                    #         # print("SALE PRICE: ")
                    #         # print(text[i+1])
                    #         price_sale = text[i+1]
                    #     i += 1
                    # # print(text[1])

                    # # Save link, image, url, and name data for each listing 
                    link = item.find_element_by_class_name('shop-now-button').get_attribute('href')

                    # image_wrapper = item.find_element_by_class_name('lazyload__image-wrapper')
                    # image = item.find_element_by_class_name('no-js lazyautosizes lazyloaded').get_attribute('src')
                    # linkElem = self.driver.find_element_by_xpath('//img[@alt="' + name + '"]').get_attribute('src')
                    image_container = item.find_element_by_class_name('product-grid-image')
                    linkElem = image_container.find_element(By.TAG_NAME, 'img').get_attribute('srcset')
                    print(linkElem)
                    # slug = link.split("/")[-1]
                    # name = (slug.replace("-", " ")).title()
                    # print(link)                    
                    # # print(image)
                    # print(" ---- ")

                    # Add polish data to polishes[] array
                    shadows.append({
                        "name":name,
                        "status":status,
                        "price_regular":price_regular,
                        # "price_sale":price_sale,
                        "href": link,
                        "img": linkElem,
                        "page": range_counter+1
                    })

                    # Save polish data to json, which you can view directly or use to build webpage with all results
                    with open('shadows.json', 'w') as fp:
                            json.dump(shadows, fp)

                range_counter += 1


        except AssertionError as e:
            print(e)
            raise

    def tearDown(self):
        print("Done with session %s" % self.driver.session_id)
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()