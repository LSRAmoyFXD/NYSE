# coding = utf-8
import calendar
import random
import time
import unittest
import selenium
import urllib
import requests
from selenium import webdriver


class NYSE(unittest.TestCase):
    def setUp(self):
        path = 'C:/Users/lsram/Downloads/chromedriver_win32/chromedriver'
        self.driver = webdriver.Chrome(path)

    def tearDown(self):
        self.driver.close()

    def test_1(self):
        self.driver.get("https://www.nyse.com/index")
        time.sleep(random.randint(1, 5))
        self.driver.find_element_by_xpath(
            '//*[@id="content-c37580c1-3072-4b0a-82a2-1fbe77004d04"]/nav/ul/li[4]').click()
        time.sleep(random.randint(1, 5))
        self.driver.find_element_by_xpath(
            '//*[@id="content-c37580c1-3072-4b0a-82a2-1fbe77004d04"]/nav/ul/li[4]/div/div[2]/ul/li[1]/a').click()
        time.sleep(random.randint(1, 5))

        # Getting all the historical data in 2019\
        mon = []
        for i in range(1, 13):
            url = "https://www.nyse.com/publicdocs/nyse/data/Monthly_Consolidated_Volume_by_Symbol_20191{0}.pdf".format(
                str(i))
            r = requests.get(url, stream=True)
            file_name = '2019-' + str(i) + '.pdf'
            print("Downloading file:%s" % file_name)
            with open(file_name, 'wb') as f:
                for chunk in r.iter_content(chunk_size=1024 * 1024):
                    if chunk:
                        f.write(chunk)
            f.close()
            time.sleep(random.randint(1, 5))


if __name__ == '__main__':
    unittest.main()
