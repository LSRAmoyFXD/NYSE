import random
import time
import unittest
import os
import requests
from selenium import webdriver
from config import ConfigClass



class WebTest(unittest.TestCase):

    os_info = os.uname()
    system = getattr(os_info, "sysname")
    # In current repo we only have driver for chrome 86
    if system == 'Darwin':
        driver = './driver/mac/chromedriver'
    elif system == 'Ubuntu':
        driver = './driver/lin/chromedriver.exe'
    else:
        driver = './driver/win/chromedriver'

    def setUp(self):
        path = self.driver
        self.driver = webdriver.Chrome(path)

    def tearDown(self):
        self.driver.close()

    def test_1(self):
        self.driver.get(ConfigClass.base_url)
        time.sleep(random.randint(1, 5))
        self.driver.find_element_by_xpath(ConfigClass.xpath1).click()
        time.sleep(random.randint(1, 5))
        self.driver.find_element_by_xpath(ConfigClass.xpath2).click()
        time.sleep(random.randint(1, 5))

        # Getting all the historical data in 2019\
        if not os.path.isdir("./pdf_result"):
            os.makedirs("./pdf_result")

        for i in range(1, 13):
            url = ConfigClass.request_url + "/Monthly_Consolidated_Volume_by_Symbol_20191{0}.pdf".format(str(i))
            r = requests.get(url, stream=True)
            file_name = "./pdf_result/" + '2019-' + str(i) + '.pdf'
            print("Downloading file:%s" % file_name)
            with open(file_name, 'wb') as f:
                for chunk in r.iter_content(chunk_size=1024 * 1024):
                    if chunk:
                        f.write(chunk)
            f.close()
            time.sleep(random.randint(1, 5))


if __name__ == '__main__':
    unittest.main()
